from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    create_access_token,
    jwt_required
)

from app.extensions import cache

import requests

external_api_bp = Blueprint(
    "external_api",
    __name__
)

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# ============================================
# LOGIN
# ============================================
@external_api_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    token = create_access_token(
        identity=data["username"]
    )

    return jsonify({
        "access_token": token
    })


# ============================================
# GET ALL POSTS
# ============================================
@external_api_bp.route("/posts", methods=["GET"])
@jwt_required()
@cache.cached(timeout=60)
def get_posts():

    response = requests.get(BASE_URL)

    return jsonify({
        "status": "success",
        "source": "third-party-api",
        "data": response.json()
    }), response.status_code


# ============================================
# GET SINGLE POST
# ============================================
@external_api_bp.route("/posts/<int:post_id>", methods=["GET"])
@jwt_required()
def get_single_post(post_id):

    response = requests.get(
        f"{BASE_URL}/{post_id}"
    )

    return jsonify({
        "status": "success",
        "data": response.json()
    }), response.status_code


# ============================================
# CREATE POST
# ============================================
@external_api_bp.route("/posts", methods=["POST"])
@jwt_required()
def create_post():

    payload = request.get_json()

    response = requests.post(
        BASE_URL,
        json=payload,
        headers={
            "Content-Type": "application/json"
        }
    )

    return jsonify({
        "status": "created",
        "third_party_response": response.json()
    }), response.status_code


# ============================================
# PUT UPDATE
# ============================================
@external_api_bp.route("/posts/<int:post_id>", methods=["PUT"])
@jwt_required()
def update_post(post_id):

    payload = request.get_json()

    response = requests.put(
        f"{BASE_URL}/{post_id}",
        json=payload,
        headers={
            "Content-Type": "application/json"
        }
    )

    return jsonify({
        "status": "updated",
        "data": response.json()
    }), response.status_code


# ============================================
# PATCH UPDATE
# ============================================
@external_api_bp.route("/posts/<int:post_id>", methods=["PATCH"])
@jwt_required()
def patch_post(post_id):

    payload = request.get_json()

    response = requests.patch(
        f"{BASE_URL}/{post_id}",
        json=payload,
        headers={
            "Content-Type": "application/json"
        }
    )

    return jsonify({
        "status": "patched",
        "data": response.json()
    }), response.status_code


# ============================================
# DELETE
# ============================================
@external_api_bp.route("/posts/<int:post_id>", methods=["DELETE"])
@jwt_required()
def delete_post(post_id):

    response = requests.delete(
        f"{BASE_URL}/{post_id}"
    )

    return jsonify({
        "status": "deleted",
        "message": f"Post {post_id} deleted"
    }), response.status_code