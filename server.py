from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Get OpenAI API key from environment variable
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

@app.route('/', methods=['GET'])
def home():
    return "ResumeKaruAI backend is running!", 200

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    audio_file = request.files['file']
    files = {
        'file': (audio_file.filename, audio_file, audio_file.content_type)
    }
    data = {
        'model': 'whisper-1',
        'response_format': 'text'
    }
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}'
    }
    response = requests.post(
        'https://api.openai.com/v1/audio/transcriptions',
        headers=headers,
        data=data,
        files=files
    )
    if response.status_code == 200:
        transcript = response.text
        return jsonify({'transcript': transcript})
    else:
        return jsonify({'error': response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

