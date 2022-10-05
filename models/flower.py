import sqlalchemy

from main import db

metadata = sqlalchemy.MetaData()


class Flower(db.Model):
    __tablename__ = "flowers"

    db.Column("id", db.Integer, primary_key=True),
    db.Column("name", db.String(100), unique=True, nullable=False),
    db.Column("description", db.String(), nullable=False),
    db.Column("price", db.Integer, nullable=False)