import os
import random

from flask import Flask, render_template, request, redirect

from root.bll.dataservice import get_data, insert_data, get_data_by_id, delete_data, save, update_data, req1, req2, req3,get_data_by_init
from root.dal.model import Student, CourseWork, Subject,  Teacher
from root.forms.Student_form import Studform
from root.forms.Student_coursework_form import CourseworkForm

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Student', methods=['GET', 'POST'])
def forstudnt():
    result = get_data(Student)
    form = Studform()
    if request.method == 'POST':
        print(form.gradebook_number.data)
        students = get_data_by_id(Student, form.gradebook_number.data)
        if(form.gradebook_number.data == students.gradebook_number):

            students = Student(int(form.gradebook_number.data),form.full_name.data, form.stgroup.data, form.year_of_receipt.data)
            update_data(students, Student)
        else:
            students = Student(form.gradebook_number.data, form.full_name.data, form.stgroup.data,
                               form.year_of_receipt.data)
            insert_data(students)
        save()
        return redirect('/Student')

    return render_template('Student.html', students = result, form = form)

@app.route('/Student/delete/<gradebook_number>')
def user_delete(gradebook_number):
    delete_data(Student, gradebook_number)
    save()
    return redirect('/Student')

@app.route('/Student/edit/<gradebook_number>', methods=['GET'])
def student_edit(gradebook_number):
    if request.method == 'GET':
        students = get_data_by_id(Student, gradebook_number)
        result = get_data(Student)
        form = Studform()
        form.gradebook_number.data = students.gradebook_number
        form.full_name.data = students.full_name
        return render_template('Student.html', students = result, form = form)

@app.route('/Course_work', methods=['GET', 'POST'])
def forcoursework():
    result = get_data(CourseWork)
    form = CourseworkForm()
    if request.method == 'POST':
        print(form.initalization_num.data)
        works = get_data_by_init(CourseWork, form.initalization_num.data)
        if(form.initalization_num.data == works.initalization_num):
            work = Student(int(form.initalization_num.data),form.cwname.data, form.research_direction.data, form.gradebook_number.data)
            update_data(work,CourseWork)
        else:
            work = CourseWork(form.initalization_num.data, form.cwname.data, form.research_direction,
                               form.gradebook_number.data)
            insert_data(work)
        save()
        return redirect('/Course_work')

    return render_template('Course_work.html', work = result, form = form)


@app.route('/Course_work/edit/<initalization_num>', methods=['GET'])
def coursework_edit(initalization_num):
    if request.method == 'GET':
        works = get_data_by_id(CourseWork,initalization_num)
        result = get_data(CourseWork)
        form = CourseworkForm()
        form.initalization_num.data = works.initalization_num
        form.cwname.data = works.cwname
        return render_template('Course_work.html', works = result, form = form)

