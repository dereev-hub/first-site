from flask import Flask, render_template
from repositories import *
from controllers import *
from routers import *
from services import *
from models import *

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():
    return render_template('index.html')

with get_db() as db:
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user_controller = UserController(user_service)
    user_router = UserRouter(user_controller)
    app.register_blueprint(user_router.router, url_prefix='/users')


    app.run()