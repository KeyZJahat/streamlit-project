import streamlit as st
import pandas as pd

# Title
st.title("Elements Demo")

# Dataframe Section
st.subheader("Dataframe")
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 37, 45],
    'Occupation': ['Engineer', 'Doctor', 'Artist', 'Chef']
})

st.dataframe(df)
