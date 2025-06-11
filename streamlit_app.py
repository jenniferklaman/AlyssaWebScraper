import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Renewal Metrics Dashboard", layout="wide")

st.title("Renewal Metrics Tracker")

# Load data
try:
    with open("data/renewal_data.json", "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
except:
    st.warning("No data file found. Run the scraper first.")
    st.stop()

# Sidebar filters
employee = st.sidebar.selectbox("Filter by Employee", ["All"] + sorted(df["Employee First Name"].unique()))
month = st.sidebar.selectbox("Filter by Book Month", ["All"] + sorted(df["Book Month"].unique()))

if employee != "All":
    df = df[df["Employee First Name"] == employee]
if month != "All":
    df = df[df["Book Month"] == month]

# Display data
st.dataframe(df)

# Summary
st.subheader("Metrics Summary")
st.metric("Total Records", len(df))
st.metric("Total Premium ($)", df["Target Total"].sum())
