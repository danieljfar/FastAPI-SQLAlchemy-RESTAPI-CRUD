from venv import create
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:siclo2112@localhost:3306/storedb")
metadata = MetaData()

conn = engine.connect()