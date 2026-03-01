from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from peewee import IntegrityError

from ..models.user import User
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def register():
    data = request.json
    hashed = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt()).decode()
    try:
        user = User.create(
            username=data["username"],
            email=data["email"],
            password=hashed,
            role="listener"
        )
    except IntegrityError:
        return jsonify({"error": "User already exists"}), 409

    return jsonify({"message": "User created"}), 201

@auth_bp.post("/login")
def login():
    data = request.json
    user = User.get_or_none(User.email == data["email"])

    if not user or not bcrypt.checkpw(data["password"].encode(), user.password.encode()):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=str(user.id),
        additional_claims={"role": user.role}
    )
    return jsonify({
        "access_token": create_access_token(identity=str(user.id)),
        "refresh_token": create_refresh_token(identity=str(user.id))
    })

# TODO: HAS TO BE DELETED, ONLY FOR TESTING PURPOSES
@auth_bp.post("/promote")
@jwt_required()
def promote():
    user_id = get_jwt_identity()
    user = User.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Invalid token"}), 401
    # set as publisher role
    user.role = "publisher"
    user.save()
    return jsonify({"success": True}), 201

@auth_bp.post("/refresh")
@jwt_required(refresh=True)
def refresh():
    user_id = get_jwt_identity()
    new_token = create_access_token(identity=user_id)
    return jsonify({"access_token": new_token})

@auth_bp.get("/get_infos")
@jwt_required()
def get_infos():
    user_id = get_jwt_identity()
    user = User.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Invalid token"})
    return jsonify({
        "username": user.username,
        "email": user.email,
        "role": user.role
    })