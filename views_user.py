from mgc import app
from flask import flash, request, render_template, redirect, url_for, session
from models import Users
from helpers import UserForm
from flask_bcrypt import check_password_hash


@app.route("/login")
def login():
    next = request.args.get("next")
    form = UserForm()
    return render_template("login.html", next=next, form=form)


@app.route("/auth", methods=["POST"])
def authenticate():
    form = UserForm(request.form)
    user = Users.query.filter_by(username=form.username.data).first()
    password = check_password_hash(user.password, form.password.data)
    if user and password:
        session["user_active"] = user.username
        flash(f"Welcome {user.username}. Successfully login!")
        next_page = request.form["next"]
        if next_page != "None":
            return redirect(next_page)
        return redirect(url_for("index"))
    flash(f"Failed to login")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session["user_active"] = None
    flash("Successful logout!")
    return redirect(url_for("index"))
