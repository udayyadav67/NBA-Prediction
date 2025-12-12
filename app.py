import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

with open(r"D:\streamlit project\AQI CLS\knn_model.pkl", "rb") as f:
    model=pickle.load(f)
    

st.title("AQI CLASS PREDICTION APP")
st.write("Bollu Uday Yadav")

City = st.selectbox("City",['Ahmedabad', 'Talcher', 'Mumbai', 'Kolkata', 'Patna', 'Delhi',
       'Hyderabad', 'Bengaluru', 'Chandigarh', 'Coimbatore', 'Lucknow',
       'Chennai', 'Gurugram', 'Shillong', 'Jaipur', 'Jorapokhar', 'Kochi',
       'Amaravati', 'Visakhapatnam', 'Guwahati', 'Amritsar',
       'Brajrajnagar', 'Ernakulam', 'Thiruvananthapuram', 'Aizawl',
       'Bhopal'])

PM2_5 = float(st.number_input("PM2.5", value = 0.0))
NO = float(st.number_input("NO", value = 0.0))
NO2 = float(st.number_input("NO2", value = 0.0))
NOx = float(st.number_input("NOx",value = 0.0))
CO = float(st.number_input("CO", value = 0.0))
SO2 = float(st.number_input("SO2",value = 0.0))
O3 = float(st.number_input("O3",value = 0.0))
Benzene = float(st.number_input("Benzene",value = 0.0))

if st.button("PREDICT AQI CLASS"):

    input_df = pd.DataFrame([{
        "City" : City,
        "PM2.5" : PM2_5,
        "NO" : NO,
        "NO2" : NO2,
        "NOx" : NOx,
        "CO" : CO,
        "SO2" : SO2,
        "O3" : O3,
        "Benzene" : Benzene
    }])
    
    result = model.predict(input_df)[0]

    st.success(f"Predicted AQI Class :  {result}")