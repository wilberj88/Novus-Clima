import streamlit as st
import requests
from streamlit_echarts import st_echarts
import pandas as pd
from lightweight_charts.widgets import StreamlitChart
import random
import pandas as pd
import time
import datetime
import plotly.graph_objects as go
from vega_datasets import data
import altair as alt
from country_pollutants import pie_plot, observations
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_dark"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "146090ad17fa8843bc9eca97c53926b4"
    
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

st.sidebar.header("Data Sources")
st.sidebar.info(
    """The raw data is taken from [Kaggle](https://www.kaggle.com/datasets/hasibalmuzdadid/global-air-pollution-dataset) and 
    originally scraped from [here](https://www.elichens.com/)!"""
    )

st.markdown('<p class="dashboard_title">⛅ Novus Clima<br>Saving ♡ & 🏛️ <br>in Real Time</p>', unsafe_allow_html = True)

with st.expander("The Challenge"):
    st.header("Detoxify Cities 💪")
    st.subheader("Diagnosis context: How is the Air We Breathe?")
    st.markdown("*Visualizing Global Air Pollution Levels*")

# =========================
# Load the data
    df = pd.read_csv('air-pollution.csv', encoding='latin-1', index_col=0)


# ============== PLOTS ==============

    st.subheader("About Air Pollution")
    st.write("""Air Pollution is contamination of the indoor or outdoor environment by any chemical,
                 physical, or biological agent that modifies the natural characteristics of the atmosphere.""")

# ---- AQI on World Map ----
    st.subheader("Global Air Quality Index (AQI) ☁")
    st.info("""The below world map shows how polluted the air currently is or
            how polluted it is forecast to become. As air pollution levels rise,
            so does the AQI, along with the associated public health risk.""")
    
    world_aqi = pd.DataFrame(df.groupby("country")["aqi_value"].max())
    
    fig = go.Figure(data=go.Choropleth(
        locations = df['country_code'].values.tolist(),
        z = world_aqi['aqi_value'].values.tolist(),
        text = df.index,
        colorscale = 'matter',  #Color_options: magenta, Agsunset, Tealgrn
        autocolorscale=False,
        marker_line_color='darkgray',
        marker_line_width=1,
        colorbar_title = 'AQI<br>Value',
    ))
    
    fig.update_layout(
        geo=dict(
            showframe=True,
            showcoastlines=False,
            projection_type='natural earth'
        ),
        height=450,
        margin={"r":10,"t":0,"l":10,"b":50}
    )
    
    st.plotly_chart(fig)
    
    
    # =========================
    # ---- Exploring countries with diff. air pollutants' levels  ----
    
    st.divider()
    st.subheader("Countries with air pollutants' levels 🏭")
    tab1, tab2, tab3, tab4 = st.tabs(["CO", "O3", "NO2", "PM2.5"])
    
    with tab1:
        st.info("""Carbon Monoxide is a colorless and odorless gas.
                Outdoor, it is emitted in the air above all by cars, trucks and
                other vehicles or machineries that burn fossil fuels.
                Such items like kerosene and gas space heaters, gas stoves also
                release CO affecting indoor air quality.""")
        
        st.markdown('#### Explore the air quality of CO for different countries to know more!')
        choose_catg = st.selectbox('Select an air quality type 👇',
        ('Good', 'Moderate', 'Unhealthy for Sensitive Groups'))
    
        pie_plot(category='co_aqi_category', catg_type=choose_catg,
                 catg_aqi='co_aqi_value', aqi_label='CO',
                 title='CO Levels Globally')
    
    with tab2:
        st.info("""The Ozone molecule is harmful for outdoor air quality (if outside of the ozone layer).
                Ground level ozone can provoke several health problems like chest pain,
                coughing, throat irritation and airway inflammation.""")
        
        st.markdown('#### Explore the air quality of O3 for different countries to know more!')
        choose_catg = st.selectbox('Select an air quality type 👇',
        ('Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy'))
    
        pie_plot(category='ozone_aqi_category', catg_type=choose_catg,
                 catg_aqi='ozone_aqi_value', aqi_label='O3',
                 title='Ozone O3 Levels Globally', color=px.colors.sequential.haline)
        
    with tab3:
        st.info("""Nitrogen Dioxide is introduced into the air by natural phenomena
                like entry from stratosphere or lighting. At the surface level, however,
                NO2 forms from cars, trucks and buses emissions, power plants and
                off-road equipment. Exposure over short periods can aggravate
                respiratory diseases, like asthma.""")
        
        st.markdown('#### Explore the air quality of NO2 for different countries to know more!')
        choose_catg = st.selectbox('Select an air quality type 👇',
        ('Good', 'Moderate'))
    
        pie_plot(category='no2_aqi_category', catg_type=choose_catg,
                 catg_aqi='no2_aqi_value', aqi_label='NO2',
                 title='NO2 Levels Globally', color=px.colors.sequential.haline)
    
    with tab4:
        st.info("""Atmospheric Particulate Matter, also known as atmospheric aerosol particles,
                are complex mixtures of small solid and liquid matter that get into the air.
                If inhaled they can cause serious heart and lungs problem.""")
        
        st.markdown('#### Explore the air quality of PM2.5 for different countries to know more!')
        choose_catg = st.selectbox('Select an air quality type 👇',
        ('Good', 'Moderate', 'Unhealthy for Sensitive Groups', 'Unhealthy', 'Very Unhealthy', 'Hazardous'))
    
        pie_plot(category='pm2_5_aqi_category', catg_type=choose_catg,
                 catg_aqi='pm2_5_aqi_value', aqi_label='PM2.5',
                 title='PM2.5 Levels Globally')
    
    # Insights for above pie plots
    observations()
    
    # =========================
    # ---- 8 Countries whose top 15 cities shows diff. air pollutants' levels  ----
    
    def plot_bar(coc='', aqi=''):
        """Plots a Seaborn barplot for ."""
    
        # Filter data for specific country
        df_coc = df[df['country_code'] == coc]
    
        # Filter data for pollutant values
        cont_plot = pd.DataFrame(df_coc.groupby("city")[aqi].max())
    
        sns.set_theme(style='dark')
        plt.style.use('dark_background')
        sns_fig = plt.figure(figsize=(40, 20))
        
        sns.barplot(x=cont_plot.index,
                    y=cont_plot[aqi].values,
                    order=cont_plot.sort_values(aqi,ascending=False).index[:15],
                    palette=("cool"))
        st.pyplot(sns_fig)
    
    st.divider()
    st.subheader('Represents Maximum Values from 8 Countries📊')
    
    choose_coc = st.selectbox('Select a Country Code 👇',
        ('USA', 'IND', 'CHN', 'MYS', 'IDN', 'ZAF', 'RUS', 'BRA'))
    
    st.success("""📌 USA: United States, IND: India, CHN: China,
               MYS: Malaysia, IDN: Indonesia, ZAF: South Africa,
               RUS: Russia, BRA: Brazil""")
    
    col1, col2 = st.columns(2, gap='medium')
    
    with col1:
        st.markdown(':blue[Top 15 Cities with max values of **CO**]')
        plot_bar(coc=choose_coc, aqi='co_aqi_value')
    
    with col2:
        st.markdown('Top 15 Cities with max values of **O3**')
        plot_bar(coc=choose_coc, aqi='ozone_aqi_value')
    
    
    col3, col4 = st.columns(2, gap='medium')
    
    with col3:
        plot_bar(coc=choose_coc, aqi='no2_aqi_value')
        st.markdown('Top 15 Cities with max values of **NO2**')
    
    with col4:
        plot_bar(coc=choose_coc, aqi='pm2_5_aqi_value')
        st.markdown(':blue[Top 15 Cities with max values of **PM2.5**]')
    





