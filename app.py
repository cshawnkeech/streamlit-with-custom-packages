import os
import sys
import streamlit as st

import add_path
from src.constants import KS_ALERTS_ENDPOINT

p = sys.path

cwd = os.getcwd()

st.write(f"Current Working Directory: {cwd}")


st.write(f"sys.path: {p}")

st.write(f"KS_ALERTS_ENDPOINT: {KS_ALERTS_ENDPOINT}")
