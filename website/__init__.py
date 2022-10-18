from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database_dev.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views,url_prefix = '/')
    app.register_blueprint(auth,url_prefix = '/')
    
    from .models import User,Note
    
    create_database(app)
    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("db created successfully") 