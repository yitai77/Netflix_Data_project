import streamlit as st
import common

st.title("Data")

st.data = pd.read_csv

st.usa_data = data[data['country'] == 'United States']
st.usa_data
