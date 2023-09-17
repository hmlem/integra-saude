from flask import Blueprint
from . import db

blueprint = Blueprint('webhook', __name__)

@blueprint.route('/google-sheet')
def index():
    return 'Index'