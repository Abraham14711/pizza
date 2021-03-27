from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///db.sqlite'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    tel=db.Column(db.String(11),nullable=False)
    food=db.Column(db.String,nullable=False)
    adress=db.Column(db.String(600),nullable=False)

@app.route('/')
def main_page():
    return render_template('main page.html')

@app.route('/отправить', methods=['POST'])
def send():
    name=request.form['name']
    tel=request.form['tel']
    food=request.form['food']
    adress=request.form['adress']
    db.session.add(User(name,tel,food,adress))
    return redirect(url_for('main page.html'))


@app.route('/contacts')
def contacts():
    return render_template('Contacts.html')

@app.route('/new')
def new_things():
    return render_template('New things.html')


@app.route('/new1')
def new1():
    return render_template('new 1.html')

@app.route('/new2')
def new2():
    return render_template('new 2.html')


if __name__ == '__main__':
    app.run()

