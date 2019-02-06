#database tables are referred to as models
from app import db
from datetime import datetime

#creating tables
class Loan_History(db.Model):
    __tablename__='loan_history'

    #autopopulated
    loan_result_id=db.Column(db.Integer,primary_key=True)

    #from form
    gender=db.Column(db.String(80),nullable=False)
    married=db.Column(db.String(80),nullable=False)
    dependents=db.Column(db.String(80),nullable=False)
    education=db.Column(db.String(80),nullable=False)
    self_employed=db.Column(db.String(80),nullable=False)
    applicant_income=db.Column(db.Integer,nullable=False)
    coapplicant_income=db.Column(db.Integer,nullable=False)
    loan_amount=db.Column(db.Integer,nullable=False)
    loan_term_days=db.Column(db.Integer, nullable=False)
    credit_history=db.Column(db.String(80),nullable=False)
    property_area=db.Column(db.String(80),nullable=False)
    #foreign key from users table
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    #populates from result after algorithm is run
    loan_result=db.Column(db.String(80))

    #autopopulated
    date=db.Column(db.DateTime,default=datetime.utcnow())

    def __init__(self,gender,married,dependents,education,self_employed,applicant_income,coapplicant_income,loan_amount,loan_term_days,credit_history,property_area,user_id,loan_result):

        self.gender=gender
        self.married=married
        self.dependents=dependents
        self.education=education
        self.self_employed=self_employed
        self.applicant_income=applicant_income
        self.coapplicant_income=coapplicant_income
        self.loan_amount=loan_amount
        self.credit_history=credit_history
        self.loan_term_days=loan_term_days
        self.property_area=property_area
        self.user_id=user_id
        self.loan_result=loan_result



    def __repr__(self):
        return 'The loan_result is {}, user_id is {}'.format(self.loan_result,self.user_id)


