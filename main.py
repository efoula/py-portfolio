import streamlit as st
import pandas as pd

st.set_page_config()
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Eslam Foula")
    bio = """ Seasoned Product Manager with 12+ years in tech, skilled in product lifecycle management, user-centric design, and cross-functional team leadership. Proven track record of scaling startups, increasing revenue through innovative solutions, and spearheading projects that deliver measurable outcomes. Adept at leveraging agile methodologies, prioritizing customer experience, and driving product-market fit! """
    st.write(bio, size=10)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")



