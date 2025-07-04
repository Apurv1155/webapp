import os
import base64
import cv2
import numpy as np
import json
import random
import smtplib
import threading
from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# ---- Android-specific storage path handling ----
try:
    from android.storage import app_storage_path
    STORAGE_DIR = app_storage_path()
except ImportError:
    STORAGE_DIR = os.path.dirname(__file__)

KNOWN_FACES_DIR = os.path.join(STORAGE_DIR, "known_faces")
os.makedirs(KNOWN_FACES_DIR, exist_ok=True)

# ---- Flask Setup ----
app = Flask(__name__, static_folder="assets")
CORS(app)

# ---- Static route for assets (logo, mp3 etc.) ----
@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory("assets", filename)

@app.route('/')
def index():
    return render_template("index.html")
