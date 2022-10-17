import streamlit as st
import pandas as pd
import plotly.express as px

#Streamlit Configs
st.set_page_config(page_title="Data Analysis Consensus Clients",
                   page_icon=":floppy_disk:",
                   layout="wide")

st.title('💾Data Analysis of Consensus Clients')
st.markdown('The aim is to provide a **Data Analysis of the Consensus Clients landscape to statistically identify inconsistency, seeking to improve the Consensus Layer.**')


#Import data from .csv
@st.cache
def load_slotclientreward_data(nrows):
    data = pd.read_csv('./data/slotclientreward.csv', nrows=nrows)
    return data

@st.cache
def load_relay7d_data(nrows):
    data = pd.read_csv('./data/relay7d.csv', nrows=nrows)
    return data

@st.cache
def load_relay30d_data(nrows):
    data = pd.read_csv('./data/relay30d.csv', nrows=nrows)
    return data


#Load data
slotclientreward_data = load_slotclientreward_data(100)
relay7d_data = load_relay7d_data(100)
relay30d_data = load_relay30d_data(100)


#Chart
st.subheader('Chart')

#BarChart
fig = px.bar(slotclientreward_data, x = 'Client', y = 'Number of Slots', color='Number of Slots', color_continuous_scale='Viridis')
st.plotly_chart(fig, use_container_width=True, sharing="streamlit")



#Data
st.subheader('Data')
if st.checkbox('Slot Client Reward'):
    st.markdown('Provided by [blockprint](https://github.com/sigp/blockprint) and [beaconcha.in](https://beaconcha.in/)')
    st.write(slotclientreward_data)

if st.checkbox('Relay 7d'):
    st.markdown('Provided by [beaconcha.in](https://beaconcha.in/)')
    st.write(relay7d_data)

if st.checkbox('Relay 30d'):
    st.markdown('Provided by [beaconcha.in](https://beaconcha.in/)')
    st.write(relay30d_data)


#Footer
st.subheader('Footer')