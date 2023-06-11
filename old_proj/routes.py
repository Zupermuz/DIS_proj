from flask import Blueprint, flash, redirect, render_template, request, url_for
from models import add_fridge_item, get_fridge_content

RoutesBlueprint = Blueprint('RoutesBlueprint', __name__)

posts = [{}]

@RoutesBlueprint.route('/')
@RoutesBlueprint.route('/index')
def index():
    return render_template('index.html')

@RoutesBlueprint.route('/about/')
def about():
    return render_template('about.html')

@RoutesBlueprint.route('/fridge/')
def fridge():
    fridge = get_fridge_content(1)

    return render_template('fridge.html', fridge = fridge)

@RoutesBlueprint.route('/add_fridge_item/', methods=('GET', 'POST'))
def add_fridge_item_route():
    if request.method == 'POST':
        food = request.form['food']

        if not food:
            flash('Type something!')
        else:
            add_fridge_item(1, food)
            return redirect(url_for('RoutesBlueprint.fridge'))
    return render_template('add_fridge_item.html')