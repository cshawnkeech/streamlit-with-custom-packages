"""
Detect file structure for Streamlit app
discover method for adding custom module to path
"""
import os
import sys
import streamlit as st

from add_path import add_dir_to_path

from src.constants import KS_ALERTS_ENDPOINT

add_dir_to_path(os.getcwd())

p = sys.path

cwd = os.getcwd()

st.write(f"Current Working Directory: {cwd}")


st.write(f"sys.path: {p}")

st.write(f"KS_ALERTS_ENDPOINT: {KS_ALERTS_ENDPOINT}")
