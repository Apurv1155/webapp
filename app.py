import os
from flask import Flask, request, send_from_directory, jsonify, render_template
from flask_cors import CORS

# Android storage support
try:
    from android.storage import app_storage_path
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE
    ])
    STORAGE_PATH = app_storage_path()
except ImportError:
    STORAGE_PATH = os.path.abspath(".")

# Known faces folder in internal storage
KNOWN_FACES_DIR = os.path.join(STORAGE_PATH, "known_faces")
os.makedirs(KNOWN_FACES_DIR, exist_ok=True)

# Flask app setup
app = Flask(__name__, static_folder="assets")
CORS(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory("assets", filename)

@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.json
    name = data.get("name", "unknown")
    content = data.get("content", "")

    save_path = os.path.join(KNOWN_FACES_DIR, f"{name}.txt")
    with open(save_path, "w") as f:
        f.write(content)

    return jsonify({"status": "success", "saved_to": save_path})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
