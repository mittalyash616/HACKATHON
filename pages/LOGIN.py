import streamlit as st

if "Authentication" not in st.session_state:
    st.session_state.Authentication = {"Username":"",
                                       "Password":""}

with st.form(key = "loginpage"):
    st.session_state.Authentication["Username"] = st.text_input("Enter your Username")
    st.session_state.Authentication["Password"] = st.text_input("Enter your Password")
    submitButton = st.form_submit_button(label = "Submit")
    if submitButton:
        # need to apply backend for data checking in session_state.Authentication
        # TODO
        st.switch_page("HOME.py")

st.caption("No Account Yet ?")
if st.button("Signup"):
    st.switch_page("pages/SIGNUP.py")