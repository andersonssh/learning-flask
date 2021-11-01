from . import auth
from flask_login import login_required, logout_user, login_user
from werkzeug.security import (check_password_hash,
                               generate_password_hash)
from datetime import timedelta

from ..forms import LoginForm, RegisterForm
from flask import render_template, redirect, url_for, flash
from ..models import User
from .. import db

@auth.route("/register", methods=["GET", "POST"])
def register():
    formm = RegisterForm()
    if formm.validate_on_submit():
        user = User()
        user.name = formm.name.data
        user.email = formm.email.data
        user.password = generate_password_hash(formm.password.data)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("register.html", form=formm)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    #valida o formulario
    print('login')
    if form.validate_on_submit():
        print('validado anti crsf')
        user = User.query.filter_by(email=form.email.data).first()

        if not user:
            flash("Credênciais incorretas", "danger")
            return redirect(url_for(".login"))

        if not check_password_hash(user.password, form.password.data):
            flash("Usuário ou senha incorreto", "danger")
            return redirect(url_for(".login"))

        login_user(user, remember=form.remember.data, duration=timedelta(days=7))
        return redirect(url_for("index"))

    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))