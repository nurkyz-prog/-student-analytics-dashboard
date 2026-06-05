import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Student Performance Dashboard")

df = pd.read_csv("students.csv")

st.write(df)

avg = df["Score"].mean()

st.metric(
    "Average Score",
    round(avg, 1)
)

chart = px.bar(
    df,
    x="Student",
    y="Score",
    color="Course"
)

st.plotly_chart(chart)

course = st.selectbox(
    "Filter",
    df["Course"].unique()
)

filtered = df[
    df["Course"] == course
]

st.write(filtered)