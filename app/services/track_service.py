from ..models.track import Track

def get_all_tracks():
    return [{"id": t.id, "title": t.title, "artist": t.artist.name, "album": t.album.title} for t in Track.select()]