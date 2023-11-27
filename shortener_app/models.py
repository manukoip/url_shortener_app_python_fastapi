# shortener_app/models.py
# Describes how data should be stored in database

from sqlalchemy import Boolean, Integer, Column, String

from .database import Base

# Class name is singular and table name is plural of class name


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)
