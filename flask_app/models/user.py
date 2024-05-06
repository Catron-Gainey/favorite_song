from flask import request, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import song
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class User:
    DB = "favorite_song"
    
    #! Constructor
    def __init__(self, db_data):
        self.id = db_data["id"]
        self.name = db_data["name"]
        self.email = db_data["email"]
        self.password = db_data["password"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]

    #! Create
    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO users (name, email, password)
            VALUES (%(name)s, %(email)s, %(password)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    #! Read
    #!! Get user by email
    @classmethod
    def get_user_by_email(cls, email):
        query = """
            SELECT *
            FROM users
            WHERE email = %(email)s;
        """
        data = {
            "email": email
        }
        user_data = connectToMySQL(cls.DB).query_db(query, data)
        if len(user_data) < 1:
            return False
        return cls(user_data[0])

    #! Update

    #! Delete        

    #! Validations
    @staticmethod
    def validate_register(user):
        is_valid = True;
        
        # all fields
        if len(user["name"].strip()) == 0 and len(user["email"].strip()) == 0 and len(user["password"].strip()) == 0:
            flash("All fields are required.", "reg_invalid")
            is_valid = False
            return is_valid
        
        # name field
        if len(user["name"].strip()) < 2:
            flash("Name must be at least 2 characters long.", "reg_name")
            is_valid = False
        elif len(user["name"].strip()) == 0:
            flash("Name cannot be left blank.", "reg_name")
            is_valid = False
            
        # email field
        if not EMAIL_REGEX.match(user["email"]):
            flash("Please provide a valid email.", "reg_email")
            is_valid = False
        elif len(user["email"].strip()) == 0:
            flash("Email cannot be left blank.", "reg_email")
            is_valid = False
            
        # password field
        if len(user["password"].strip()) < 6:
            flash("Password must be at least 6 characters long.", "reg_pw")
            is_valid = False
        elif len(user["password"].strip()) == 0:
            flash("Password cannot be left blank.", "reg_pw")
            is_valid = False
            
        # confirm_pw field
        if len(user["confirm_pw"]) == 0:
            flash("Please re-type password to confirm.", "reg_confirm_pw")
            is_valid = False
        elif user["confirm_pw"] != user["password"]:
            flash("Password does not match.", "reg_pw")
        
        return is_valid
    
    @staticmethod
    def validate_login(user):
        is_valid = True
        
        # all fields required.
        if len(user["email"].strip()) == 0 and len(user["password"]) == 0:
            flash("All fields required.", "login_invalid")
            is_valid = False
            return is_valid
        
        # email field
        if not EMAIL_REGEX.match(user["email"]):
            flash("Please provide a valid email.", "login_email")
            is_valid = False
        elif len(user["email"].strip()) == 0:
            flash("Email field is required.", "login_email")
            is_valid = False
        
        # password field
        if len(user["password"].strip()) == 0:
            flash("Password field is required.", "login_pass")
            is_valid = False
        
        return is_valid