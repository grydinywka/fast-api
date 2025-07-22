import os
from sqlalchemy import create_engine, MetaData
from databases import Database


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "pet01")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")

DATABASE_URL = f"mysql+pymysql://root:database_pass@{DB_HOST}:{DB_PORT}/pet01"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)
