from flask_wtf import FlaskForm
from wtforms import  StringField, validators, SubmitField, DateTimeField , IntegerField


class TeacherForm(FlaskForm):
    pass_number = IntegerField("Pass number:")

    full_name = StringField("Teacher name: ", [
                                    validators.DataRequired("Please enter  name."),
    ])

    department = StringField("Department:")


    submit = SubmitField("Save")