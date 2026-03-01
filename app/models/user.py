from peewee import CharField
from .base import BaseModel

class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    role = CharField(default="listener") # "listener" or "publisher" or "admin"