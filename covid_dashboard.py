# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:45:39 2021

@author: cansu
"""

import pandas as pd
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots

time_data = pd.read_csv('C:/Users/cansu/Desktop/streamlit_dashboard/full_grouped.csv')
country_data = pd.read_csv('C:/Users/cansu/Desktop/streamlit_dashboard/country_wise_latest.csv')
country_data = country_data.melt(id_vars = ['Country/Region'], value_vars = ['Confirmed', 'Deaths', 'Recovered', 'Active'],
           var_name ='Status', value_name ='Number')

st.sidebar.title("Covid-19 Visualization")
st.sidebar.markdown("This application is for visualizing the Covid-19 data.")

sidebar_select = st.sidebar.radio("Graphs", ('Covid-19 Country Wise', 'Covid-19 Date and Country Wise'))

if sidebar_select == 'Covid-19 Country Wise':
    st.title("Total Confirmed/Deaths/Recovered/Active Numbers for Countries")
    st.markdown("You can select bars to remove from the chart.")
    select = st.selectbox('Select a Country', country_data['Country/Region'])
    country_data = country_data[country_data['Country/Region'] == select]
    if not st.checkbox('Hide Graph', False, key=1):
        country_graph = px.bar(country_data, x='Status', y='Number',
        labels = {'Number of cases':'Number of cases in %s' % (select)}, color = 'Status')
        st.plotly_chart(country_graph)
    
if sidebar_select == 'Covid-19 Date and Country Wise':
    st.title("Confirmed/Deaths/Recovered/Active Trends")
    st.markdown("You can select lines to remove from the chart.")
    select1 = st.selectbox('Select a Country', time_data['Country/Region'])
    date_data = time_data[time_data['Country/Region'] == select1]
    if not st.checkbox('Hide Graph', False, key=1):
        fig = make_subplots(rows = 1, cols = 1)
        fig.add_scatter(x = date_data['Date'], y = date_data['Confirmed'], name = 'Confirmed', mode = 'lines')
        fig.add_scatter(x = date_data['Date'], y = date_data['Deaths'], name = 'Deaths', mode = 'lines')
        fig.add_scatter(x = date_data['Date'], y = date_data['Recovered'], name = 'Recovered', mode = 'lines')
        fig.add_scatter(x = date_data['Date'], y = date_data['Active'], name = 'Active', mode = 'lines')
        st.plotly_chart(fig, use_container_width=True)