with st.expander("The Solution"):
    st.header("Lead Cities to build their own Novus Clima 🏆 - Seattle`s case")
    
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Historic PATTERNS</p>', unsafe_allow_html = True)
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
    
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Monitoring TODAY</p>', unsafe_allow_html = True)
        current_time = time.ctime()
        st.subheader("Automated Report by LLM (Open AI - Crew AI) 🤖")
        st.write("""
        
        - Today's temperature in Seattle is forecasted to be warmer than yesterday, with a high of 52°F and a low of 43°F. 
        - There are chances of rain showers throughout the day. 
        - After a brief period of spring-like weather, winter conditions have returned with some lowland snow in parts of western Washington.
        - There are advisories for small crafts and beach hazards.
        - The weather forecast predicts the snow to turn into rain, followed by sunshine.
        """
        )
        st.subheader("Real time data By Open Weather API At:")
        st.write(current_time)
        sity = "Seattle"
        URL1 = BASE_URL + "q=" + sity + "&appid=" + API_KEY
        
        # HTTP request
        if sity:
           response = requests.get(URL1)
        
        # checking the status code of the request
        if response.status_code == 200:
           # getting data in the json format
           data = response.json()
           # getting the main dict block
           main = data['main']
          # getting temperature
           temperature = main['temp']
           # getting the humidity
           humidity = main['humidity']
           # getting the pressure
           pressure = main['pressure']
           # weather report
           report = data['weather']
          
        st.write(main)
        st.write(temperature)
        st.write(humidity)
        st.write(pressure)
        st.write(report)

        
        st.header("Risks in Seattle rigth now")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Wildfire", "57%", "14%")
        col2.metric("Flooding", "25%", "-18%")
        col3.metric("Drought", "89%", "13%")
        col4.metric("Hurricanes", "45%", "18%")
        st.header("OPPORTUNITIES in Seattle rigth now")
        col5, col6, col7, col8 = st.columns(4)
        col5.metric("FIRE EXTINGUISHERS", "97%", "14%")
        col6.metric("WATER WUMPS", "45%", "-18%")
        col7.metric("KAYAKS", "85%", "13%")
        col8.metric("SHELTERS", "35%", "18%")

    
    
    
    
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Alarming RIGH NOW</p>', unsafe_allow_html = True)
        st.subheader('Risk Dissasters Predictions')
    
    
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Preventing TOMORROW</p>', unsafe_allow_html = True)
        st.subheader('Best Practices')
    
