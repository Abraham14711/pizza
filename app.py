from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('pizza.html')

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
