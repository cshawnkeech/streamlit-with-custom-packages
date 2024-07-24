"""
Detect file structure for Streamlit app
discover method for adding custom module to path
"""
import os
import sys
import streamlit as st
import add_path

from src.constants import KS_ALERTS_ENDPOINT

from src.restore import restore_bounds


bounds = restore_bounds()
st.dataframe(bounds)

p = sys.path

cwd = os.getcwd()

st.write(f"Current Working Directory: {cwd}")

st.write(f"sys.path: {p}")

st.write(f"KS_ALERTS_ENDPOINT: {KS_ALERTS_ENDPOINT}")
