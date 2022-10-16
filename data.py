import streamlit as st
import pandas as pd




st.title('💾Data Analysis of Consensus Clients')
st.markdown('The aim is to provide a **Data Analysis of the Consensus Clients landscape to statistically identify inconsistency, seeking to improve the Consensus Layer.**')
    
    

st.header('Client Data')

block_data = pd.read_csv('data.csv')
st.write(block_data.head())

numberofslots_dist = pd.DataFrame(block_data['Client'].value_counts())
st.bar_chart(numberofslots_dist)
