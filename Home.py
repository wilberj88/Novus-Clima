import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import random
import pandas as pd
import time
from datetime import time
import plotly.graph_objects as go
    
st.set_page_config(
    layout = 'wide',
    page_title = '⛅ Novus Clima'
)

st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
    </style>
    """, unsafe_allow_html = True
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)


st.markdown('<p class="dashboard_title">⛅ Novus Clima<br>Saving ♡ & 🏛️ in Real Time</p>', unsafe_allow_html = True)


c1, c2, c3 =  st.columns(3)
with c1:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Monitoring<br></p>', unsafe_allow_html = True)
    

with c2:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Alarming<br></p>', unsafe_allow_html = True)

with c3:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Preventing<br></p>', unsafe_allow_html = True)
    
