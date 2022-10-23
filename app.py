import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

#---Streamlit Configs---
st.set_page_config(page_title="Data Analysis Consensus Clients",
                   page_icon=":floppy_disk:",
                   layout="wide"
                   )

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


#st.title('💾Data Analysis of Consensus Clients')
st.markdown("<h1 style='text-align: center; color: white;'>💾Data Analysis of Consensus Clients</h1>", unsafe_allow_html=True)

CLIENTCOLOR = {'Prysm':'aqua', 'Lighthouse':'mediumslateblue', 'Teku':'mediumblue', 'Nimbus':'orange','Lodestar':'yellow'}
RELAYCOLOR = {'flashbots':'blueviolet', 'bloxroute (max profit)':'crimson', 'blocknative':'darkseagreen', 'eden':'mediumslateblue', 'bloxroute (ethical)':'burlywood', 'manifold':'aqua', 'bloxroute (regulated)':'lightcoral', 'none':'palegreen'}

#---Import TOTAL data from .csv---
@st.cache
def load_relay_data(nrows):
    data = pd.read_csv('./data/total/relay.csv', nrows=nrows)
    return data

@st.cache
def load_relrew_data(nrows):
    data = pd.read_csv('./data/total/relrew.csv', nrows=nrows)
    return data

@st.cache
def load_reward_data(nrows):
    data = pd.read_csv('./data/total/reward.csv', nrows=nrows)
    return data

@st.cache
def load_overview_data(nrows):
    data = pd.read_csv('./data/total/overview.csv', nrows=nrows)
    return data


#---Load TOTAL data---
relay_data = load_relay_data(100)
relrew_data = load_relrew_data(100)
reward_data = load_reward_data(100)
overview_data = load_overview_data(100)


#---Import 7d data from .csv---
@st.cache
def load_relay7_data(nrows):
    data = pd.read_csv('./data/7days/relay7.csv', nrows=nrows)
    return data

@st.cache
def load_relrew7_data(nrows):
    data = pd.read_csv('./data/7days/relrew7.csv', nrows=nrows)
    return data

@st.cache
def load_reward7_data(nrows):
    data = pd.read_csv('./data/7days/reward7.csv', nrows=nrows)
    return data

@st.cache
def load_overview7_data(nrows):
    data = pd.read_csv('./data/7days/overview7.csv', nrows=nrows)
    return data


#---Load 7d data---
relay7_data = load_relay7_data(100)
relrew7_data = load_relrew7_data(100)
reward7_data = load_reward7_data(100)
overview7_data = load_overview7_data(100)
    

selected = option_menu(
    menu_title=None,
    options=["Last 7 Days", "From Merge to Now"],
    default_index=0,
    orientation="horizontal",
)

