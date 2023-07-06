import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as hash
from ..configs.db import Base


class User(Base):
    __tablename__ = "users"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String(200), unique=True, index=True)
    hashed_password = _sql.Column(_sql.String(200))
    is_active = _sql.Column(_sql.Boolean, default=True)
    is_partner = _sql.Column(_sql.Boolean, default=False)
    is_admin = _sql.Column(_sql.Boolean, default=False)

    #reunioes = _orm.relationship("Business", back_populates="user")

    def verify_password(self, password: str):
        return hash.bcrypt.verify(password, self.hashed_password)