from peewee import CharField, IntegerField
from .base import BaseModel

class Artist(BaseModel):
    name = CharField()
    picture = CharField()
    followers = IntegerField()
    description = CharField()