import streamlit as st
import pandas as pd
import os

# Set page configuration
st.set_page_config(page_title="Pinoybaiting Dashboard", layout="wide")

import bertopic_module  


# Sidebar navigation
# st.sidebar.title("Pinoybaiting Dashboard")
# selection = st.sidebar.radio("Go to", ["Summary", "LDA", "BERTopic", "HLTM"])

st.title("Pinoybaiting Dashboard (Topic Modeling using BERTopic Algorithm")

# ---------------------------------
#  BERTopic
# ---------------------------------

bertopic_module.show_bertopic_section()