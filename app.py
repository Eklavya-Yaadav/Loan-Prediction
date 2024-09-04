# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:21:34 2024

@author: eklavya yaadav
"""
import numpy as np
import pickle
import pandas as pd
import streamlit as st
#from sklearn.preprocessing import StandardScaler

model = pickle.load(open('Eklavya_loan','rb'))



def loan_prediction(input_data):
    
    a = pd.to_numeric(input_data)
    b = np.asarray(a)
    c = b.reshape(1,-1)
    
    predicted_status = model.predict(c)
    print(predicted_status)

    if (predicted_status[0] == 0):
      return 'Approved'
    else:
      return 'Rejected'
  
    
  
def main():
    
    
    # giving a title
    st.title('Loan Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Gender = st.text_input('Gender (0-Female, 1-Male)')
    Married = st.text_input('Married (0-NO, 1-YES) ')
    Dependents = st.text_input('Dependents (1, 2, 3, 3+)')
    Education = st.text_input('Education (0-Not Graduate, 1-Graduate)')
    Self_Employed = st.text_input('Self Employed (0-NO, 1-YES)')
    Total_Income = st.text_input('Total Income')
    Loan_Amount = st.text_input('Loan Amount')
    Loan_Amount_Term = st.text_input('Loan Amount Term')
    Credit_History = st.text_input('Credit History (0-Bad, 1-Good)')
    Property_Area = st.text_input('Property Area (0-Urban, 1-Semi-Urban, 2-Rural)')
    
    
    # code for Prediction
    Loan_Status = ''
    
    # creating a button for Prediction
    
    if st.button('Loan Prediction'):
        Loan_Status = loan_prediction([Gender, Married, Dependents, Education, Self_Employed, Total_Income, Loan_Amount, Loan_Amount_Term, Credit_History, Property_Area ])
        
        
    st.success(Loan_Status)
    
    
    
    
    
if __name__ == '__main__':
    main()
    

























