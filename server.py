from flask import Flask, request, jsonify 
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'ResumeKaru backend is running!'})

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if not OPENAI_API_KEY:
        return jsonify({'error': 'OpenAI API key missing in environment variables'}), 500

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
        try:
            error = response.json()
        except Exception:
            error = response.text
        return jsonify({'error': error}), response.status_code

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render ke liye dynamic port le raha hai
    app.run(host="0.0.0.0", port=port)
