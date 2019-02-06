import pandas as pd
import numpy as np
import pickle


# make a function and feed application into this function:

def calculate_loan_result(application):
    # loading the model
    model_file_object=open("model.pkl", "rb")
    model_loan = pickle.load(model_file_object)


    # populating the dataframe with response
    df = pd.DataFrame(application, index=[0])
    df.credit_history = df.credit_history.astype(int)
    df = df.drop(['user_id', 'submit', 'csrf_token'], axis=1)
    df['loan_amount_log'] = np.log(df['loan_amount'])

    # creating empty data frame
    df_model = pd.DataFrame(columns=['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                                     'Loan_Amount_Term', 'Credit_History', 'LoanAmount_log', 'Gender_Female',
                                     'Gender_Male', 'Married_No', 'Married_Yes', 'Dependents_0',
                                     'Dependents_1', 'Dependents_2', 'Dependents_3+', 'Education_Graduate',
                                     'Education_Not Graduate', 'Self_Employed_No', 'Self_Employed_Yes',
                                     'Property_Area_Rural', 'Property_Area_Semiurban',
                                     'Property_Area_Urban'])

    # filling data into dataframe - done every time
    df_model['ApplicantIncome'] = df['applicant_income']
    df_model['CoapplicantIncome'] = df['coapplicant_income']
    df_model['LoanAmount'] = df['loan_amount']
    df_model['Loan_Amount_Term'] = df['loan_term_days']
    df_model['Credit_History'] = df['credit_history']
    df_model['LoanAmount_log'] = df['loan_amount_log']
    df_model['Gender_Female'] = df['gender'].apply(lambda x: 1 if x == "Female" else 0)
    df_model['Gender_Male'] = df['gender'].apply(lambda x: 1 if x == "Male" else 0)
    df_model['Married_No'] = df['married'].apply(lambda x: 1 if x == "No" else 0)
    df_model['Married_Yes'] = df['married'].apply(lambda x: 1 if x == "Yes" else 0)
    df_model['Dependents_0'] = df['dependents'].apply(lambda x: 1 if x == "0" else 0)
    df_model['Dependents_1'] = df['dependents'].apply(lambda x: 1 if x == "1" else 0)
    df_model['Dependents_2'] = df['dependents'].apply(lambda x: 1 if x == "2" else 0)
    df_model['Dependents_3+'] = df['dependents'].apply(lambda x: 1 if x == "3+" else 0)
    df_model['Education_Graduate'] = df['education'].apply(lambda x: 1 if x == "Graduate" else 0)
    df_model['Education_Not Graduate'] = df['education'].apply(lambda x: 1 if x == "Not Graduate" else 0)
    df_model['Self_Employed_No'] = df['self_employed'].apply(lambda x: 1 if x == "No" else 0)
    df_model['Self_Employed_Yes'] = df['gender'].apply(lambda x: 1 if x == "Yes" else 0)
    df_model['Property_Area_Rural'] = df['property_area'].apply(lambda x: 1 if x == "Rural" else 0)
    df_model['Property_Area_Semiurban'] = df['property_area'].apply(lambda x: 1 if x == "Semiurban" else 0)
    df_model['Property_Area_Urban'] = df['property_area'].apply(lambda x: 1 if x == "Urban" else 0)

    # predicting values
    pred_test = model_loan.predict(df_model)

    # delete df model after each assessment and close the file
    df_model = df_model[0:0]
    model_file_object.close()

    # giving a message with the result
    return pred_test[0]
