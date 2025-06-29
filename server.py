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

@app.route('/healthz')
def healthz():
    return 'ok', 200

# DO NOT manually call app.run() when using gunicorn on Render
