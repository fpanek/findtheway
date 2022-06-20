from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from flask import jsonify
from flask import make_response
import uuid

auth = Blueprint('auth', __name__)


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
                response = make_response(redirect('https://findtheway.geokhugo.com:804/mainpage.html'))
                response.set_cookie("id", myuuid)
                response.set_cookie("username", str(user.first_name))

                return response
            else:
                response = jsonify(success=False, responseText="Password invalid",id ="xyz")
                response.status_code = 400
                response.set_cookie("sdfasdf", "asdf")
                return response
        else:
            #Email doesnt exist...
            response = jsonify(success=False, responseText="Email doesnt exist", id ="xyz")
            response.status_code = 400
            response.set_cookie("sdfasdf", "asdf")
            return response
    
    response = jsonify(success=True, id ="xyz")
    response.status_code = 200
    response.set_cookie("sdfasdf", "asdf")
    return response

    #LOGIN OK Response:
    #return redirect("https://findtheway.geokhugo.com:804/mainpage.html?")
    #LOGIN NOK Response
    

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))


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
            response.set_cookie("sdfasdf", "asdf")
            return response
        elif len(email) < 4:
            response = jsonify(success=True, responseText="Email must be longer than 4 characters", id ="xyz")
            response.status_code = 400
            response.set_cookie("sdfasdf", "asdf")
            return response
        elif len(first_name) < 2:
            response = jsonify(success=True, responseText="First name must be greater than 1 character", id ="xyz")
            response.status_code = 400
            response.set_cookie("sdfasdf", "asdf")
            return response
        elif len(last_name) < 2:
            response = jsonify(success=True, responseText="Last Name must be greater than 1 character", id ="xyz")
            response.status_code = 400
            response.set_cookie("sdfasdf", "asdf")
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
    response.set_cookie("sdfasdf", "asdf")
    return response
