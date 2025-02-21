#!/usr/bin/python3
"""
Flask API with Basic and JWT Authentication.

This module provides an API with user authentication using both
Basic Authentication and JSON Web Tokens (JWT). The following
endpoints are available:

- `/basic-protected`: Basic Auth protected route.
- `/login`: Authenticates users and returns a JWT.
- `/jwt-protected`: JWT protected route.
- `/admin-only`: Admin-only JWT protected route.

Custom error handlers for JWT-related errors are also implemented.
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
    get_jwt,
)

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify the username and password.

    Args:
        username (str): The username to verify.
        password (str): The password to verify.

    Returns:
        str or None: The username if verification is successful, else None.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Basic Auth protected route.

    Returns:
        JSON response indicating access is granted.
    """
    return ("Basic Auth: Access Granted")


@app.route("/login", methods=["POST"])
def login():
    """
    User login endpoint.

    Expects a JSON payload with 'username' and 'password'.

    Returns:
        JSON response with access token if successful,
        or error message if authentication fails.
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify(), 401

    access_token = create_access_token(
        identity=username, additional_claims={"role": user["role"]}
    )
    return jsonify(access_token=access_token), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    JWT protected route.

    Returns:
        JSON response indicating access is granted,
        along with the current user's identity.
    """
    current_user = get_jwt_identity()
    return jsonify({"message": "JWT Auth:\
                     Access Granted", "user": current_user})


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only JWT protected route.

    Returns:
        JSON response indicating access
          is granted if the user has an admin role,
        or an error message if access is denied.
    """
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def unauthorized_response(error):
    return jsonify({"error": str(error)}), 401



@jwt.invalid_token_loader
def invalid_token_response():
    """
    Custom response for invalid tokens.

    Returns:
        JSON response indicating the error.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_response():
    """
    Custom response for expired tokens.

    Returns:
        JSON response indicating the error.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401
    

if __name__ == "__main__":
    app.run()
