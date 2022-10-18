import streamlit as st
import pandas as pd
import plotly.express as px

#Streamlit Configs
st.set_page_config(page_title="Data Analysis Consensus Clients",
                   page_icon=":floppy_disk:",
                   #layout="wide"
                   )

st.title('💾Data Analysis of Consensus Clients')
st.markdown('Data provided by [blockprint](https://github.com/sigp/blockprint) and [beaconcha.in](https://beaconcha.in/). Thank You:heart:')


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


#BarChart
st.subheader('Consensus Clients Distribution')
fig = px.bar(slotclientreward_data, x = 'Client', y = 'Number of Slots', color='Number of Slots', color_continuous_scale='Viridis')
st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


#PieChart 7Days
st.subheader('Relay Distribution Last 7 Days')
fig = px.pie(relay7d_data, values='BlockCount', names='Name')
st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


#PieChart 7Days
st.subheader('Relay Distribution Last 30 Days')
fig = px.pie(relay30d_data, values='BlockCount', names='Name')
st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


#Data
st.subheader('Data')
if st.checkbox('Slot Client Reward'):
    st.write(slotclientreward_data)

if st.checkbox('Relay 7d'):
    st.write(relay7d_data)

if st.checkbox('Relay 30d'):
    st.write(relay30d_data)


#Footer
st.subheader('Footer')