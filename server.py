from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part. Use key "file" in form-data.'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file temporarily
    try:
        filepath = 'uploaded.wav'
        file.save(filepath)

        # Transcribe using OpenAI Whisper API
        with open(filepath, 'rb') as audio_file:
            response = requests.post(
                "https://api.openai.com/v1/audio/transcriptions",
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}"
                },
                files={
                    "file": (file.filename, audio_file, "audio/wav")
                },
                data={
                    "model": "whisper-1"
                }
            )

        if response.status_code == 200:
            result = response.json()
            transcript = result.get('text', '')
            return jsonify({'transcript': transcript}), 200
        else:
            return jsonify({'error': response.text}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

@app.route('/healthz')
def healthz():
    return 'ok', 200

# Do NOT add: if __name__ == "__main__": ... etc. Render runs gunicorn.
