import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


st.title("US-Data")

#''type' 열 기준으로 데이터 분류
sk_data_counts = sk_data['type'].value_counts()

#색상 설정
colors = ['violet', 'mistyrose']

#도덧 차트 그리기
fig, ax = plt.subplots()
ax.pie(sk_data_counts, labels=sk_data_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white', 'width':0.7}, colors = colors)
ax.axis('equal')
ax.set_title('Netflix Shows in the South Korea')

st.pyplot(fig)