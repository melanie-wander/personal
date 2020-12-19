from flask import Flask, render_template, url_for,  request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

#Table for Storing Master Logins to PMS
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(2000), nullable = False)
    password = db.Column(db.String(2000), nullable = False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    def __repr__(self):
        return '<user %r>' % self.user_id

#Table Storing App login crediential Forgein Key on User Table
class appUser(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(1000), nullable = False)
    password = db.Column(db.String(1000), nullable = False)
    appname = db.Column(db.String(1000))
    masterid =  db.Column(db.Integer,nullable =False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr2__(self):
        return '<app %r>' % self.id


@app.route('/', methods=['POST','GET'])
def main(): 
    #Maybe add Authentication here ?
    return render_template('main.html')

@app.route('/register/', methods=['POST','GET'])
def register():
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        new_user = User(username=username,password=password)

        try: 
            db.session.add(new_user) #adds the new user information to database
            db.session.commit()
            return redirect('/login/')
        except:
            return  'Failed to register'
            #'There was an issue registering'

    else:
        return render_template('register.html')

@app.route('/login/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_to_login = appUser.query.get_or_404(username)
        return redirect('/apps/',user_id = 4)
        #if password == user_to_login.password: 
         #   user_id = user_to_login.user_id
          #  return redirect('/apps/')
        #else: 
         #   return redirect('/login/')
    else: 
        users = User.query.all()
        return render_template('login.html', users = users)

@app.route('/apps/', methods=['POST','GET'])
def pmsindex(user_id):
    if request.method == 'POST': 
        appname = request.form['appname']
        username = request.form['username']
        password = request.form['password']
        new_app = appUser(username=username,password=password,appname=appname, masterid = user_id)

        try: 
            db.session.add(new_app) #adds the new user information to database
            db.session.commit()
            return redirect('/')
        except:
            return  'App was not able to be added'
            #'There was an issue in adding the new application'

    else:
        apps = appUser.query.all() #grabs all apps in the database  per user
        return render_template('index.html', apps = apps)


@app.route('/delete/<int:id>')
def delete(id):
    app_to_delete = appUser.query.get_or_404(id)

    try: 
        db.session.delete(app_to_delete) #deletes app from database
        db.session.commit()
        return redirect('/')
    except:
        return 'The application does not appear to be present in database'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    app = appUser.query.get_or_404(id)

    if request.method == 'POST':
        app.username = request.form['username']
        app.password = request.form['password']

        try: 
            db.session.commit() # updates app in database
            return redirect('/')
        except: 
            return 'There was an error while updating'
    else:
        return render_template('update.html', task = app)


if __name__ == "__main__":
    app.run(debug=True)