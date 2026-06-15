import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import streamlit as st
import pandas as pd
from database.connection import get_connection

st.title("Products Analytics Dashboard")

# Establish database connection to fetch data for the dashboard
conn = get_connection()

df = pd.read_sql("SELECT * FROM cln_products", conn)
st.subheader("Products Data")
st.dataframe(df)