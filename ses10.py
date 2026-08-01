import streamlit as st 
import time

st.title("DASHBOARD")

with st.form("DETAILS"):
    st.write("Enter your name")
    Name = st.text_input("name")
    age = st.slider("AGE", 0,5,30)
    submitted = st.form_submit_button()

if submitted:
    
    if age > 18:
        st.success("You can apply for dl")
    else:
        st.error("you cannot apply for dl")
    
    





if st.button("save data"):
  with st.spinner("Processing your request..."):
    time.sleep(2)  
  st.toast("Data saved successfully!")
