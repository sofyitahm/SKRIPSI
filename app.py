import streamlit as st
import pandas as pd
import plotly.express as px

# Membaca CSV
df = pd.read_csv("my_data.csv")

# Menampilkan data frame
st.write("Data Frame:", df)

# Membuat diagram pie chart untuk semua kolom
for column in df.columns:
    # Menggunakan try-except untuk menangani kolom yang tidak dapat diplot sebagai pie chart
    try:
        fig = px.pie(df, names=column, title=f"Pie Chart for {column}")
        st.plotly_chart(fig)
    except:
        st.warning(f"Tidak dapat membuat pie chart untuk kolom {column}.")
