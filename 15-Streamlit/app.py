'''
Streamlit is an open-source app framework for Machine Learning and Data Science 
projects. It allows you to create beautiful web applications for your machine 
learning and data science projects with simple Python scripts.

streamlit run app.py
'''

import streamlit as st
import pandas as pd
import numpy as np

#title of application
st.title('Streamlit App')

#display simple text
st.write('Hello, World')

#create a dataframe
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

#display dataframe
st.write(df)

#create a line chart
chart=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart)