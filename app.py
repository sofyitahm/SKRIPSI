import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca CSV
df = pd.read_csv("my_data.csv")

# Menampilkan data frame
st.write("Data Frame:", df)

# Extracting data from the DataFrame
kategori = df['kategori']
jumlah = df['jumlah']

# Membuat diagram pie chart dengan matplotlib
fig1, ax1 = plt.subplots()
ax1.pie(jumlah, labels=kategori, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Menampilkan diagram pie chart menggunakan streamlit
st.pyplot(fig1)
