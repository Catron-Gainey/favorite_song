from flask import request, flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user



class User:
    DB = "favorite_song"
    
    #! Constructor
    def __init__(self, db_data):
        self.id = db_data["id"]
        self.title = db_data["title"]
        self.artist = db_data["artist"]
        self.created_at = db_data["created_at"]
        self.updated_at = db_data["updated_at"]
        
    #! Create

    #! Read

    #! Update

    #! Delete

    #! Validations