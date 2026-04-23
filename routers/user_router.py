from controllers.user_controller import UserController
from flask import Blueprint


class UserRouter:
    def __init__(self, user_controller:UserController):
        self.user_controller = user_controller
        self.router = Blueprint('user',__name__)
        self.router.add_url_rule("/signup/",
                                 view_func=self.user_controller.signup,
                                 methods=['POST'],
                                 endpoint='signup')
        # self.router.add_url_rule("/signin/",
        #                         view_func=self.user_controller.signin,
        #                         methods=['POST'],
        #                         endpoint='signin')