if selected == "From Merge to Now":
        #---Overview---
    col1, col2 = st.columns(2)

    highest = open('./data/total/highest.txt', "r")
    highest = int(highest.read())
    lowest = open('./data/total/lowest.txt', "r")
    lowest = int(lowest.read())

    col1.metric("From Slot:", lowest)
    col2.metric("To Slot:", highest)


    #---Consensus Clients Overview---
    col1, col2 = st.columns(2)

    #Consensus Clients Overview - Distribution
    with col1:
        fig = px.pie(overview_data, values='slot', names='client', title='Client Distribution', color='client', color_discrete_map=CLIENTCOLOR)
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Consensus Clients Overview - Rewards/Slot
    with col2:
        fig = px.bar(reward_data, x = 'client', y = 'reward', color='client', color_discrete_map=CLIENTCOLOR, title='BlockReward/Slot Grouped by Client')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #st.subheader('Data Grouped by Client')
    st.markdown("<h3 style='text-align: center; color: white;'>Data Grouped by Client</h3>", unsafe_allow_html=True)

    contact_options = ["Prysm", "Lighthouse", "Teku", "Nimbus", "Lodestar"]
    contact_selected = st.selectbox("Select Client", label_visibility="hidden", options = contact_options)

    #---Prysm---
    col1, col2 = st.columns(2)
    if contact_selected == "Prysm":

    #Prysm - Distribution
        with col1:
            fig = px.pie(relay_data, values='Prysm', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Prysm - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Prysm - Rewards/Slot
        with col2:
            fig = px.bar(relrew_data, x = 'relay', y = 'Prysm', color='relay', color_discrete_map=RELAYCOLOR, title='Prysm - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #---Lighthouse---
    col1, col2 = st.columns(2)
    if contact_selected == "Lighthouse":

    #Lighthouse - Distribution
        with col1:
            fig = px.pie(relay_data, values='Lighthouse', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Lighthouse - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Lighthouse - Rewards/Slot
        with col2:
            fig = px.bar(relrew_data, x = 'relay', y = 'Lighthouse', color='relay', color_discrete_map=RELAYCOLOR, title='Lighthouse - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


    #---Teku---
    col1, col2 = st.columns(2)
    if contact_selected == "Teku":

    #Teku - Distribution
        with col1:
            fig = px.pie(relay_data, values='Teku', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Teku - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Teku - Rewards/Slot
        with col2:
            fig = px.bar(relrew_data, x = 'relay', y = 'Teku', color='relay', color_discrete_map=RELAYCOLOR, title='Teku - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


    #---Nimbus---
    col1, col2 = st.columns(2)
    if contact_selected == "Nimbus":

    #Nimbus - Distribution
        with col1:
            fig = px.pie(relay_data, values='Nimbus', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Nimbus - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Nimbus - Rewards/Slot
        with col2:
            fig = px.bar(relrew_data, x = 'relay', y = 'Nimbus', color='relay', color_discrete_map=RELAYCOLOR, title='Nimbus - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


    #---Lodestar---
    col1, col2 = st.columns(2)
    if contact_selected == "Lodestar":

    #Lodestar - Distribution
        with col1:
            fig = px.pie(relay_data, values='Lodestar', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Lodestar - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Lodestar - Rewards/Slot
        with col2:
            fig = px.bar(relrew_data, x = 'relay', y = 'Lodestar', color='relay', color_discrete_map=RELAYCOLOR, title='Lodestar - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


if selected == "Last 7 Days":
        #---Overview---
    col1, col2 = st.columns(2)

    highest7 = open('./data/7days/highest7.txt', "r")
    highest7 = int(highest7.read())
    lowest7 = open('./data/7days/lowest7.txt', "r")
    lowest7 = int(lowest7.read())

    col1.metric("From Slot:", lowest7)
    col2.metric("To Slot:", highest7)


    #---Consensus Clients Overview---
    col1, col2 = st.columns(2)

    #Consensus Clients Overview - Distribution
    with col1:
        fig = px.pie(overview7_data, values='slot', names='client', title='Client Distribution', color='client', color_discrete_map=CLIENTCOLOR)
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Consensus Clients Overview - Rewards/Slot
    with col2:
        fig = px.bar(reward7_data, x = 'client', y = 'reward', color='client', color_discrete_map=CLIENTCOLOR, title='BlockReward/Slot Grouped by Client')
        st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #st.subheader('Data Grouped by Client')
    st.markdown("<h3 style='text-align: center; color: white;'>Data Grouped by Client</h3>", unsafe_allow_html=True)

    contact_options = ["Prysm", "Lighthouse", "Teku", "Nimbus", "Lodestar"]
    contact_selected = st.selectbox("Select Client", label_visibility="hidden", options = contact_options)

    #---Prysm---
    col1, col2 = st.columns(2)
    if contact_selected == "Prysm":

    #Prysm - Distribution
        with col1:
            fig = px.pie(relay7_data, values='Prysm', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Prysm - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Prysm - Rewards/Slot
        with col2:
            fig = px.bar(relrew7_data, x = 'relay', y = 'Prysm', color='relay', color_discrete_map=RELAYCOLOR, title='Prysm - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


    #---Lighthouse---
    col1, col2 = st.columns(2)
    if contact_selected == "Lighthouse":

    #Lighthouse - Distribution
        with col1:
            fig = px.pie(relay7_data, values='Lighthouse', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Lighthouse - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Lighthouse - Rewards/Slot
        with col2:
            fig = px.bar(relrew7_data, x = 'relay', y = 'Lighthouse', color='relay', color_discrete_map=RELAYCOLOR, title='Lighthouse - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


    #---Teku---
    col1, col2 = st.columns(2)
    if contact_selected == "Teku":

    #Teku - Distribution
        with col1:
            fig = px.pie(relay7_data, values='Teku', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Teku - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Teku - Rewards/Slot
        with col2:
            fig = px.bar(relrew7_data, x = 'relay', y = 'Teku', color='relay', color_discrete_map=RELAYCOLOR, title='Teku - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


    #---Nimbus---
    col1, col2 = st.columns(2)
    if contact_selected == "Nimbus":

    #Nimbus - Distribution
        with col1:
            fig = px.pie(relay7_data, values='Nimbus', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Nimbus - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Nimbus - Rewards/Slot
        with col2:
            fig = px.bar(relrew7_data, x = 'relay', y = 'Nimbus', color='relay', color_discrete_map=RELAYCOLOR, title='Nimbus - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")


    #---Lodestar---
    col1, col2 = st.columns(2)
    if contact_selected == "Lodestar":

    #Lodestar - Distribution
        with col1:
            fig = px.pie(relay7_data, values='Lodestar', names='relay', color='relay', color_discrete_map=RELAYCOLOR, title='Lodestar - Relay Distribution')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    #Lodestar - Rewards/Slot
        with col2:
            fig = px.bar(relrew7_data, x = 'relay', y = 'Lodestar', color='relay', color_discrete_map=RELAYCOLOR, title='Lodestar - BlockReward/Slot Grouped by Relay')
            st.plotly_chart(fig, use_container_width=True, sharing="streamlit")



st.markdown('Data provided by [blockprint](https://github.com/sigp/blockprint), [Relay API](https://flashbots.notion.site/Relay-API-Documentation-5fb0819366954962bc02e81cb33840f5) and [beaconcha.in](https://beaconcha.in/). Thank You:heart:')
st.markdown(':computer: [GitHub](https://github.com/kevinbogner/data-analysis-consensus-clients) and :bird:[Twitter](https://twitter.com/kevin_bogner)')