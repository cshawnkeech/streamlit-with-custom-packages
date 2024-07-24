"""
restore model and observation_bounds

"""
from joblib import load
import pandas as pd
import streamlit as st


@st.cache_resource()
def restore_model():
    """
    return model object
    """
    # Restore model
    with open("models/final_model.joblib", "rb") as f:

        # we'll load the file here
        model = load(f)

    return model


@st.cache_data
def restore_bounds():
    """
    return bounds df
    """
    # Restore model
    with open("models/observation_bounds.joblib", "rb") as f:

        # we'll load the file here
        bounds = load(f)

    return bounds


MODEL = restore_model


if __name__ == "__main__":

    print(restore_bounds())
