#!/usr/bin/python3
"""
Flask API that provides user data management.

This module defines a simple Flask API with the following endpoints:
- `/` (GET): Returns a welcome message.
- `/data` (GET): Returns a list of available usernames.
- `/status` (GET): Returns the API status.
- `/users/<username>` (GET): Retrieves details for a specific user.
- `/add_user` (POST): Adds a new user.

Usage:
Run this script to start the Flask API server.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane",
             "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John",
             "age": 30, "city": "New York"},
}


@app.route("/", strict_slashes=False)
def home():
    """
    Welcome message for the API root.

    Returns:
        str: A simple welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"], strict_slashes=False)
def data():
    """
    Retrieves a list of all usernames in the system.

    Returns:
        tuple: JSON list of usernames and HTTP status code 200.
    """
    return jsonify(list(users.keys())), 200


@app.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """
    Returns the status of the API.

    Returns:
        tuple: Status message and HTTP status code 200.
    """
    return "OK", 200


@app.route("/users/<username>", methods=["GET"], strict_slashes=False)
def user_details(username):
    """
    Retrieves details of a specific user.

    Args:
        username (str): The username to fetch details for.

    Returns:
        tuple: JSON user details with status 200 if found,
        or error message with status 404.
    """
    if username in users:
        return jsonify(users[username]), 200
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"], strict_slashes=False)
def add_user():
    """
    Adds a new user to the system.

    The request must contain a JSON body with a "username" key.

    Returns:
        tuple: JSON response with success message and HTTP status 201,
               or error message with HTTP status 400 if username is missing.
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON request"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
