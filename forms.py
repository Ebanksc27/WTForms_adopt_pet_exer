from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, URLField
from wtforms.validators import AnyOf, URL, NumberRange, Optional

class AddPetForm(FlaskForm):
    name = StringField("Pet Name", [InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = URLField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    photo_url = URLField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available?")

