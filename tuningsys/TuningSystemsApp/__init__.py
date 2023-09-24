from flask import Flask
from flask_sqlalchemy import SQLAlchemy

data = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
    
    data.init_app(app)

    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app
