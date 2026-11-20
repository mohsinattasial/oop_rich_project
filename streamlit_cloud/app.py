"""Streamlit Community Cloud portfolio adapter for oop_rich_project.

This does not replace the original implementation.
"""
from pathlib import Path

import streamlit as st

TITLE = "Rich Library OOP Study"
ICON = "🧩"
DESC = "University coursework exploring the Rich terminal presentation library and a custom StudentDashboard table."
CATEGORY = "Python terminal UI / OOP"
NOTICE = "The Rich dashboard is a terminal program. This Streamlit page displays a lightweight educational representation."
GITHUB = "https://github.com/mohsinattasial/oop_rich_project"
VERCEL = "https://mohsin-rich-oop.vercel.app"
LOCAL_COMMAND = "python oop_rich_project/code/custom_extension.py"
FEATURES = ["Object-oriented class extension","UML architecture","Student dashboard example"]

st.set_page_config(page_title=TITLE + " | Mohsin Atta", page_icon=ICON, layout="wide")
st.caption("Mohsin Atta · GitHub Portfolio · Streamlit Cloud edition")
st.title(ICON + " " + TITLE)
st.write(DESC)
st.caption(CATEGORY)

left, right = st.columns(2)
with left:
    st.link_button("GitHub source code", GITHUB, use_container_width=True)
with right:
    st.link_button("Existing browser version", VERCEL, use_container_width=True)

st.info(NOTICE)
with st.expander("Original project and features", expanded=False):
    for feature in FEATURES:
        st.write("• " + feature)
    st.code(LOCAL_COMMAND, language="bash")

st.subheader("Example student dashboard")
st.dataframe([
    {"Course": "Object-Oriented Programming", "Status": "Completed", "Priority": "High"},
    {"Course": "Artificial Intelligence", "Status": "In progress", "Priority": "High"},
    {"Course": "Linear Algebra", "Status": "Completed", "Priority": "Medium"},
], hide_index=True, use_container_width=True)
st.caption("Illustrative Streamlit table. The repository's real StudentDashboard uses the Rich terminal library.")

st.divider()
st.caption("© 2026 Mohsin Atta · Educational portfolio · MIT-licensed original code where applicable")
