from app.calculator import main
from app import db
from app.calculator.models import Loan_History
from flask import render_template,flash, request, redirect, url_for
from flask_login import login_required,current_user
from app.calculator.forms import SubmitApplication
from app.calculator.loan_model import calculate_loan_result
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

#using blueprints instead of app
@main.route('/')
@login_required
def display_history():
    id=current_user.id
    #filter only records based on usernumber
    history= Loan_History.query.filter_by(user_id=id)
    x=Loan_History.query.get(5)
    print(x)
    return render_template('home.html',history=history)

@main.route('/newapplication/<id>', methods=['GET','POST'])
@login_required
def submit_application(id):
    form=SubmitApplication()
    form.user_id.data=id
    if form.validate_on_submit():
        application=Loan_History(gender = form.gender.data,married =form.married.data,dependents=form.dependents.data,education =form.education.data,self_employed = form.self_employed.data,applicant_income =form.applicant_income.data ,coapplicant_income =form.coapplicant_income.data,loan_amount =form.loan_amount.data,loan_term_days=form.loan_term_days.data, credit_history =form.credit_history.data,property_area =form.property_area.data,user_id=form.user_id.data,loan_result="")
        db.session.add(application)
        db.session.commit()

        #calculating algorithm
        result=calculate_loan_result(form.data)

        #include result into the table
        application.loan_result=result
        db.session.commit()
        #if no history, do not show the header of the table, find the way to add scroller to the table
        #what happened to the cat?
        if result=='N':
           flash('Unfortunately, no loan could be granted on this occasion','error')
        else:
            flash('The loan of requested amount is available for you','good')

        return redirect(url_for('main.display_history'))
    return render_template('submit_application.html',form=form)





"""
this filter needs to be merged with above route in order to filter records based on the loaded user. 
 Models part 3, Section 9 explains more about this, separate html page made for this. 
@main,route('/display/history/<user_id>')
def display_history(user_id):
   """