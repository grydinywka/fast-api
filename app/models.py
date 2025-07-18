# models.py
from sqlalchemy import Table, Column, Integer, String
from app.db import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("email", String(100)),
)
