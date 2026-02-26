from flask import Blueprint, jsonify
from ..services.track_service import get_all_tracks

tracks_bp = Blueprint("tracks", __name__)

@tracks_bp.get("/")
def list_tracks():
    return jsonify(get_all_tracks())