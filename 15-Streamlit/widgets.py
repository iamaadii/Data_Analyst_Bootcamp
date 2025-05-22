import streamlit as st
import pandas as pd

st.title('Streamlit text input')

name=st.text_input('Enter your name : ')
age = st.slider('Select your age',0,100,24)

options=['C','C++','Java','Python']
choice=st.selectbox("Choose your favourite programming language : ",options)

if name:
    st.write(f'Your name is {name}')
    
st.write(f'Your age is {age}')
st.write(f'You selected {choice}')

uploaded_file=st.file_uploader('Choose a csv file',type='csv')
if uploaded_file:
    df=pd.DataFrame(uploaded_file)
    st.write(df)