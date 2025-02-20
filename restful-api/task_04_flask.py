#!/usr/bin/env python3
"""
Flask API that provides user data management.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """
    Welcome message for the API root.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Retrieves a list of all usernames in the system.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Returns the status of the API..
    """
    return "OK"


@app.route("/users/<username>")
def user_details(username):
    """
    Retrieves details of a specific user.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the system..
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username or username not in data:
        return jsonify({"error": "Username is required"}), 400


    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
