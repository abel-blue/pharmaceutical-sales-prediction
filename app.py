
import os
import sys
import streamlit as st

sys.path.insert(0, './scripts')
from applications import visualizations, viz_model
from multiapp import MultiApp

st.set_page_config(page_title="Rossmann Sales Predictions", layout="wide")

app = MultiApp()

st.sidebar.markdown("""
# Rossmann Sales Predictions
""")

# Add all your application here
app.add_app("visualizations", visualizations.app)
app.add_app("model-prediction", viz_model.app)

# The main app
app.run()
