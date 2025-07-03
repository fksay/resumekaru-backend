from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "ResumeKaruAI backend is running!"

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    # Just confirms POST is working; expand logic as needed.
    return jsonify({"message": "Received"}), 200

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
