import imp
from sqlalchemy import Table, Column
from sqlalchemy import String, Integer, DateTime, Boolean, ForeignKey
from config.db import metadata, engine

users = Table("users", metadata,
              Column("id", Integer, primary_key=True),
              Column("name", String(255)),
              Column("email", String(255)),
              Column("password", String(255)
                     ))

metadata.create_all(engine)
