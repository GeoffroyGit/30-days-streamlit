import streamlit as st
import pandas as pd
import numpy as np



st.header('Line chart')

n_data = st.slider('How big do you want your chart?', 3, 100, 15)

chart_data = pd.DataFrame(
     np.random.randn(n_data, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
