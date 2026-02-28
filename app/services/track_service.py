from ..models.track import Track
from ..models.album import Album
from ..models.artist import Artist


def get_all_tracks():
    return [{"id": t.id, "title": t.title, "artist": t.artist.name, "album": t.album.title, "cover": t.album.cover} for t in Track.select()]

def create_new_track(title: str, artist: str, album: str, cover: str, path: str):
    song_artist, new = Artist.get_or_create(
        name=artist,
        defaults={
            "picture": "/placeholder/picture.png",
            "followers": 0,
            "description": ""}
    )
    song_album, new = Album.get_or_create(
        title=album,
        artist=song_artist,
        defaults={"cover": "/placeholder/cover.png"}
    )

    Track.create(
        title=title,
        artist=song_artist,
        album=song_album,
        cover=cover,
        audio_url=path
    )

def get_track_location_from_id(track_id):
    return Track.select().where(Track.id == track_id).get()