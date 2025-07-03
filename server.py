import os
from flask import Flask, request, jsonify
import openai
import whisper

app = Flask(__name__)

# Securely load OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # 1. Check if file is in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part. Use key "file" in form-data.'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 2. Save the uploaded file
    filepath = 'uploaded.wav'
    try:
        file.save(filepath)
        print(f"File {file.filename} uploaded and saved as {filepath}")
    except Exception as e:
        return jsonify({'error': f'File save failed: {str(e)}'}), 500

    # 3. Transcribe audio using Whisper
    try:
        # If using OpenAI Whisper API (recommended for prod, not local)
        with open(filepath, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        result = transcript.text if hasattr(transcript, "text") else str(transcript)
        return jsonify({'transcript': result}), 200

        # # If using local whisper (if GPU available, UNCOMMENT & comment out above):
        # model = whisper.load_model("base")
        # result = model.transcribe(filepath)
        # return jsonify({'transcript': result['text']}), 200

    except Exception as e:
        return jsonify({'error': f'Transcription failed: {str(e)}'}), 500

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

@app.route('/healthz')
def healthz():
    return 'ok', 200

# Do NOT add if __name__ == "__main__": ... Render uses gunicorn
