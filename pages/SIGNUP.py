import streamlit as st

if "Information" not in st.session_state:
    st.session_state.Information = {"Name": "",
                                    "Username":"",
                                    "Password":""}

with st.form(key = "signuppage"):
    st.session_state.Information["Name"] = st.text_input("Enter your Name")
    st.session_state.Information["Username"] = st.text_input("Enter your Username")
    st.session_state.Information["Password"] = st.text_input("Enter your Password")
    submitButton = st.form_submit_button(label = "Submit")
    if submitButton:
        st.switch_page("Home.py")

st.caption("Already Login ?")
st.markdown("[Login](Login.py)")