"""
Detect file structure for Streamlit app
discover method for adding custom module to path
"""
import os
import sys
import streamlit as st
import add_path

# import a constant
from src.constants import KS_ALERTS_ENDPOINT
# import a function
from src.restore import restore_bounds

p = sys.path
cwd = os.getcwd()

st.write(f"Current Working Directory: {cwd}")
st.write(f"sys.path: {p}")

# display imported constant
st.write(f"KS_ALERTS_ENDPOINT: {KS_ALERTS_ENDPOINT}")


# use imported function
bounds = restore_bounds()
# display df created from restored function
st.dataframe(bounds)
