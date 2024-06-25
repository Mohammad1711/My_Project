import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

file_path = './vehicles_us.csv'
df = pd.read_csv(file_path)

st.header('This is a header with a divider')
st.header('this is test')