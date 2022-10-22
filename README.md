# 💾Data Analysis of Consensus Clients

This project is created as part of the third cohort of the [Ethereum Protocol Fellowship (EPF)](https://github.com/eth-protocol-fellows/cohort-three/blob/master/program-guide/program-details.md).

The aim is to provide a **Data Analysis of the Consensus Clients landscape to statistically identify inconsistency, seeking to improve the Consensus Layer.**

## Overview

💾 **Check Out the Website: https://kevinbogner-data-analysis-consensus-clients-app-lz484x.streamlitapp.com/. Still super early stage.**

For now, the primary sources of the data are [blockprint](https://github.com/sigp/blockprint) for client data and https://beaconcha.in/ for reward data.


## Journal Backlog
:sparkler: **Detailed Research & Development Process: https://github.com/eth-protocol-fellows/cohort-three/tree/master/notes/kevinbogner**.

**[10/22/2022]**
- [Wrote a script](https://user-images.githubusercontent.com/114221396/197349383-831a1bac-5b35-4704-ac91-b7947e581126.png) to automize the .csv file creation.
- Reduced the amount of required .csv files to make the website more lightweight.
- Thinking about how I want to proceed: Mid-term, I want to group the data in different timeframes to allow users time-specific drill-downs. Long-term, I want to publish the data through a Twitterbot with daily reports.

**[10/21/2022]**
- Fetched [data of Clients and Relays](https://user-images.githubusercontent.com/114221396/197228380-c0a6eb72-f5b9-421b-a72a-1afcfeb617f8.png).
- [Created Dropdown](https://user-images.githubusercontent.com/114221396/197228617-374b8e22-3650-47f6-a8b0-6b6b67a3f2c9.png) to display Client data.
- Added [Dataset](https://user-images.githubusercontent.com/114221396/197270088-5a9d1297-b227-452f-9977-74c0be3abf73.png) of 'Last 7 Days'.

**[10/19/2022]**
- Published [Dev Update #2](https://hackmd.io/@lODlsf2CR9uWlyIyEdjjPQ/SkSBLnG7i).

**[10/18/2022]**
- Adding new charts to the Website.

**[10/17/2022]**
- Creating [visualization](https://user-images.githubusercontent.com/114221396/196202723-77851bae-bf00-4b4e-8e17-33e965782025.png) with https://plotly.com/graphing-libraries/
- Deployed the Website at https://kevinbogner-data-analysis-consensus-clients-app-lz484x.streamlitapp.com/

**[10/16/2022]**
- Pivot to https://www.python.org/ and https://streamlit.io/.
- [Visualize data](https://user-images.githubusercontent.com/114221396/196051309-7abcb35f-db99-4a3c-8031-b48254489724.png).

**[10/15/2022]**
- [Tables](https://user-images.githubusercontent.com/114221396/195984206-9690965b-7046-459f-ae15-1fcc1a41af41.png) displayed in React.
- Next Steps: Visualize Tables and Automate Data Import.
