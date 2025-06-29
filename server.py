from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    data = request.get_json(force=True, silent=True)
    return jsonify({"received": data}), 200

@app.route('/routes')
def show_routes():
    return jsonify([str(rule) for rule in app.url_map.iter_rules()])

# Do NOT add app.run() here.
# Gunicorn will automatically use 'app' when you deploy on Render.
