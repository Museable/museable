from peewee import CharField, IntegerField, ForeignKeyField
from uuid import uuid4

from .base import BaseModel
from .artist import Artist
from .album import Album

class Track(BaseModel):
    id = CharField(default=uuid4(), primary_key=True)
    title = CharField()
    album = ForeignKeyField(Album, backref="tracks")
    artist = ForeignKeyField(Artist, backref="tracks")
    audio_url = CharField()