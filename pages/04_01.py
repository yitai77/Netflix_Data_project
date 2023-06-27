import streamlit as st
import common
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

Korean = common.get_ko_data()

rating_counts = Korean['rating'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,6))
ax.pie(rating_counts, labels=rating_counts.index,autopct='%1.1f%%', colors=['skyblue', 'limegreen', 'orange', 'red', 'purple'])

ax.set_title('Distribution of Top 10 Ratings for Netflix Content in South Korea')

st.pyplot(fig)