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
    st.markdown('<p class="dashboard_title">Monitorización de<br>Riesgos Climáticos</p>', unsafe_allow_html = True)

with btc_col:
    with st.container(border=True):
        st.markdown(f'<p class="btc_text">Vidas<br></p><p class="price_details">34060.92</p>', unsafe_allow_html = True)
       
with eth_col:
    with st.container(border=True):
        #eth_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=ETH/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="eth_text">Activos<br></p><p class="price_details">1789.26</p>', unsafe_allow_html = True)

with xmr_col:
    with st.container(border=True):
        #xmr_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XMR/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xmr_text">Infraestructura<br></p><p class="price_details">162.1</p>', unsafe_allow_html = True)

with sol_col:
    with st.container(border=True):
        #sol_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=SOL/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="sol_text">Viviendas<br></p><p class="price_details">32.27</p>', unsafe_allow_html = True)

with xrp_col:
    with st.container(border=True):
        #xrp_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XRP/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xrp_text">Cultivos<br></p><p class="price_details">0.5449</p>', unsafe_allow_html = True)


params_col, chart_col, data_col = st.columns([0.7,1.6,1.1])

with params_col:
    
    with st.form(key = 'params_form'):
        
        st.markdown(f'<p class="params_text">PARÁMETROS', unsafe_allow_html = True)
                
        listado_modos = ['Conservador', 'Precavido', 'Arriesgado']
        modo = st.selectbox('Selecciona un modo financiero', listado_modos, key = 'modo')

        listado_edad_retiro = ['50 años','55 años','60 años','65 años','70 años']
        retiro = st.selectbox('¿A qué edad deseas pensionarte?', listado_edad_retiro, key = 'retiro')
        
        estilo_de_vida_retiro = st.selectbox('Estilo de vida', ['Popular', 'Clase Media', 'Clase Media Alta', 'Clase Alta'], key = 'interval_selectbox')
        ahorro = st.number_input('Meta Ahorros USD millones', min_value = 10, max_value = 500, value = 365, step = 1, key = 'period_no_input')
        a = st.slider("Indica cuánto en promedio ganas al mes en dólares", 0, 10000, 500)
        st.divider()
        update_chart = st.form_submit_button('Update chart')
        
        if update_chart:
           

            with chart_col:

                with st.container(border=True):
                    fig1 = go.Figure(data=[go.Sankey(
                        node = dict(
                            pad = 15,
                            thickness = 20,
                            line = dict(color = "black", width = 0.5),
                            label = ["Gastos Mensuales", "Necesidades", "Entretenimiento", "Inversiones", "Vivienda", "Estudio", "Alimentación", "Transporte", "Entretenimiento", "Viajes", "Acciones", "Activos", "Criptomonedas", "Bonos"],
                            color = "red"
                            ),
                        link = dict(
                        source = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
                        target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                        value = [50, 20, 30, 10, 20, 10, 22, 22, 10, 14, 10, 10, 10]
                        ))])
                    
                    fig1.update_layout(title_text="Usos promedio de tu presupuesto💰", font_size=10)
                    st.plotly_chart(fig1, theme="streamlit")
                    df = pd.DataFrame(
                        {
                            "name": ["Roadmap", "Extras", "Issues"],
                            "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
                            "stars": [random.randint(0, 1000) for _ in range(3)],
                            "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
                        }
                    )
                    st.dataframe(
                        df,
                        column_config={
                            "name": "App name",
                            "stars": st.column_config.NumberColumn(
                                "Github Stars",
                                help="Number of stars on GitHub",
                                format="%d ⭐",
                            ),
                            "url": st.column_config.LinkColumn("App URL"),
                            "views_history": st.column_config.LineChartColumn(
                                "Views (past 30 days)", y_min=0, y_max=5000
                            ),
                        },
                        hide_index=True,
                    )
                       
                    
            with data_col:
                data_df = pd.DataFrame(
                    {
                        "name": ["Mando", "Atento", "Campus"],
                        "apps": [
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
                            "https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
                        ],
                        "sales": [
                            [0, 4, 26, 80, 100, 40],
                            [80, 20, 80, 35, 40, 100],
                            [10, 20, 80, 80, 70, 0],
                        ],
                        "Performance": [200, 550, 1000],
                    }
                )                
                st.dataframe(
                    data_df,
                    column_config={
                        "name": "Tech Required",
                        "apps": st.column_config.ImageColumn(
                            "Preview Image", help="Streamlit app preview screenshots"
                        ),
                        "sales": st.column_config.BarChartColumn(
                            "Sales (last 6 months)",
                            help="The sales volume in the last 6 months",
                            y_min=0,
                            y_max=100,
                        ),
                        "Performance": st.column_config.ProgressColumn(
                            "Performance",
                            help="The sales volume in USD",
                            format="$%f",
                            min_value=0,
                            max_value=1000,
                        ),
                    },
                    hide_index=True,
                )
                st.caption("By Wilber Jimenez Hernandez")
                
               
