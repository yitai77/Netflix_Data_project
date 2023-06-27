import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def get_sales():
    return pd.read_csv("./netflix1.csv")

def page_config():
    st.set_page_config(
        page_title="Netflix : South Korea and United States",
        page_icon="🎥",
    )
