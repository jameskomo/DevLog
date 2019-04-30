from flask import Flask
from flask import g, request
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_babel import Babel

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()
photos = UploadSet('photos',IMAGES)
mail = Mail()
babel = Babel()
global translate

def create_app(config_name):
    app = Flask(__name__)
    moment = Moment(app)
    babel = Babel(app)
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

   
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .request import configure_request
    configure_request(app)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    # configure UploadSet
    configure_uploads(app,photos)

    return app

@babel.localeselector
def get_locale():
    translations = [str(translation) for translation in babel.list_translations()]
    return request.accept_languages.best_match(translations)
  

