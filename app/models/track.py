from peewee import CharField, IntegerField, ForeignKeyField
from .base import BaseModel
from .artist import Artist
from .album import Album

class Track(BaseModel):
    title = CharField()
    duration = IntegerField()
    album = ForeignKeyField(Album, backref="tracks")
    artist = ForeignKeyField(Artist, backref="tracks")
    audio_url = CharField()