import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

#---Streamlit Configs---
st.set_page_config(page_title="Data Analysis Consensus Clients",
                   page_icon=":floppy_disk:",
                   layout="wide"
                   )

st.title('💾Data Analysis of Consensus Clients')

#---Import TOTAL data from .csv---
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


#---Load TOTAL data---
overview_data = load_overview_data(100)
prysm_data = load_prysm_data(100)
lighthouse_data = load_lighthouse_data(100)
teku_data = load_teku_data(100)
nimbus_data = load_nimbus_data(100)
lodestar_data = load_lodestar_data(100)


#---Import 7d data from .csv---
@st.cache
def load_overview7_data(nrows):
    data = pd.read_csv('./data/overview7.csv', nrows=nrows)
    return data

@st.cache
def load_prysm7_data(nrows):
    data = pd.read_csv('./data/prysm7.csv', nrows=nrows)
    return data

@st.cache
def load_lighthouse7_data(nrows):
    data = pd.read_csv('./data/lighthouse7.csv', nrows=nrows)
    return data

@st.cache
def load_teku7_data(nrows):
    data = pd.read_csv('./data/teku7.csv', nrows=nrows)
    return data

@st.cache
def load_nimbus7_data(nrows):
    data = pd.read_csv('./data/nimbus7.csv', nrows=nrows)
    return data

@st.cache
def load_lodestar7_data(nrows):
    data = pd.read_csv('./data/lodestar7.csv', nrows=nrows)
    return data


#---Load 7d data---
overview7_data = load_overview7_data(100)
prysm7_data = load_prysm7_data(100)
lighthouse7_data = load_lighthouse7_data(100)
teku7_data = load_teku7_data(100)
nimbus7_data = load_nimbus7_data(100)
lodestar7_data = load_lodestar7_data(100)
    

selected = option_menu(
    menu_title=None,
    options=["Last 7 Days", "From Merge to Now"],
    default_index=0,
    orientation="horizontal",
)

if selected == "From Merge to Now":
    st.title(f"You have selected {selected}")
        #---Overview---
    col1, col2 = st.columns(2)
    col1.metric("Range of Slots:", "4700013 - 4953535")
    col2.metric("Range of Blocks:", "15537394  - 15789106")



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

if selected == "Last 7 Days":
    st.title(f"You have selected {selected}")
        #---Overview---
    col1, col2 = st.columns(2)
    col1.metric("Range of Slots", "4903535 - 4953535")
    col2.metric("Range of Blocks", "15739391 - 15789106")


    #---Consensus Clients Overview---
    st.subheader('Consensus Clients Overview')

    col1, col2 = st.columns(2)

    #Consensus Clients Overview - Distribution
    with col1:
        fig = px.pie(overview7_data, values='slots', names='Client', title='Client Distribution')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Consensus Clients Overview - Rewards/Slot
    with col2:
        fig = px.bar(overview7_data, x = 'Client', y = 'averagereward', color='Client', title='BlockReward/Slot Grouped by Client')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    st.subheader('Data Grouped by Client')

    contact_options = ["Select Client", "Prysm", "Lighthouse", "Teku", "Nimbus", "Lodestar"]
    contact_selected = st.selectbox("Select Client", label_visibility="hidden", options = contact_options)

    #---Prysm---
    col1, col2 = st.columns(2)
    if contact_selected == "Prysm":

    #Prysm - Distribution
        with col1:
            fig = px.pie(prysm7_data, values='slots', names='relay', title='Prysm - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Prysm - Rewards/Slot
        with col2:
            fig = px.bar(prysm7_data, x = 'relay', y = 'averagereward', color='relay', title='Prysm - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

        st.write(prysm7_data)


    #---Lighthouse---
    col1, col2 = st.columns(2)
    if contact_selected == "Lighthouse":

    #Lighthouse - Distribution
        with col1:
            fig = px.pie(lighthouse7_data, values='slots', names='relay', title='Lighthouse - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Lighthouse - Rewards/Slot
        with col2:
            fig = px.bar(lighthouse7_data, x = 'relay', y = 'averagereward', color='relay', title='Lighthouse - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

        st.write(lighthouse7_data)


    #---Teku---
    col1, col2 = st.columns(2)
    if contact_selected == "Teku":

    #Teku - Distribution
        with col1:
            fig = px.pie(teku7_data, values='slots', names='relay', title='Teku - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Teku - Rewards/Slot
        with col2:
            fig = px.bar(teku7_data, x = 'relay', y = 'averagereward', color='relay', title='Teku - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

        st.write(teku7_data)


    #---Nimbus---
    col1, col2 = st.columns(2)
    if contact_selected == "Nimbus":

    #Nimbus - Distribution
        with col1:
            fig = px.pie(nimbus7_data, values='slots', names='relay', title='Nimbus - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Nimbus - Rewards/Slot
        with col2:
            fig = px.bar(nimbus7_data, x = 'relay', y = 'averagereward', color='relay', title='Nimbus - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

        st.write(nimbus7_data)


    #---Lodestar---
    col1, col2 = st.columns(2)
    if contact_selected == "Lodestar":

    #Lodestar - Distribution
        with col1:
            fig = px.pie(lodestar7_data, values='slots', names='relay', title='Lodestar - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Lodestar - Rewards/Slot
        with col2:
            fig = px.bar(lodestar7_data, x = 'relay', y = 'averagereward', color='relay', title='Lodestar - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

        st.write(lodestar7_data)



st.markdown('Data provided by [blockprint](https://github.com/sigp/blockprint) and [beaconcha.in](https://beaconcha.in/). Thank You:heart:')