import click
from flask import Blueprint
from app.models import User, Role, Capability, db

extended_cli_bp = Blueprint('cli', __name__)


@extended_cli_bp.cli.command('initial-seed')
def initial_seed():
    # creating roles
    roles = [
        Role(name="Administrador Root", tag="root"),
        Role(name="Administrador Geral", tag="admin"),
        Role(name="HMLEM - Administrativo", tag="hmlem-admin"),
        Role(name="HMLEM - Colaborador", tag="hmlem"),
        Role(name="Atenção Básica - Médico", tag="ab-medico"),
        Role(name="Atenção Básica - Recepção", tag="ab-recepcao"),
        Role(name="Atenção Básica - Enfermagem", tag="ab-enfermagem"),
        Role(name="Atenção Básica - Administrativo", tag="ab-admin"),
        Role(name="Gestão Política", tag="gestao"),
    ]
    db.session.bulk_save_objects(roles)
    # creating capabilities
    capabilities = [
        Capability(name="can_comment"),
        Capability(name="can_close_report"),
        Capability(name="can_open_report"),
        Capability(name="can_create_user"),
        Capability(name="can_edit_user"),
        Capability(name="can_create_role"),
        Capability(name="can_edit_role"),
    ]
    db.session.bulk_save_objects(capabilities)


@extended_cli_bp.cli.command('create-user-test')
def create_user_test(role):
    print(role)


@extended_cli_bp.cli.command('create-user')
@click.argument('name')
@click.argument('email')
@click.argument('role')
def create_user(name, email, role):
    user = User(name=name, email=email)
    user.password = "passw@rd"
    user.role.add(db.session.query(Role).filter(
        Role.tag == role).one_or_none())
    db.session.add(user)
    db.session.commit()
