from flask_wtf import FlaskForm
from wtforms import validators, SubmitField, SelectField, StringField, IntegerField


class SubjectForm(FlaskForm):

    pass_num = IntegerField("pass_num:")
    sbname = StringField("Name:")
    student_rating = IntegerField("Rating:")
    gradebook_number = IntegerField("gradebook_number:")
    pass_number = IntegerField("pass_number")
    submit = SubmitField("Save")


    def __init__(self,pass_num ,sbname ,student_rating ,gradebook_number,pass_number ):
        self.pass_num = pass_num
        self.sbname = sbname
        self.student_rating = student_rating
        self.gradebook_number = gradebook_number
        self.pass_number = pass_number

    def to_string(self):
        return "Subject: " + self.sbname + " Teacher:(" + self.pass_numbe + ")"
