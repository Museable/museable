from flask import Flask
from flask_jwt_extended import JWTManager

from dotenv import dotenv_values

from .models import db
from .models.track import Track
from .models.album import Album
from .models.artist import Artist
from .models.user import User


config = dotenv_values(".env")

def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = config["JWT_SECRET_KEY"]

    JWTManager(app)

    @app.before_request
    def connect_db():
        db.connect(reuse_if_open=True)

    @app.teardown_request
    def close_db(exc):
        if not db.is_closed():
            db.close()

    db.create_tables([Track, Album, Artist, User], safe=True)

    from .routes.tracks import tracks_bp
    from .routes.auth import auth_bp
    from .routes.test import test_bp
    app.register_blueprint(tracks_bp, url_prefix="/api/tracks")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(test_bp, url_prefix="/api/test")

    return app