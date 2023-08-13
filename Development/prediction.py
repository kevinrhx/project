import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

with open('rf_randomcv_best.pkl', 'rb') as file_1:
  grid_best = pickle.load(file_1)

with open('model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('model_encoder.pkl','rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('list_num_cols.txt', 'r') as file_4:
  list_num_cols = json.load(file_4)

with open('list_cat_cols.txt', 'r') as file_5:
  list_cat_cols = json.load(file_5)

def run():
    st.title('Admission predictor')
    with st.form('key=form_2022'):
        gender = st.radio('Gender- Male= M,Female= F',('Male','Female'),index=0)
        edu = st.radio('Education',('Uneducated', 'High School','College','Graduate','Post-Graduate','Doctorate','Unknown'),index=1)
        ms = st.radio('marital status',('Single', 'Married','Unknown'),index=0)
        ic = st.radio('Income bracket',('Less than $40K', '$40K - $60K', '$60K - $80K','$80K - $120K','$120K +','Unknown'),index=2)
        cc = st.radio('Card Type',('Blue', 'Silver', 'Gold', 'Platinum'),index=0)
        

        st.markdown('---')
        age = st.number_input('Customer ages',min_value =18, max_value = 100 ,value =40,help='age')
        dep = st.number_input('dependent count',min_value =0, max_value = 10 ,value =0,help='dependent')
        rel = st.number_input('Relationship',min_value =0, max_value = 6 ,value =1,help='Relationship')
        month12 = st.number_input('Months_Inactive_12_mon',min_value =0, max_value = 6 ,value =1,step=1,help='Months_Inactive_12_mon')
        contract12 = st.number_input('Contacts_Count_12_mon',min_value =0, max_value = 6 ,value =1,help='Contacts_Count_12_mon')
        cl = st.number_input('Customer ages',min_value =1000, max_value = 35000 ,value =4000,step=500,help='Credit_Limit')
        revbal = st.number_input('dependent count',min_value =0, max_value = 3000 ,value =500,step=50,help='Total_Revolving_Bal')
        amtq4 = st.number_input('Degree Percentage',min_value =0.0, max_value = 4.0 ,value =1.0,step=0.1,help='Total_Amt_Chng_Q4_Q1')
        tamnt = st.number_input('dependent count',min_value =0, max_value = 20000 ,value =500,step=50,help='Total_Trans_Amt')
        ctq4 = st.number_input('Degree Percentage',min_value =0.0, max_value = 4.0 ,value =1.0,step=0.1,help='Total_Ct_Chng_Q4_Q1')
        ratio = st.number_input('Avg_Utilization_Ratio',min_value =0.0, max_value = 1.0 ,value =1.0,step=0.01,help='Avg_Utilization_Ratio')
        submitted = st.form_submit_button('predict')

    data_inf = {
      "Gender":gender, 
      "Education_Level":edu, 
      "Marital_Status":ms, 
      "Income_Category":ic, 
      "Card_Category":cc,
      "Customer_Age":age, 
      "Dependent_count":dep, 
      "Total_Relationship_Count":rel, 
      "Months_Inactive_12_mon":month12, 
      "Contacts_Count_12_mon":contract12, 
      "Credit_Limit":cl, 
      "Total_Revolving_Bal":revbal, 
      "Total_Amt_Chng_Q4_Q1":amtq4, 
      "Total_Trans_Amt":tamnt, 
      "Total_Ct_Chng_Q4_Q1":ctq4, 
      "Avg_Utilization_Ratio":ratio
    }

    data_inf = pd.DataFrame([data_inf])
    #data_inf#membuat contoh input

    st.dataframe(data_inf)


    if submitted:
        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]
        data_inf_num_scaled = model_scaler.transform(data_inf_num)
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat).toarray()
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)
        #y_pred_inf = bag_clf.predict(data_inf_final)

        y_pred_inf = grid_best.predict(data_inf_final)
        #st.write(str(y_pred_inf))


        if y_pred_inf[0] == 'Attrited Customer':
          st.title(str('The Customer are attrited '))
        else:
          st.title(str('The customner are not attrited'))

    if __name__ == '__main__':
        run()
