from flask import Flask
from .models import db
from .models.track import Track
from .models.album import Album
from .models.artist import Artist


def create_app(config="app.config.Dev"):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.before_request
    def connect_db():
        db.connect(reuse_if_open=True)

    @app.teardown_request
    def close_db(exc):
        if not db.is_closed():
            db.close()

    db.create_tables([Track, Album, Artist], safe=True)

    from .routes.tracks import tracks_bp
    app.register_blueprint(tracks_bp, url_prefix="/api/tracks")

    return app