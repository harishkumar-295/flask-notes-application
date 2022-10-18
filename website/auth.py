from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db

auth = Blueprint('auth',__name__)

@auth.route('/login',methods=['POST','GET'])
def login():
    data = request.form
    print(data)
    return render_template('login.html',text = "Testing login...",boolean = False)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # condition checks
        if len(email) < 4:
            flash('Invalid email address, email must have greater than 4 characters',category='error')
        elif len(first_name) < 4:
            flash('Invalid first name, first name must have greater than 4 characters',category='error')
        elif len(password1) != len(password2):
            flash('Invalid password, password does not match',category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # add user to the database
            new_user = User(email=email,first_name = first_name , password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully..',category='success')
            return redirect(url_for('views.home'))
    
    return render_template('sign_up.html')