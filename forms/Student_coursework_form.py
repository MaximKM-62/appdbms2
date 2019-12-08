from flask_wtf import FlaskForm
from wtforms import  validators, SubmitField, SelectField, StringField, IntegerField


class CourseworkForm(FlaskForm):
    initalization_num = IntegerField("Initialization_number:")
    gradebook_number = IntegerField("Gradebook_number:")
    cwname = StringField("Name:")
    research_direction = StringField("Research direction:")
    mark = IntegerField("Mark:")



    submit = SubmitField("Save")