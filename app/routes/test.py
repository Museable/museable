from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..utils.auth import role_required

test_bp = Blueprint("test", __name__)

@test_bp.get("/public")
def public():
    return "Hello", 200

@test_bp.get("/logged")
@jwt_required()
def logged():
    return "Hello", 200

@test_bp.get("/publisher")
@role_required("publisher")
def publisher():
    return "Hello", 200