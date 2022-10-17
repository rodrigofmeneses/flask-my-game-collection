from flask import (
    render_template,
    redirect,
    request,
    session,
    flash,
    url_for,
    send_from_directory,
)
from mgc import app, db
from models import Games
from helpers import image_recovery, delete_file, GameForm

import time


@app.route("/")
def index():
    games = Games.query.order_by(Games.id)
    return render_template("list.html", title="Games", games=games)


@app.route("/new")
def new():
    if "user_active" not in session or session["user_active"] is None:
        return redirect(url_for("login", next=url_for("new")))
    form = GameForm()
    return render_template("new.html", title="New Game", form=form)


@app.route("/create", methods=["POST"])
def create():
    form = GameForm(request.form)
    if not form.validate_on_submit():
        return redirect(url_for("new"))

    name = form.name.data
    category = form.category.data
    console = form.console.data

    game = Games.query.filter_by(name=name).first()
    if game:
        flash("Already existing game!")
        return redirect(url_for("index"))
    new_game = Games(name=name, category=category, console=console)
    db.session.add(new_game)
    db.session.commit()

    file = request.files["file"]
    upload_path = app.config["UPLOAD_PATH"]
    timestamp = time.time()
    file.save(f"{upload_path}/cover_{new_game.id}-{timestamp}.jpg")

    return redirect(url_for("index"))


@app.route("/edit/<int:id>")
def edit(id):
    if "user_active" not in session or session["user_active"] is None:
        return redirect(url_for("login", next=url_for("edit", id=id)))
    game = Games.query.filter_by(id=id).first()
    form = GameForm()
    form.name.data = game.name
    form.category.data = game.category
    form.console.data = game.console
    game_cover = image_recovery(id)
    return render_template(
        "edit.html", title="Editing Game", id=id, game_cover=game_cover, form=form
    )


@app.route("/update", methods=["POST"])
def update():
    form = GameForm(request.form)

    if form.validate_on_submit():
        game = Games.query.filter_by(id=request.form["id"]).first()
        game.name = form.name.data
        game.category = form.category.data
        game.console = form.console.data

        db.session.add(game)
        db.session.commit()

        file = request.files["file"]
        upload_path = app.config["UPLOAD_PATH"]
        timestamp = time.time()
        delete_file(game.id)
        file.save(f"{upload_path}/cover_{game.id}-{timestamp}.jpg")
    return redirect(url_for("index"))


@app.route("/delete/<int:id>")
def delete(id):
    if "user_active" not in session or session["user_active"] is None:
        return redirect(url_for("login"))
    Games.query.filter_by(id=id).delete()
    db.session.commit()

    delete_file(id)
    flash("Successfully Delete!")
    return redirect(url_for("index"))


@app.route("/uploads/<file_name>")
def image(file_name):
    return send_from_directory("uploads", file_name)
