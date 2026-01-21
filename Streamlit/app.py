import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Hello Streamlit")

# Display a single text
st.write("This is a simple text")

# Create a simple DataFrame
df = pd.DataFrame({
    "first_column": [1, 2, 3, 4],
    "second_column": [10, 20, 30, 40]
})

# Display the DataFrame
st.write("Here is the dataframe")
st.write(df)