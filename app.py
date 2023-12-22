import streamlit as st
import pandas as pd
 
st.write("""
# My first app
Hello *world!*
I will make a PieChart wuhu
""")
 
import streamlit as st
import pandas as pd

# Membaca CSV
df = pd.read_csv("my_data.csv")

# Menampilkan data frame
st.write("Data Frame:", df)

# Memilih kolom-kolom yang ingin digunakan untuk pie chart
selected_columns = st.multiselect("Pilih kolom untuk Pie Chart", df.columns)

# Memeriksa apakah ada kolom yang dipilih
if selected_columns:
    # Menampilkan diagram pie chart
    st.pie_chart(df[selected_columns])
else:
    st.warning("Pilih setidaknya satu kolom untuk membuat pie chart.")

