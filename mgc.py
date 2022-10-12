from flask import Flask, render_template, redirect, request, session, flash, url_for


class Game:
    def __init__(self, name, category, console) -> None:
        self.name = name
        self.category = category
        self.console = console

title = "Games"
game_one = Game("Tetris", "Puzzle", "Atari")
game_two = Game("God of War", "Hack n Slash", "PS2")
game_three = Game("Mortal Kombat", "Luta", "SNES")
games = [game_one, game_two, game_three]

class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
    
    def __repr__(self) -> str:
        return f'User(name={self.name}, username={self.username})'
        

user1 = User('Rodrigo', 'RFM', '1234')
user2 = User('Marta', 'Maregs', '4321')
user3 = User('Fulano', 'Cicrano', '1144')
users = {
    user1.username: user1,
    user2.username: user2,
    user3.username: user3,
}


app = Flask(__name__)
app.secret_key = 'mgc1234'


@app.route("/")
def index():
    return render_template("game_list.html", title=title, games=games)


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
    game = Game(name, category, console)
    games.append(game)

    return redirect(url_for('index'))


@app.route("/login")
def login():
    next = request.args.get('next')
    return render_template("login.html", next=next)


@app.route("/auth", methods=["POST"])
def authenticate():
    if request.form['user'] in users:
        user = users[request.form['user']]
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

