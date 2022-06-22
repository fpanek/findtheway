#!/usr/local/bin/python3.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_cors import CORS
from  WienerLinienAPI.getNearbyStations import *
from  WienerLinienAPI.filterStations import *

db = SQLAlchemy()
DB_NAME = "database.db"

stationsFile = "stations.json"
stationsStopIDFile = "stations_stopID.csv"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    CORS(app)
    saveNearbyStationsStopIDIntoFile(stationsStopIDFile)
    from .views import views
    from .auth import auth
    from  WienerLinienAPI.stations import stations

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(stations, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

