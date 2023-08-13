import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config(
    page_title ='Churn predictor',
    layout='wide',
    initial_sidebar_state='expanded'

)


def run():
    ##title
    st.title('Credit Card churn')

    st.subheader('A website to predict credit card churn')

    image = Image.open('CC.jpg')

    st.image(image, caption='Credit Card')
    st.write('Untuk melakukan prediksi masuklah ke halaman prediction')
    st.markdown('---')

    df = pd.read_csv('BankChurners.csv')
   

    st.write('Plot education')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Education_Level',data =df)
    st.pyplot(fig)

    st.write('Plot Card_Category')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Card_Category',data =df)
    st.pyplot(fig)

    st.write('churn ratio')
    fig = plt.figure(figsize=(15,5))
    keys = ['Not Churn', 'Churn']
    plt.pie(df['Attrition_Flag'].value_counts() ,labels=keys, autopct='%0.2f%%')
    st.pyplot(fig)



    pilihan = st.selectbox('pilihan:',('Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count', 'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal', 'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[pilihan],bins=30,kde=True)
    st.pyplot(fig)




    if __name__ == '__main__':
        run()