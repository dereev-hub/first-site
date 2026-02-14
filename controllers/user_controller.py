from flask import render_template, request
from services.user_service import UserService


class UserController:
    def __init__ (self, user_service: UserService):
        self.user_service = user_service

    def signup(self):
        if request.method == 'GET':
            return render_template("signup.html")