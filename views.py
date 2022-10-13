from flask import render_template, redirect, request, session, flash, url_for
from mgc import app, db
from models import Games, Users

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
        flash('Already existing game!')
        return redirect(url_for('index'))
    new_game = Games(name=name, category=category, console=console)
    db.session.add(new_game)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/edit/<int:id>")
def edit(id):
    if 'user_active' not in session or session['user_active'] is None:
        return redirect(url_for('login', next=url_for('edit')))
    game = Games.query.filter_by(id=id).first()
    return render_template("edit.html", title="Editing Game", game=game)

@app.route('/update', methods=['POST'])
def update():
    game = Games.query.filter_by(id=request.form['id']).first()
    game.name = request.form['name']
    game.category = request.form['category']
    game.console = request.form['console']
    db.session.add(game)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/delete/<int:id>")
def delete(id):
    if 'user_active' not in session or session['user_active'] is None:
        return redirect(url_for('login'))
    Games.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Successfully Delete!')
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

