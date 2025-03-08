import streamlit as st
import ChatGPT as cg

st.title("Best Email Writer.")
st.write("This is the best email maker ever. I LOVE writing emails.")
st.write("Looks like you need help writing an email to someone. No problem!")


name = st.text_input("What is your name?: ") 
sentTo = st.text_input("And who are you sending this to?: ")
option = st.text_input("Pick from one of these writing styles:1. Angry, 2. Formal, 3. Casual, 4. Like a Child Wrote It:")
topic = st.text_input("What are you writing about?: ")

prompt = "Write an email from " + name + " to " + sentTo + " in a " + option + " style about " + topic +  "."

but = st.button("Write!")

if (but): st.write(cg.singleRequest(prompt))