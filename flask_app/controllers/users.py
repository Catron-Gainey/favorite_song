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
    # validation for reg
    if not user.User.validate_register(request.form):
        return redirect("/")
    
    # check if user_email exists in db
    user_in_db = user.User.get_user_by_email(request.form["email"])
    # if so, flash message
    if user_in_db:
        flash("Account already exists! Please log in.", "account_confirmed")
        return redirect("/")
    
    print("Got Post Info")
    
    # hash pw
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    
    # save post info
    data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": pw_hash,
    }
    
    user_id = user.User.save(data)
    
    # store user_id into sessions
    session["user_id"] = user_id
    return redirect("/dashboard")


#! Login Post
@app.post("/user/login")
def login_post():
    # validation for login
    if not user.User.validate_login(request.form):
        return redirect("/")
    
    # fetch user_email 
    user_in_db = user.User.get_user_by_email(request.form["email"])
    # if not, flash message
    if not user_in_db:
        flash("The email and/or password you entered was incorrect. Please try again.", "error")
        return redirect("/")
    
    # save user_email in sessions
    session["email"] = request.form["email"]
    
    # pw check (if match with pw in db)
    pw_check = bcrypt.check_password_hash(user_in_db.password, request.form["password"])
    if not pw_check:
        flash("Unable to process verification. Please try again.", "error")
        return redirect("/")
    
    # store user into session
    user_id = user_in_db.id
    session["user_id"] = user_id
    return redirect("/dashboard")

############################################

### DESTROY SESSION ########################

#! clear session - temp button
@app.get("/clear_session_temp")
def destroy():
    if "user_id" not in session:
        return redirect("/")
    
    session.clear()
    print("----- Session cleared. -----")
    return redirect("/")

############################################

