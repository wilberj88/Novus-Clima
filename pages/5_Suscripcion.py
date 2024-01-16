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
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os


if "symbols_list" not in st.session_state:
    st.session_state.symbols_list = None
    
st.set_page_config(
    layout = 'wide',
    page_title = 'Novus Clima'
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


title_col, emp_col, btc_col, eth_col, xmr_col, sol_col, xrp_col = st.columns([1.3,0.2,1,1,1,1,1])

with title_col:
    st.markdown('<p class="dashboard_title">Suscripción de<br>Riesgos Climáticos</p>', unsafe_allow_html = True)




api_key1 = st.secrets["OPENAI_API_KEY"]

api_key2 = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key1)

template = "You area helpful saler of monthly suscriptions to climate insurances for Novus Clima Company. You know that save lifes and assets by insurance is like a be superheros in real time. You are welcoming customers and trying to sale insurance monthly basic by 10USD por person, medium by 50USD for cupples and large by 100USD for families and homes"
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
  ("system", template),
  ("human", human_template),
])

messages = chat_prompt.format_messages(text="Hi I would like to know what do you do in Novus Clima")

result = chat_model.predict_messages(messages)

st.write(result.content)
