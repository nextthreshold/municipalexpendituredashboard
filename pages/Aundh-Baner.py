import streamlit as st

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt   
import plotly.graph_objects as go
import plotly.express as px

#REading the data file 
df=pd.read_csv("Aundh-Baner.csv")

#calcualting  the total amount spent 
total_amount_in_term=df['Amount'].sum()

#counting the number of wards
num_unique_values = df['Ward No.'].nunique()

amount_by_year = df.groupby('Year')['Amount'].sum().reset_index()
#print(amount_by_year)

#amount by item
amount_by_item = df.groupby('Expense Code')['Amount'].sum().reset_index()

max_exp = amount_by_item[amount_by_item['Amount'] == amount_by_item['Amount'].max()]



col1,col2=st.columns(2)
with col1:
    col1.metric("Number of Wards",num_unique_values)

#add vertical divider


with col2:
    col2.metric("INR spent in 5 Years","{:,}".format(round(total_amount_in_term,2)))



st.divider()
st.subheader('Maximum Amount of Fund in 5 Years was Spent on')
st.table(max_exp)

st.subheader('Classification of the Funds Expended in the region')
figure=px.pie(amount_by_item, values='Amount', names='Expense Code', title='Classification of Utilised Funds')
st.plotly_chart(figure)

st.divider()



st.subheader('Yearwise Expenditure in the Region')
st.markdown("This chart presents the total amount of funds in Rupees Expended in the Region")
fig1=px.bar(amount_by_year,x='Year', y='Amount',title='Annual Expenditure')
st.plotly_chart(fig1)

st.divider()

st.header("Classification of Expenditures in the Region")
st.markdown("This chart displays the classification of funds spent by the corporation in a particualr year")
year=st.selectbox('Select Year',df['Year'].unique())

if st.button('Display Classification of Amount'):
    filtered_data = df[df['Year'] == year]
    profit_by_item = filtered_data.groupby('Expense Code')['Amount'].sum().reset_index()
    fig3=px.bar(filtered_data,x='Expense Code',y='Amount')
    st.plotly_chart(fig3)

