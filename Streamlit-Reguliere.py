import streamlit as st
import pandas as pd

# Add containers
header = st.container()
dataset = st.container()
features = st.container()
modelTraining = st.container()

with header:
    st.title("Welcome to my application")