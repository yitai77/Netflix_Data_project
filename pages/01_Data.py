import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

st.title("Data")

st.data = pd.read_csv

st.usa_data = data[data['country'] == 'United States']
st.usa_data
