from flask import Flask, g, render_template, session
from requests import Session
from models.base import SessionLocal
from repositories import *
from controllers import *
from routers import *
from services import *
from models import *
from dotenv import load_dotenv
from flask_cors import CORS
import os


load_dotenv(override=True)
app = Flask(__name__)
CORS(app)
app.static_folder = 'static'
app.secret_key = os.getenv('SECRET')


@app.before_request
def before_request_db():
    g.db = SessionLocal()


@app.teardown_appcontext
def teardown_request_db(exception=None):
    db: Session = g.pop('db', None)
    if db is not None:
        db.close()


Base.metadata.create_all(bind = engine)


user_repository = UserRepository()
user_service = UserService(user_repository)
user_controller = UserController(user_service)
user_router = UserRouter(user_controller)
app.register_blueprint(user_router.router, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=True)