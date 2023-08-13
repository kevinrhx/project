import streamlit as st
import pandas as pd
import numpy as np
import eda 
import prediction

navigation = st.sidebar.selectbox('pilihan:',('EDA','Bank Churn Predictor'))

if navigation == 'EDA':
    eda.run()
else:
    prediction.run()