from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    project_root = os.path.dirname(base_dir)
    
    app = Flask(__name__, 
                template_folder=os.path.join(project_root, 'templates'),
                static_folder=os.path.join(project_root, 'static'))
    
    app.config['SECRET_KEY'] = 'fsdalwlkqrlkwqrlkwq'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    login_manager.init_app(app)

    from .models import User  # Ensure User model is imported

    from .app import main_blueprint, init_oauth
    from .admin import admin_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint)
    
    # Initialize OAuth
    init_oauth(app)

    with app.app_context():
        db.create_all()

    return app