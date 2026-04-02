from flask import Flask, render_template, session
from repositories import *
from controllers import *
from routers import *
from services import *
from models import *
from dotenv import load_dotenv
import os


load_dotenv(override=True)
app = Flask(__name__)
app.static_folder = 'static'
app.secret_key = os.getenv('SECRET')

@app.route("/")
def index():
    # TODO: переделать главную ,добавить поиск и любимые треки
    user_email = session.get('user_email','аноним')
    return render_template('index.html',user_email = user_email)


Base.metadata.create_all(bind = engine)

with get_db() as db:
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user_controller = UserController(user_service)
    user_router = UserRouter(user_controller)
    app.register_blueprint(user_router.router, url_prefix='/users')


if __name__ == '__main__':
    app.run(debug=True)