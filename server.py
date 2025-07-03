from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# Set OpenAI API key globally from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

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

    filename = 'uploaded.wav'
    file.save(filename)
    print(f"File {file.filename} uploaded and saved as {filename}")

    # Check if API key is set
    if not openai.api_key:
        print("Error: OpenAI API key not set in environment variables.")
        return jsonify({'error': 'OpenAI API key not set in environment variables.'}), 500

    # Transcribe using OpenAI Whisper API
    try:
        with open(filename, "rb") as audio_file:
            transcript = openai.audio.transcriptions.create(
                file=audio_file,
                model="whisper-1"
            )
        print("Transcription successful:", transcript)
        return jsonify({
            'message': f'File {file.filename} uploaded and transcribed successfully!',
            'transcription': transcript.text
        }), 200
    except Exception as e:
        print("Error in /transcribe:", str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

@app.route('/healthz')
def healthz():
    return 'ok', 200

# Do NOT add: if __name__ == "__main__": ... etc. Render runs gunicorn.
