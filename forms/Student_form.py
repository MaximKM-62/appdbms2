from flask_wtf import FlaskForm
from wtforms import  StringField, validators, SubmitField , IntegerField, DateTimeField



class Studform(FlaskForm):

    gradebook_number = IntegerField("Gradebook_number:", [
                                    validators.DataRequired("Please enter  number")
    ])

    full_name = StringField("Student name: ", [
                                    validators.DataRequired("Please enter  name")
    ])
    stgroup = StringField("Group:")
    year_of_receipt = DateTimeField("Year_of_receipt:")
    submit = SubmitField("Save")
