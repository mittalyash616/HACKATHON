import streamlit as st

if "Authentication" not in st.session_state:
    st.session_state.Authentication = {"Username":"",
                                       "Password":""}

with st.form(key = "loginpage"):
    st.session_state.Authentication["Username"] = st.text_input("Enter your Username")
    st.session_state.Authentication["Password"] = st.text_input("Enter your Password")
    submitButton = st.form_submit_button(label = "Submit")
    if submitButton:
        st.switch_page("HOME.py")

st.caption("Not Login ?")
st.markdown("[SignUp](SIGNUP.py)")