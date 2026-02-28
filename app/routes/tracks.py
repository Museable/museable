import os

from flask import Blueprint, request, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required

from ..utils.auth import role_required
from ..services.track_service import get_all_tracks, create_new_track, get_track_location_from_id

TRACKS_FILE_LOCATION = "audiodata/"
ALLOWED_EXTENSIONS = ["mp3", "flac", "wav", "webm"]

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

tracks_bp = Blueprint("tracks", __name__)

@tracks_bp.get("/")
def list_tracks():
    return jsonify(get_all_tracks())

@tracks_bp.post("/create")
@role_required("publisher")
def publish_track():

    data = request.form
    if not data.get("title"):
        return jsonify({"error": "Title is required"}), 400
    if not data.get("artist"):
        return jsonify({"error": "Artist is required"}), 400
    if not data.get("album"):
        return jsonify({"error": "Album is required"}), 400
    if not data.get("cover"):
        return jsonify({"error": "Cover is required"}), 400

    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    track = request.files['file']
    if track.filename == '':
        return jsonify({"error": "File empty"})
    if track and allowed_file(track.filename):
        filename = secure_filename(track.filename)
        track_path = os.path.join(TRACKS_FILE_LOCATION, filename)
        track.save(track_path)
        create_new_track(data["title"], data["artist"], data["album"], data["cover"], track_path)

    return jsonify({"success": True}), 200

@tracks_bp.get("/play/<id>")
@jwt_required()
def play_track(id):
    return send_file(get_track_location_from_id(id))
