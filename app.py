import streamlit as st

st.set_page_config(page_title="Saheli.ai", page_icon="🌸")

st.title("🌸 Saheli.ai")
st.subheader("Your supportive companion for students")

st.write("Hi, I'm Saheli. You can talk to me about exams, stress, friends or anything on your mind.")

user_input = st.chat_input("Type your message...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    # temporary reply so app runs
    reply = "I am here with you. Tell me more about it."

    with st.chat_message("assistant"):
        st.write(reply)
