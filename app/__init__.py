from flask import Flask
from app.config import Config
from app.extensions import db, migrate, jwt, cache
from app.routes.external_api_routes import external_api_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cache.init_app(app)

    app.register_blueprint(
        external_api_bp,
        url_prefix="/api/external"
    )

    return app