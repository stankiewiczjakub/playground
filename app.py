from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder

def create_app():
    app = Flask(__name__)

    db = SQLAlchemy()
    db.init_app(app)

    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    return app
