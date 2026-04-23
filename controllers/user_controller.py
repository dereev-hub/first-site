from flask import jsonify, render_template, request, session, redirect
from services.user_service import UserService


class UserController:
    def __init__ (self, user_service: UserService):
        self.user_service = user_service

    # def signup(self):
    #     if request.method == 'GET':
    #         return render_template("signup.html")
    #     elif request.method == 'POST':
    #         try:
    #             email = request.form.get('email')
    #             password = request.form.get('password')
    #             self.user_service.signup(email, password)
    #         except Exception as e:
    #             return render_template("signup.html", error= str(e))
    #         return render_template("signup.html")
    
    # def signin(self):  # ← НОВЫЙ МЕТОД
    #     if request.method == 'GET':
    #         return render_template("signin.html")
    #     elif request.method == 'POST':
    #         try:
    #             email = request.form.get('email')
    #             password = request.form.get('password')
    #             user = self.user_service.signin(email, password)
    #             session.update({'user_id': user.id, 'user_email': user.email})
    #             return redirect('../../')
    #         except Exception as e:
    #             return render_template("signin.html", error=str(e))
    def signup(self):
        try:
            if request.is_json:
                body = request.get_json()
                self.user_service.signup(**body)
                return jsonify({'message': 'пользователь успешно зарегистрирован'}),201
            return jsonify({'error': "требуется json"}),403
        except Exception as e:
            return jsonify({'error': str(e)}),409