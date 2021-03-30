#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 10:05:50 2021

@author: chocz
"""

import pandas as pd 
import numpy as np 
import requests 
import json
import re
import datetime
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image
import time
import matplotlib as plt





st.title('Marketing Promotion Strategies')

st.sidebar.header('Select the type of model')
add_selectbox = st.sidebar.selectbox(
    "Choose a model",
    ("Last Touch Attribution","Linear Model", "First Touch Attribution",
     "U Shape Attribution", "Time Decay Model")
)


lta = pd.read_csv('lta.csv')
fta = pd.read_csv('fta.csv')
lm = pd.read_csv('lm.csv')
ushape = pd.read_csv('ushape.csv')
timedecay = pd.read_csv('timedelta.csv')
roi =pd.read_csv('roi.csv')

lta1 = lta.iloc[150:200]
fta1 = fta.iloc[150:200]
lm1 = lm.iloc[150:200]
ushape1 = ushape.iloc[150:200] 
timedecay1 = timedecay.iloc[150:200]

campaign_idx = range(1, 50)

if add_selectbox == "Last Touch Attribution":
    fig = px.bar(lta1, x="Unnamed: 0", y="Value", title = "Last Touch Attribution")
    fig.update_xaxes(title = "Return Per Impression")
    fig.update_yaxes(title = "Campaign ID")
    st.plotly_chart(fig)
    
    fig = px.line(roi, x="pitches", y="lta", title='Last Touch Attribution ROI')
    fig.update_yaxes(title ='LTA ROI')
    fig.update_xaxes(title ='Pitch')
    st.plotly_chart(fig)



elif add_selectbox == "Linear Model":
    fig = px.bar(lm1, x="Unnamed: 0", y="Value", title = "Linear Model")
    fig.update_xaxes(title = "Return Per Impression")
    fig.update_yaxes(title = "Campaign ID")
    st.plotly_chart(fig)
    
    fig = px.line(roi, x="pitches", y="lm", title= 'Linear Model ROI')
   
    fig.update_xaxes(title ='Pitch')
    fig.update_yaxes(title ='LM ROI')
    st.plotly_chart(fig)
    

elif add_selectbox == "First Touch Attribution":
    fig = px.bar(fta1, x="Unnamed: 0", y="Value", title = "First Touch Attribution")
    fig.update_xaxes(title = "Return Per Impression")
    fig.update_yaxes(title = "Campaign ID")
    st.plotly_chart(fig)
    
    fig = px.line(roi, x="pitches", y="fta", title='First Touch Attribution ROI')
    fig.update_yaxes(title ='FTA ROI')
    fig.update_xaxes(title ='Pitch')
    st.plotly_chart(fig)

elif add_selectbox == "U Shape Attribution":
    fig = px.bar(ushape1, x="Unnamed: 0", y="Value", title ="U Shape Attribution")
    fig.update_xaxes(title = "Return Per Impression")
    fig.update_yaxes(title = "Campaign ID")
    st.plotly_chart(fig)
    
    fig = px.line(roi, x="pitches", y="lm", title='U shape Attribution ROI')
    fig.update_yaxes(title ='U Shape ROI')
    fig.update_xaxes(title ='Pitch')
    st.plotly_chart(fig)
    
elif add_selectbox == "Time Decay Model":
    fig = px.bar(timedecay1, x="Unnamed: 0", y="Value", title = "Time Decay Model")
    fig.update_xaxes(title = "Return Per Impression")
    fig.update_yaxes(title = "Campaign ID")
    st.plotly_chart(fig)
    
    fig = px.line(roi, x="pitches", y="timedecay", title='Time Decay Model ROI')
    fig.update_yaxes(title ='Time Decay ROI')
    fig.update_xaxes(title ='Pitch')
    st.plotly_chart(fig)
