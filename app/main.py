from flask import Blueprint
from . import db

blueprint = Blueprint('main', __name__)

@blueprint.route('/')
def index():
    return 'Hello World'

@blueprint.route('/feed')
def feed():
    return 'Profile'

@blueprint.route('/perfil')
def profile():
    return 'Profile'