from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = './'  # Or '/tmp' if you want a safer temp folder

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Check if 'file' is in the request (from form-data)
    if 'file' not in request.files:
        return jsonify({'error': 'No file part. Use key \"file\" in form-data.'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file (overwrite if exists)
    try:
        save_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(save_path)
        print(f"File saved at {save_path}")  # This appears in Render logs!
        return jsonify({'message': f'File {file.filename} uploaded successfully!'}), 200
    except Exception as e:
        print(f"Error saving file: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/files')
def list_files():
    # List all files in the upload folder
    files = os.listdir(UPLOAD_FOLDER)
    # Only show files (skip folders)
    files = [f for f in files if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
    return jsonify(files)

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

@app.route('/hea
