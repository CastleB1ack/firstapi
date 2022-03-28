from sqlalchemy import text, Boolean, Column, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from d import b


class pp(b):
    __tablename__ = "ppp"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    users = Column(String,nullable=False)
    posts = Column(String,nullable=False)
    bub   = Column(Boolean,  server_default='True')
    em = Column(String, ForeignKey("users.email", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")


class vot(b):
    __tablename__ = "vo"
    ui = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'),primary_key=True, nullable=False)
    pi = Column(Integer, ForeignKey('ppp.id', ondelete='CASCADE'),primary_key=True, nullable=False)


class User(b):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String,nullable=False, unique=True)
    pas = Column(String,nullable=False)
    re = Column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))



