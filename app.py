import streamlit as st
import os
import sys

p = sys.path

cwd = os.getcwd()

st.write(f"Current Working Directory: {cwd}")


st.write(f"sys.path: {p}")
