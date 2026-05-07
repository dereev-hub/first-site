import os
from typing import Callable

from flask import jsonify, request
from jwt import DecodeError, InvalidSignatureError, decode


def extract_token_from_header(bearer_token):
    """Вспомогательная функция для безопасного извлечения токена из заголовка"""
    if not bearer_token:
        return None, "Unauthorized"

    parts = bearer_token.split()
    if len(parts) != 2:
        return None, "Неверный формат токена. Ожидается: Bearer <token>"

    if parts[0].lower() != 'bearer':
        return None, "Тип токена должен быть Bearer"

    return parts[1], None
 
 
def authorized(f: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        headers = request.headers
        bearer_token = headers.get("Authorization")
        if not bearer_token:
            return jsonify({"message": "Unauthorized"}), 401
        try:
            token, error = extract_token_from_header(bearer_token)
            if error:
                return jsonify({"message": error}), 419
            user_id = int(decode(token, os.getenv("SECRET"), algorithms=["HS256"]).get("user_id"))
            return f(*args, **kwargs, user_id=user_id)
        except InvalidSignatureError as e:
            return jsonify({"message": "Invalid token"}), 419
        except DecodeError as e:
            print('Ошибка расшифровки токена', e)
            return jsonify({"message": "Ошибка расшифровки токена - Not enough segments"}), 419

    return wrapper
