from flask import Blueprint,render_template,request

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
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # condition checks
        if len(email) < 4:
            pass
        elif len(firstName) < 4:
            pass
        elif len(password1) != len(password2):
            pass
        else:
            # add user to the database
            print("add user to the database")
    
    return render_template('sign_up.html')