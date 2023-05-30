import streamlit as st
import pickle 
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

kidney_model = pickle.load(open('kidney.pkl','rb'))

with st.sidebar:
    
    selected = option_menu('Prediction System',                
                          ['Chronic Kidney Disease'],
                           default_index=0)

if (selected == 'Chronic Kidney Disease'):
    
    # page title
    st.title('Chronic Kidney Disease prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('age')
        
    with col2:
        bp = st.text_input('blood_pressure')

    with col3:
        bgr = st.text_input('blood_glucose_random')
        
    
    with col3:
        al = st.text_input('albumin')
        
        
    with col1:
        pc = st.text_input('pus_cell')      
        
    with col2:
        sc = st.text_input('serum_creatinine')
        
    with col3:
        hemo = st.text_input('haemoglobin')
        
    with col1:
        wc = st.text_input('white_blood_cell_count')
        
    with col2:
        rc = st.text_input('red_blood_cell_count')
        
     
    # code for Prediction
    kidney_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('kidney Disease Test Result'):
        kidney_prediction = kidney_model.predict([[age, bp , al, pc, bgr, sc, hemo,
                                                     wc, rc]])                          
        
        if (kidney_prediction[0] == 0):
          kidney_diagnosis = 'The person does not has Chronic KIdney Disease'
        else:
          kidney_diagnosis = 'The person has Chronic KIdney Disease'
        
    st.success(kidney_diagnosis)