from flask import render_template
from forms import AddPetForm

@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template('list_pets.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        pet = Pet(name=form.name.data, species=form.species.data, photo_url=form.photo_url.data, age=form.age.data, notes=form.notes.data)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('list_pets'))

    return render_template('add_pet.html', form=form)