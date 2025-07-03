from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Check if 'file' is present in the form-data
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # You can save the file to disk (optional, for testing)
    file.save('uploaded.wav')

    return jsonify({'message': f'File {file.filename} uploaded successfully!'}), 200

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

@app.route('/healthz')
def healthz():
    return 'ok', 200

# Do NOT add app.run(); Gunicorn starts the app in production.
