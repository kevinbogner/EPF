import streamlit as st
import pandas as pd
import plotly.express as px

#---Streamlit Configs---
st.set_page_config(page_title="Data Analysis Consensus Clients",
                   page_icon=":floppy_disk:",
                   layout="wide"
                   )


#---Overview---
st.title('💾Data Analysis of Consensus Clients')
st.markdown('Data provided by [blockprint](https://github.com/sigp/blockprint) and [beaconcha.in](https://beaconcha.in/). Thank You:heart:')
st.markdown('Last Updated on Slot: 4895291')


#---Import data from .csv---
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


#---Load data---
slotclientreward_data = load_slotclientreward_data(100)
relay7d_data = load_relay7d_data(100)
relay30d_data = load_relay30d_data(100)


#---Consensus Clients---
st.subheader('Consensus Clients')

col1, col2 = st.columns(2)

#Consensus Clients - Distribution
with col1:
    fig = px.pie(slotclientreward_data, values='Number of Slots', names='Client', title='Distribution')
    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Consensus Clients - Rewards/Slot
with col2:
    fig = px.bar(slotclientreward_data, x = 'Client', y = 'Average Reward/Slot', color='Client', title='Rewards/Slot')
    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


#---Relay Last 7 Days---
st.subheader('Relay Last 7 Days')

col1, col2 = st.columns(2)

#Relay Last 7 Days - Distribution
with col1:
    fig = px.pie(relay7d_data, values='BlockCount', names='Name', title='Distribution')
    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Relay Last 7 Days - Distribution
with col2:
    fig = px.bar(relay7d_data, x = 'Name', y = 'AverageReward', color='Name', title='Rewards/Slot')
    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


#---Relay Last 30 Days----
st.subheader('Relay Last 30 Days')

col1, col2 = st.columns(2)

#Relay Last 30 Days - Distribution
with col1:
    fig = px.pie(relay30d_data, values='BlockCount', names='Name', title='Distribution')
    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Relay Last 30 Days - Rewards/Slot
with col2:
    fig = px.bar(relay30d_data, x = 'Name', y = 'AverageReward', color='Name', title='Rewards/Slot')
    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


#---Data---
st.subheader('Data')

col1, col2, col3 = st.columns(3)

with col1:
    if st.checkbox('Slot Client Reward'):
        st.write(slotclientreward_data)

with col2:
    if st.checkbox('Relay 7d'):
        st.write(relay7d_data)

with col3:
    if st.checkbox('Relay 30d'):
        st.write(relay30d_data)


#---Footer---
st.subheader('Footer')