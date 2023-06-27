import streamlit as st
import common

st.title("Data")

st.dataframe(common.get_sales(),
             use_container_width=True,
             hide_index=True)
