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
# Data Editor Section (Editable dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df)

# Static Table Section
st.subheader("Static Table")
st.table(df)

# Metrics Section
st.subheader("Metrics")

st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value=round(df['Age'].mean(), 1))
