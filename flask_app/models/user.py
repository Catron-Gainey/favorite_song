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
            INSERT INTO users (name, email, password, created_at, updated_at)
            VALUES (%(name)s, %(email)s, %(password)s, NOW(), NOW());
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    #! Read

    #! Update

    #! Delete

    #! Validations