from uuid import uuid4
from app import create_app
from app.models.artist import Artist
from app.models.album import Album
from app.models.track import Track

app = create_app()

def create_unique_artist():
    return Artist.create(
        name=f"{uuid4()}",
        picture="/picture.png",
        followers=125,
        description="Aaaaa"
    )

def create_unique_album(artist_entry):
    return Album.create(
        title=f"{uuid4()}",
        cover="/cover.png",
        artist=artist_entry
    )

def create_unique_track(artist_entry, album_entry):  # fixed order
    Track.create(
        title=f"{uuid4()}",
        audio_url="/audio.mp3",
        duration=125,
        album=album_entry,
        artist=artist_entry,
    )

for i in range(5):
    artist = create_unique_artist()
    for j in range(5):
        album = create_unique_album(artist)
        for k in range(5):
            create_unique_track(artist, album)