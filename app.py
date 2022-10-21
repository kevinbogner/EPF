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
col1, col2 = st.columns(2)
col1.metric("Last Updated on Slot:", "4953535")
col2.metric("Last Updated on Block:", "15789106")


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

@st.cache
def load_overview_data(nrows):
    data = pd.read_csv('./data/overview.csv', nrows=nrows)
    return data

@st.cache
def load_prysm_data(nrows):
    data = pd.read_csv('./data/prysm.csv', nrows=nrows)
    return data

@st.cache
def load_lighthouse_data(nrows):
    data = pd.read_csv('./data/lighthouse.csv', nrows=nrows)
    return data

@st.cache
def load_teku_data(nrows):
    data = pd.read_csv('./data/teku.csv', nrows=nrows)
    return data

@st.cache
def load_nimbus_data(nrows):
    data = pd.read_csv('./data/nimbus.csv', nrows=nrows)
    return data

@st.cache
def load_lodestar_data(nrows):
    data = pd.read_csv('./data/lodestar.csv', nrows=nrows)
    return data



#---Load data---
slotclientreward_data = load_slotclientreward_data(100)
relay7d_data = load_relay7d_data(100)
relay30d_data = load_relay30d_data(100)
overview_data = load_overview_data(100)
prysm_data = load_prysm_data(100)
lighthouse_data = load_lighthouse_data(100)
teku_data = load_teku_data(100)
nimbus_data = load_nimbus_data(100)
lodestar_data = load_lodestar_data(100)


#---Consensus Clients Overview---
st.subheader('Consensus Clients Overview')

col1, col2 = st.columns(2)

#Consensus Clients Overview - Distribution
with col1:
    fig = px.pie(overview_data, values='slots', names='Client', title='Client Distribution')
    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Consensus Clients Overview - Rewards/Slot
with col2:
    fig = px.bar(overview_data, x = 'Client', y = 'averagereward', color='Client', title='BlockReward/Slot Grouped by Client')
    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

st.subheader('Data Grouped by Client')

contact_options = ["Select Client", "Prysm", "Lighthouse", "Teku", "Nimbus", "Lodestar"]
contact_selected = st.selectbox("Select Client", label_visibility="hidden", options = contact_options)

#---Prysm---
col1, col2 = st.columns(2)
if contact_selected == "Prysm":

#Prysm - Distribution
    with col1:
        fig = px.pie(prysm_data, values='slots', names='relay', title='Prysm - Relay Distribution')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Prysm - Rewards/Slot
    with col2:
        fig = px.bar(prysm_data, x = 'relay', y = 'averagereward', color='relay', title='Prysm - BlockReward/Slot Grouped by Relay')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    st.write(prysm_data)


#---Lighthouse---
col1, col2 = st.columns(2)
if contact_selected == "Lighthouse":

#Lighthouse - Distribution
    with col1:
        fig = px.pie(lighthouse_data, values='slots', names='relay', title='Lighthouse - Relay Distribution')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Lighthouse - Rewards/Slot
    with col2:
        fig = px.bar(lighthouse_data, x = 'relay', y = 'averagereward', color='relay', title='Lighthouse - BlockReward/Slot Grouped by Relay')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    st.write(lighthouse_data)


#---Teku---
col1, col2 = st.columns(2)
if contact_selected == "Teku":

#Teku - Distribution
    with col1:
        fig = px.pie(teku_data, values='slots', names='relay', title='Teku - Relay Distribution')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Teku - Rewards/Slot
    with col2:
        fig = px.bar(teku_data, x = 'relay', y = 'averagereward', color='relay', title='Teku - BlockReward/Slot Grouped by Relay')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    st.write(teku_data)


#---Nimbus---
col1, col2 = st.columns(2)
if contact_selected == "Nimbus":

#Nimbus - Distribution
    with col1:
        fig = px.pie(nimbus_data, values='slots', names='relay', title='Nimbus - Relay Distribution')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Nimbus - Rewards/Slot
    with col2:
        fig = px.bar(nimbus_data, x = 'relay', y = 'averagereward', color='relay', title='Nimbus - BlockReward/Slot Grouped by Relay')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    st.write(nimbus_data)


#---Lodestar---
col1, col2 = st.columns(2)
if contact_selected == "Lodestar":

#Lodestar - Distribution
    with col1:
        fig = px.pie(lodestar_data, values='slots', names='relay', title='Lodestar - Relay Distribution')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Lodestar - Rewards/Slot
    with col2:
        fig = px.bar(lodestar_data, x = 'relay', y = 'averagereward', color='relay', title='Lodestar - BlockReward/Slot Grouped by Relay')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    st.write(lodestar_data)


#---Relay Last 7 Days---
#st.subheader('Relay Last 7 Days')

#col1, col2 = st.columns(2)

#Relay Last 7 Days - Distribution
#with col1:
#    fig = px.pie(relay7d_data, values='BlockCount', names='Name', title='Distribution')
#    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Relay Last 7 Days - Distribution
#with col2:
#    fig = px.bar(relay7d_data, x = 'Name', y = 'AverageReward', color='Name', title='Rewards/Slot')
#    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


#---Relay Last 30 Days----
#st.subheader('Relay Last 30 Days')

#col1, col2 = st.columns(2)

#Relay Last 30 Days - Distribution
#with col1:
#    fig = px.pie(relay30d_data, values='BlockCount', names='Name', title='Distribution')
#    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

#Relay Last 30 Days - Rewards/Slot
#with col2:
#    fig = px.bar(relay30d_data, x = 'Name', y = 'AverageReward', color='Name', title='Rewards/Slot')
#    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


#---Data---
#st.subheader('Data')

#col1, col2, col3 = st.columns(3)

#with col1:
#    if st.checkbox('Slot Client Reward'):
#        st.write(slotclientreward_data)

#with col2:
#    if st.checkbox('Relay 7d'):
#        st.write(relay7d_data)

#with col3:
#    if st.checkbox('Relay 30d'):
#        st.write(relay30d_data)


#---Footer---
#st.subheader('Footer')

