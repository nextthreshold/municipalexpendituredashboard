import pandas as pd 
import numpy as np 
import streamlit as st 
import matplotlib.pyplot as py
import plotly.express as px
 
st.header('Expenditure Of Pune Municpal Corporation for between years 2017-2021')
st.divider()
st.image('map.jpg',caption='Pune Municipal Corporation')


st.divider()

st.markdown('This webpage aims at providing a platform to the citizens to observe and analyse the expenditure of money that is supposed to be utilised for their service and welfare.')

st.markdown('### Demographics')
col1,col2,col3=st.columns(3)
col1.metric("### Population","4,436,000")
col2.metric("### Area sq.km","340.45")
col3.metric("### Budget of PMC INR","8,592 Crores")

st.divider()