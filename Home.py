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
from vega_datasets import data
    
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


st.markdown('<p class="dashboard_title">⛅ Novus Clima<br>Saving ♡ & 🏛️ <br>in Real Time</p>', unsafe_allow_html = True)


c1, c2, c3 =  st.columns(3)
with c1:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Monitoring TODAY</p>', unsafe_allow_html = True)
        st.subheader('Seattle Patterns')
        source = data.seattle_weather()
        
        scale = alt.Scale(
            domain=["sun", "fog", "drizzle", "rain", "snow"],
            range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
        )
        color = alt.Color("weather:N", scale=scale)
        
        # We create two selections:
        # - a brush that is active on the top panel
        # - a multi-click that is active on the bottom panel
        brush = alt.selection_interval(encodings=["x"])
        click = alt.selection_multi(encodings=["color"])
        
        # Top panel is scatter plot of temperature vs time
        points = (
            alt.Chart()
            .mark_point()
            .encode(
                alt.X("monthdate(date):T", title="Date"),
                alt.Y(
                    "temp_max:Q",
                    title="Maximum Daily Temperature (C)",
                    scale=alt.Scale(domain=[-5, 40]),
                ),
                color=alt.condition(brush, color, alt.value("lightgray")),
                size=alt.Size("precipitation:Q", scale=alt.Scale(range=[5, 200])),
            )
            .properties(width=550, height=300)
            .add_selection(brush)
            .transform_filter(click)
        )
        
        # Bottom panel is a bar chart of weather type
        bars = (
            alt.Chart()
            .mark_bar()
            .encode(
                x="count()",
                y="weather:N",
                color=alt.condition(click, color, alt.value("lightgray")),
            )
            .transform_filter(brush)
            .properties(
                width=550,
            )
            .add_selection(click)
        )
        
        chart = alt.vconcat(points, bars, data=source, title="Historic Seattle Weather: 2012-2015")
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    

with c2:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Alarming RIGH NOW</p>', unsafe_allow_html = True)
        st.subheader('Risk Dissasters Predictions')

with c3:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Preventing TOMORROW</p>', unsafe_allow_html = True)
        st.subheader('Best Practices')
    
