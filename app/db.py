from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "mysql+pymysql://root:database_pass@localhost:3307/pet01"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)
