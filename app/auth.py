import flask
from flask import Blueprint, redirect, g, request
from flask_login import LoginManager, login_required, logout_user, login_user
from app.models import User

blueprint = Blueprint('auth', __name__)

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    user = User.get(user_id)
    g.user = user
    return user


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    flask.flash(request.method)
    # form = LoginForm()
    # if form.validate_on_submit():
    #     # Login and validate the user.
    #     # user should be an instance of your `User` class
    #     login_user(user, remember=True)

    #     flask.flash('Logged in successfully.')

    #     next = flask.request.args.get('next')
    #     # url_has_allowed_host_and_scheme should check if the url is safe
    #     # for redirects, meaning it matches the request host.
    #     # See Django's url_has_allowed_host_and_scheme for an example.
    #     if not url_has_allowed_host_and_scheme(next, request.host):
    #         return flask.abort(400)

    #     return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html')


@blueprint.route('/cadastro')
@login_required
def signup():
    return 'Signup'


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
