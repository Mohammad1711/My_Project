import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

df = pd.read_csv('vehicles_us.csv')  
st.header('Car Advertisement Data Analysis')
st.subheader('Distribution of Car Prices')
fig = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig)

st.subheader('Distribution of Car Prices')
fig = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig)

st.subheader('Price vs Model Year')
fig2 = px.scatter(df, x='model_year', y='price', color='condition', title='Price vs Model Year by Condition')
st.plotly_chart(fig2)


low_mileage = st.checkbox('Show only low mileage cars (<= 50,000 miles)')

if low_mileage:
    df = df[df['odometer'] <= 50000]


st.subheader('Distribution of Car Prices')
fig = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig)

st.subheader('Price vs Model Year')
fig2 = px.scatter(df, x='model_year', y='price', color='condition', title='Price vs Model Year by Condition')
st.plotly_chart(fig2)
