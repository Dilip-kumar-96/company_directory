from flask import Blueprint

# Create a Blueprint instance
main = Blueprint('main', __name__)

# Import routes to attach them to the Blueprint
from src.company_directory.route import route