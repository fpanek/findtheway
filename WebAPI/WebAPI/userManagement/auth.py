from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask import jsonify
from flask import make_response
import uuid
import json
from functools import wraps

auth = Blueprint('auth', __name__)

def isloggedin(f):
    @wraps(f)
    def wrapped_function(*args, **kwargs):
        #cookie is known ?
        cookie = request.cookies.get('id')
        print("cookie Value: ")
        print(cookie)
        user = User.query.filter_by(cookieID=cookie).first()
        if user:
             if user.cookieID==cookie:
                  print("cookie OK continue")
             else:
                  print("cookie not valid...")
        else:
             print("user cookie not known")
             userInformation = {'responseText': "User not authenticated.. - cookie id unknown"}
             response = make_response(json.dumps(userInformation))
             response.status_code = 400
             response.headers.add('Access-Control-Allow-Origin', 'https://findtheway.geokhugo.com:1234')
             response.headers.add('Access-Control-Allow-Credentials', 'true')
             return response
        return f(*args, **kwargs)
    return wrapped_function

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email)
        print(password)
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                #response = jsonify(success=True, id ="xyz")
                #response.status_code = 200
                #response.set_cookie("sdfasdf", "asdf")
                #return response
                #retiurn redirect("https://findtheway.geokhugo.com:804/mainpage.html")
                myuuid = str(uuid.uuid1() )
                response = make_response(redirect('https://findtheway.geokhugo.com:1234/mainpage.html'))
                response.set_cookie("id", myuuid)
                response.set_cookie("username", str(user.first_name))
                response.set_cookie("email", str(user.email))
                updateCookieID = User.query.filter_by(email=str(user.email)).update(dict(cookieID=myuuid))
                db.session.commit()
                return response
            else:
                response = jsonify(success=False, responseText="Password invalid",id ="xyz")
                response.status_code = 400
                return response
        else:
            #Email doesnt exist...
            response = jsonify(success=False, responseText="Email doesnt exist", id ="xyz")
            response.status_code = 400
            return response
    
    response = jsonify(success=True, id ="xyz")
    response.status_code = 200
    return response

    #LOGIN OK Response:
    #return redirect("https://findtheway.geokhugo.com:804/mainpage.html?")
    #LOGIN NOK Response
    

@auth.route('/logout')
@isloggedin
def logout():
    email = request.cookies.get('email')
    #print(email)
    user = User.query.filter_by(email=email).first()
    if user:
        print("loggin out user..")
        updateCookieID = User.query.filter_by(email=str(user.email)).update(dict(cookieID=''))
        db.session.commit()
    logout_user()
    response = make_response(redirect('https://findtheway.geokhugo.com:1234/index.html'))
    response.set_cookie("id", "")
    response.set_cookie("username", "")
    response.set_cookie("email", "")
    return response


@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        email = request.form.get('new_email')
        password = request.form.get('new_password')
        user = User.query.filter_by(email=email).first()
        if user:
            response = jsonify(success=True, responseText="Email already exists", id ="xyz")
            response.status_code = 400
            return response
        elif len(email) < 4:
            response = jsonify(success=True, responseText="Email must be longer than 4 characters", id ="xyz")
            response.status_code = 400
            return response
        elif len(first_name) < 2:
            response = jsonify(success=True, responseText="First name must be greater than 1 character", id ="xyz")
            response.status_code = 400
            return response
        elif len(last_name) < 2:
            response = jsonify(success=True, responseText="Last Name must be greater than 1 character", id ="xyz")
            response.status_code = 400
            return response
        elif len(password) < 7:
            response = jsonify(success=True, responseText="password must be longer than 7 characters", id ="xyz")
            response.status_code = 400
            response.set_cookie("sdfasdf", "asdf")
            return response
        else:
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            response = jsonify(success=True, responseText="User successfully created.", id ="xyz")
            response.status_code = 200
            response.set_cookie("sdfasdf", "asdf")
            return response

    response = jsonify(success=True, id ="xyz")
    response.status_code = 200
    return response


#Update User
@auth.route('/updateuserelement',  methods=['PUT', 'OPTIONS'])
@isloggedin
def updateuserelement():
    email_session = request.cookies.get('email')
    user = User.query.filter_by(email=email_session).first()        
    #response = make_response(redirect('https://findtheway.geokhugo.com:1234/mainpage.html'))
    #response = jsonify(responseText="Password invalid",id ="xyz")  
    #respone = make_response()
    responses = []
    first_name = request.form.get('firstName')
    if first_name:
        print("updating usere......")
        updateFirstName = User.query.filter_by(email=str(email_session)).update(dict(first_name=first_name))
        db.session.commit()
    last_name = request.form.get('lastName')
    if last_name:
        print("updating last_name......")
        updateLastName = User.query.filter_by(email=str(email_session)).update(dict(last_name=last_name))
        db.session.commit()
    email = request.form.get('new_email')
    if email:
        print("updating mail......")
        updatingMail = User.query.filter_by(email=str(email_session)).update(dict(email=email))
        db.session.commit()
    password = request.form.get('new_password')
    if password:
        print("updating password......")
        updatingPassword = User.query.filter_by(email=str(email_session)).update(dict(password=password))
        db.session.commit()
    response = jsonify(success=True, responseText="updated settings")
    response.set_cookie("username", str(first_name))
    response.set_cookie("email", str(email))
    response.headers.add('Access-Control-Allow-Origin', 'https://findtheway.geokhugo.com:1234')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', 'PUT')
    return response



#Delete User
@auth.route('/deleteUser',  methods=['DELETE'])
@isloggedin
def deleteUserFromDB():
    email_session = request.cookies.get('email')
    deleteUser = User.query.filter_by(email=email_session).delete()
    db.session.commit()
    response = jsonify(success=True, responseText="User successfully deleted.")
    response.set_cookie("id", "")
    response.status_code = 200
    return response

#Show User Informationr
@auth.route('/getuserinformation',  methods=['GET'])
@isloggedin
def gerUserInformation():
    email_session = request.cookies.get('email')
    print("email in getuserinfomraimon")
    print(email_session)
    user = User.query.filter_by(email=email_session).first()        
    if user:
        userInformation = {'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}
        response = make_response(json.dumps(userInformation)) 
        response.status_code = 200
        response.headers.add('Access-Control-Allow-Origin', 'https://findtheway.geokhugo.com:1234')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response
    else:
        userInformation = {'responseText': "no valid user information transmitted.."}
        response = make_response(json.dumps(userInformation)) 
        response.status_code = 400
        response.headers.add('Access-Control-Allow-Origin', 'https://findtheway.geokhugo.com:1234')
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        return response


