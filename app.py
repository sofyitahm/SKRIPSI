import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("my_data.csv")

st.write("""
#Diagram Garis
""")
st.line_chart(df)

st.write("""
#Diagram Batang
""")
st.bar_chart(df)
