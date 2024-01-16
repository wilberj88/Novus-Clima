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
    page_title = 'Novus Clima'
)





st.markdown('<p class="dashboard_title">Novus<br>Clima</p>', unsafe_allow_html = True)

col1, col2 = st.columns(2)

with col1:
    suits = st.selectbox(
        "How many suits do you have?",
        ("1", "2", "3", "4", "5"),
    )
    rooms = st.radio(
        "How many rooms do you have?",
        options=['10', '15','20', '25', '30', '35', '40', '45', '50'],
    )
    beds = st.selectbox(
        "How many beds do you have?",
        ("25", "50", "75", "100"),
    )

with col2:
    name = st.text_input('What is the name of your hotel?', '''
    ''')
    email = st.text_input('What is the email of the administrator?', '''
    ''')
    bank_account =  st.text_input('Type your bank account:', '''
    ''')
    phone =  st.text_input('Type your phone number', '''
    ''')
    a = st.selectbox('How many beds for staff:', ['25', '50', '75', '100', '200'])


b = st.selectbox('Monthly average expenditures by all the beds:', ['10.000€', '25.000€', '50.000€', '75.000€', '100.000€'])
c = st.selectbox('Do you have budget for ads?:', ['Yes', 'No'])

d = st.slider('How old are the locacies in years?', 0, 24)

st.subheader('ATENTOS')
col3, col4 = st.columns(2)

with col3:
    mood = st.selectbox(
        "What mood do you prefer for your virtual staff?",
        ("Elegant", "Friendly", "Formal", "Neutro", "Informal"),
    )
    channels = st.radio(
        "What channels do you want to use for confirmations?",
        options=['email', 'phone', 'twice'],
    )
    welcoming = st.selectbox(
        "What kind of welcoming do you prefer to offer?",
        ("Cold", "Neutro", "Warm"),
    )

with col4:
    suit_price = st.text_input('What is the day price of suits?', '''
    ''')
    room_price = st.text_input('What is the day price of the rooms?', '''
    ''')
    rentability_goal =  st.text_input('What is your rentability goal?', '''
    ''')
    target =  st.text_input('What is your target?', '''
    ''')
    manifiesto = st.selectbox('Do you have support manifiesto?', ['Yes', 'No'])


h = st.button('Crear Novus Hotel 🛏️ YA')

if h:
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    st.write('¡Novus Hotel en construcción! Accede a los MANDOS y ATENTOS de tu <<', name, '>> con el código de confirmación enviado a <<', email, '>>')
