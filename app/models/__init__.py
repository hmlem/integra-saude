import enum
import bcrypt

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship, DeclarativeBase

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class Base(DeclarativeBase):
    pass


class User(BaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    enc_password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone = db.Column(db.DateTime(timezone=True), nullable=False)

    @property
    def password(self):
        raise AttributeError('Senha não é um atributo capaz de ser lido')

    @password.setter
    def password(self, password):
        self.enc_password = bcrypt.hashpw(password, bcrypt.gensalt()).decode()


class Role(BaseModel):
    # ti, gestao, hmlem-admin, hmlem, ab-medico, superadmin
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    tag = db.Column(db.String, nullable=False)


user_role = Table(
    "_user_role",
    Base.metadata,
    db.Column("user_id", ForeignKey("users.id")),
    db.Column("role_id", ForeignKey("roles.id")),
)


class Capability(BaseModel):
    __tablename__ = 'capabilities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


user_capabilities = Table(
    "_user_capabilities",
    Base.metadata,
    db.Column("user_id", ForeignKey("users.id")),
    db.Column("capability_id", ForeignKey("capabilities.id")),
)


class ReportType(enum.Enum):
    INTERNAL = "Internal"
    EXTERNAL = "External"


class Report(BaseModel):
    __tablename__ = 'records'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Enum(ReportType), nullable=False)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)

    created_by_id = db.Column(db.Integer, ForeignKey("users.id"))
    created_by = relationship("User")

    closed_by_id = db.Column(db.Integer, ForeignKey("users.id"))
    closed_by = relationship("User")


class Comment(BaseModel):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)

    created_by_id = db.Column(db.Integer, ForeignKey("users.id"))
    created_by = relationship("User")
