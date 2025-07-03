from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Check if the request contains a file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # (You can save the file or process with Whisper here)
    # For now, just return the filename
    return jsonify({
        "filename": file.filename,
        "message": "File received!"
    }), 200

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

@app.route('/healthz')
def healthz():
    return 'ok', 200

# DO NOT manually call app.run() when using gunicorn/Render!
