from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import login_required, current_user
from .models import getUserDataById, ingr_add_command, ingr_remove_command, User

views = Blueprint('views', __name__)

@views.route('/', methods=('GET', 'POST'))
@views.route('/home', methods=('GET', 'POST'))
@login_required
def home():
    user_data = getUserDataById(current_user.get_id())
    if user_data:
        ingredients = user_data['ingr_list']

    if request.method == 'POST':
        ingr_to_add = request.form['ingr_to_add']
        if not ingr_to_add:
            flash('Type something!')
        else:
            ingr_add_command(current_user.get_id(), ingr_to_add)
            return redirect(url_for('views.home'))
    return render_template("home.html", ingredients = ingredients)

@views.route('/<int:id>/<ingr_to_remove>/ingr_remove', methods=('GET', 'POST'))
def ingr_remove(id, ingr_to_remove):
    ingr_remove_command(id, ingr_to_remove)
    #flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('views.home'))