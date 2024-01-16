import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
import os

st.markdown('<p class="dashboard_title">Fidelización de<br>Riesgos Climáticos</p>', unsafe_allow_html = True)

api_key1 = st.secrets["OPENAI_API_KEY"]

api_key2 = os.getenv("OPENAI_API_KEY")

chat_model = ChatOpenAI(openai_api_key=api_key1)

template = "You area helpful saler of monthly suscriptions to climate insurances for Novus Clima Company. You know that save lifes and assets by insurance is like a be superheros in real time. You are welcoming customers and trying to sale insurance monthly basic by 10USD por person, medium by 50USD for cupples and large by 100USD for families and homes"
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
  ("system", template),
  ("human", human_template),
])

messages = chat_prompt.format_messages(text="Hi I am customer of Novus Clima the personal insurance but I want to know what could be improve my novus clima subscription")

result = chat_model.predict_messages(messages)

st.write(result.content)
