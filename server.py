from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Check if 'file' is in the request (form-data)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file
    file.save('uploaded.wav')
    return jsonify({'message': f'File {file.filename} uploaded successfully!'}), 200

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

@app.route('/healthz')
def healthz():
    return 'ok', 200

# DO NOT add:
# if __name__ == "__main__":
#     app.run()
# Gunicorn handles starting the app in Render.
