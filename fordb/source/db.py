# import package
import streamlit as st 
import plotly.express as px 
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# streamlit run db.py

#KONFIGURASI HALAMAN
st.write("""# My first app Hello *world!*""")
st.set_page_config(
  page_title = "titanic!", 
  page_icon = "?", # emoji ikon untuk ikon tab, bisa dengan "random"
  layout = "wide", #centered atau #wide
)