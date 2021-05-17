from sms2fa.config import config_env_files
from sms2fa.models import db, User
from flask import Flask

from flask_login import LoginManager
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
Bootstrap(app)
login_manager = LoginManager()
sess = Session()
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["50 per day", "10 per hour"]
)


def prepare_app(environment='development', p_db=db):
    app.config.from_object(config_env_files[environment])
    login_manager.setup_app(app)
    p_db.init_app(app)
    sess.init_app(app)
    app.session_interface.db.create_all()
    from . import views
    return app


def save_and_commit(item):
    db.session.add(item)
    db.session.commit()
db.save = save_and_commit


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)
