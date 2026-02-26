from peewee import CharField, ForeignKeyField
from .base import BaseModel
from .artist import Artist

class Album(BaseModel):
    title = CharField()
    cover = CharField()
    artist = ForeignKeyField(Artist, backref="albums")