from flask_wtf import FlaskForm

from wtforms import StringField,SubmitField,SelectField,IntegerField,FloatField
from wtforms.validators import DataRequired,NumberRange

class SubmitApplication(FlaskForm):

    gender=SelectField('2.Gender',choices=[('Male','Male'),('Female','Female')],validators=[DataRequired()])
    married = SelectField('1.Married', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    dependents=SelectField('3.Dependents',choices=[('0','0'),('1','1'),('2','2'),('3+','3+')],validators=[DataRequired()])
    education=SelectField('4.Education',choices=[('Graduate','Graduate'),('Not Graduate','Not Graduate')],validators=[DataRequired()])
    self_employed= SelectField('5.Self-Employed', choices=[('Yes', 'Yes'), ('No', 'No')], validators=[DataRequired()])
    applicant_income=FloatField('6.Applicant income',validators=[NumberRange(0,100000,message='please enter a number between 0 and 100000')])
    coapplicant_income = FloatField('7.Coapplicant income, please enter 0 if no coapplicant', validators=[ NumberRange(0, 100000,message='please enter a number between 0 and 100000')])
    loan_amount=FloatField('8.Wished loan amount', validators=[DataRequired(),NumberRange(0, 100000,message='please enter a number between 1 and 100000')])
    loan_term_days=IntegerField('9.Loan Term in days',validators=[DataRequired(),NumberRange(1,360,message='please enter a number between 1 and 360')])
    credit_history=SelectField('10.Credit History',choices=[('1','I have credit history'),('0','I have no credit history')],validators=[DataRequired()])
    property_area=SelectField('11.Property Area',choices=[('Urban','Urban'),('Semiurban','Semiurban'),('Rural','Rural')],validators=[DataRequired()])
    user_id=IntegerField('Your user ID',validators=[DataRequired()])
    submit=SubmitField('Submit')
