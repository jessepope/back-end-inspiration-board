from app import db
from app.models.board import Board
from flask import Blueprint, request, make_response, jsonify
import requests
import os

boards_bp = Blueprint("boards", __name__, url_prefix="/boards")

@boards_bp.route("", methods=["GET"])
def handle_boards():
    pass