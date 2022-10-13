import os
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, request, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.secret_key = 'mgc1234'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        user = 'root',
        password = os.getenv('MY_SQL_PASSWORD'),
        server = 'localhost',
        database = 'my_game_collection'
    )

db = SQLAlchemy(app)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f'<Name {self.name}>' 

class Users(db.Model):
    username = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f'<Name {super.name}>' 


@app.route("/")
def index():
    games = Games.query.order_by(Games.id)
    return render_template("game_list.html", title='Games', games=games)


@app.route("/new")
def new():
    if 'user_active' not in session or session['user_active'] is None:
        return redirect(url_for('login', next=url_for('new')))
    return render_template("new.html", title="New Game")


@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    category = request.form["category"]
    console = request.form["console"]
    
    game = Games.query.filter_by(name=name).first()
    if game:
        flash('Jogo já existente')
        return redirect(url_for('index'))
    new_game = Games(name=name, category=category, console=console)
    db.session.add(new_game)
    db.session.commit()

    return redirect(url_for('index'))


@app.route("/login")
def login():
    next = request.args.get('next')
    return render_template("login.html", next=next)


@app.route("/auth", methods=["POST"])
def authenticate():
    user = Users.query.filter_by(username=request.form['user']).first()
    if user:
        if request.form["password"] == user.password:
            session['user_active'] = user.username
            flash(f'Welcome {user.username}. Successfully login!')
            next_page = request.form['next']
            if next_page != 'None':
                return redirect(next_page)
            return redirect(url_for('index'))
    flash(f'Failed to login')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['user_active'] = None
    flash('Successful logout!')
    return redirect(url_for('index'))

