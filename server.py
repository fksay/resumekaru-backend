from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Check if 'file' is in the request (from form-data)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part. Use key "file" in form-data.'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file (overwrite if exists)
    try:
        filename = 'uploaded.wav'
        file.save(filename)
        print(f"File {file.filename} uploaded and saved as {filename}")

        # You can add OpenAI Whisper logic here in the next step
        # Example: get key like this:
        # openai_api_key = os.environ.get("OPENAI_API_KEY")
        # (Don't add transcription logic until next step!)

        return jsonify({'message': f'File {file.filename} uploaded successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

@app.route('/healthz')
def healthz():
    return 'ok', 200

# Do NOT add: if __name__ == "__main__": ... etc. Render runs gunicorn.
