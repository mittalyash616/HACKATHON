import streamlit as st
from streamlit_autorefresh import st_autorefresh
st.set_page_config(layout="wide")

count = st_autorefresh(interval = 1000, key = "data_refresh")

col1, col2 = st.columns(2, gap="small")

content1 = ""
content2 = ""
content3 = ""

with col1:
    st.subheader("Potential Diagnosis")
    with st.container():
        st.markdown(
            f"""
            <div style="
                background-color: #F0F0F0; 
                border-radius: 10px; 
                padding: 20px; 
                height: 300px; 
                overflow: auto;
                color: black;">
                {content1}
            </div>
            """, 
            unsafe_allow_html=True
        )

with col2:
    st.subheader("Suggested Questions")
    with st.container():
        st.markdown(
            f"""
            <div style="
                background-color: #F0F0F0; 
                border-radius: 10px; 
                padding: 20px; 
                height: 300px; 
                overflow: auto;
                color: black;">
                {content2}
            </div>
            """, 
            unsafe_allow_html=True
        )

st.subheader("Your Conversation")
with st.container():
        st.markdown(
            f"""
            <div style="
                background-color: #F0F0F0; 
                border-radius: 10px; 
                padding: 20px; 
                height: 200px; 
                overflow: auto;
                color: black;">
                {content3}
            </div>
            """, 
            unsafe_allow_html=True
        )
