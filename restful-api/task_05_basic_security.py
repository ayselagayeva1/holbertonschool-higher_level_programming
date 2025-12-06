#!/usr/bin/python3
"""
API Security and Authentication with Flask
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

# Users in memory
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# ---------------- BASIC AUTH ---------------- #

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ---------------- JWT AUTH ---------------- #

@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 401

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity={
        "username": username,
        "role": users[username]["role"]
    })

    return jsonify(access_token=token)


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    user = get_jwt_identity()

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# ---------------- ERROR HANDLERS ---------------- #

@jwt.unauthorized_loader
def missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
