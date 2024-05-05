from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import user, song
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


#! Index page route
@app.get("/")
def index():
    return redirect("/index")


### GET ROUTES #############################

#! Login Reg Page
@app.get("/index")
def login_reg_page():
    return render_template("/login_reg.html")


#! Dashboard Page
@app.get("/dashboard")
def dash_page():
    if "user_id" not in session:
        return redirect("/")  # back to index route
    
    return render_template("/dashboard.html")

############################################


### POST ROUTES ##################

#! Registration Post
@app.post("/user/register")
def reg_post():
    return redirect("/dashboard")


#! Login Post
@app.post("/user/login")
def login_post():
    return redirect("/dashboard")

############################################
