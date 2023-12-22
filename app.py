import streamlit as st
import pandas as pd
import plotly.express as px

# Membaca CSV
df = pd.read_csv("my_data.csv")

# Menampilkan data frame
st.write("Data Frame:", df)

# Membuat diagram pie chart dengan plotly
fig = px.pie(df, names='kategori', values='jumlah', title='Pie Chart Aspek Performa')
st.plotly_chart(fig)
