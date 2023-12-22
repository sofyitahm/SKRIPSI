import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Membaca CSV
df = pd.read_csv("my_data.csv")

# Menampilkan data frame
st.write("Data Frame:", df)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=kategori, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
