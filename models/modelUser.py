from flask import flash
from models.user import User
from mysql_service import db,get_user
from icecream import ic

class ModelUser():
    @classmethod
    def login(self,user):
        try:
            user_data = get_user(user.username)
            ic(user_data)
            if user_data:
                if User.check_password(user_data.password, user.password):
                    return True
                else:
                    flash('Incorrect password')
                    return False
            else:
                flash('User not found')
                return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
                