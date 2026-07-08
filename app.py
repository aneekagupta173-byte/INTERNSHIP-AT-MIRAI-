import streamlit as st 

st.title("The void") # this gives the tittle to the window. 
st.write("FILL THE FORM BELOW!") # this is my instructional message
st.write("name:") # this is the input feild name name
user_name = st.text_input("Name") # this is where the system takes the name input
st.write("message:") # this is the input feild message name
user_message = st.text_input("Message") # this is where system takes the message input
tokens = (len(user_message))/4 # number of tokens calculation

if st.button("TRANSMIT"): # gives code instructions when the button is clicked.
    if not user_name.strip() or not user_message.strip(): # if the feilds are not filled then -
        st.error("Please fill in all the fields.") # prints this message
    else: # the other situation where the feilds are filled then
        st.success(f"Trasmission successful! Greetings {user_name}, we have received your message: {user_message}") # the sucess message
        st.info(f"System Check: Your message will consume approximately {tokens} tokens from our context window.") # this is the system message

    
