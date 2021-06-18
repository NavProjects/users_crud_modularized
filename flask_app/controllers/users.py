from flask import request, render_template, redirect, session
from flask_app import app
from flask_app.models.user import User


@app.route('/')
def change():
    return redirect('/users')


@app.route('/users')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users=users)


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    user_id = User.save(data)
    # id = User.select_last(data)
    print(user_id)
    return redirect(f"/user/{user_id}")


@app.route('/user/<int:user_id>')
def display_user(user_id):
    this_user = User.select_one({'id': user_id})
    return render_template('user.html', user=this_user)


@app.route('/user/<int:user_id>/remove')
def remove(user_id):
    User.remove({'id': user_id})
    return redirect('/')


@app.route('/user/<int:user_id>/edit')
def edit_user(user_id):
    return render_template('edit.html', user = User.select_one({'id': user_id}))


@app.route('/user/<int:user_id>/change',methods = ["POST"])
def update_user(user_id):
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        'id': user_id
    }
    User.change(data)
    return redirect (f'/user/{user_id}/edit')
