import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
from mgc import app


class GameForm(FlaskForm):
    name = StringField(
        "Name", [validators.data_required(), validators.length(min=1, max=50)]
    )
    category = StringField(
        "Category", [validators.data_required(), validators.length(min=1, max=40)]
    )
    console = StringField(
        "Console", [validators.data_required(), validators.length(min=1, max=20)]
    )
    save = SubmitField('Save')

def image_recovery(id):
    for filename in os.listdir(app.config["UPLOAD_PATH"]):
        if f"cover_{id}" in filename:
            return filename
    return "default_cover.jpg"


def delete_file(id):
    filename = image_recovery(id)
    if filename != "default_cover.jpg":
        os.remove(os.path.join(app.config["UPLOAD_PATH"], filename))
