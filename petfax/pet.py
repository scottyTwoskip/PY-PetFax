from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print (pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/<int:index>')
def show(index):
    if index >= len(pets) or index < 0:
        return "Pet not found", 404
    pet = pets[index]
    return render_template('show_pet.html', pet=pet)

@bp.route('/facts/new')
def new_fact():
    return render_template('new_fact.html')

#git test