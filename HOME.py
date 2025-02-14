import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2, gap="small")

content1 = "text here"
content2 = "text here"

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
                {content1}
            </div>
            """, 
            unsafe_allow_html=True
        )

st.subheader("Your Conversation")
st.text_area("Your Conversation", height=200, label_visibility="collapsed")
