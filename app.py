import streamlit as st

st.set_page_config(page_title="Saheli.ai", page_icon="🌸")

# ---------- Simple emotion detection ----------
def detect_emotion(text):
    text = text.lower()
    if any(w in text for w in ["fail","marks","exam","viva","assignment","cgpa"]):
        return "academic"
    if any(w in text for w in ["internship","placement","career","future"]):
        return "career"
    if any(w in text for w in ["alone","lonely","friends","ignored"]):
        return "lonely"
    if any(w in text for w in ["breakup","crush","relationship","texted"]):
        return "relationship"
    if any(w in text for w in ["panic","anxiety","scared","can't breathe"]):
        return "panic"
    return "general"

# ---------- Smart replies ----------
def generate_reply(msg):
    emotion = detect_emotion(msg)

    replies = {
        "academic": "Exams feel overwhelming sometimes. You don’t have to solve everything tonight. Start with one small topic — which subject is worrying you most?",
        "career": "It feels scary when everyone seems ahead. Careers aren’t a race — many students figure things out later than they think.",
        "lonely": "Feeling left out hurts more than people admit. Want to tell me what happened with your friends?",
        "relationship": "Mixed signals confuse the mind a lot. What part of it is bothering you the most — their behaviour or your thoughts?",
        "panic": "Take a slow breath with me. Inhale 4 seconds… hold… exhale slowly. You’re safe right now. Stay with me.",
        "general": "I’m listening. Tell me a little more about what’s going on."
    }
    return replies[emotion]

# ---------- UI ----------
st.title("🌸 Saheli.ai")
st.caption("Your empathetic college companion")

if "chat" not in st.session_state:
    st.session_state.chat = []

# Display previous messages
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)

# Input
user_input = st.chat_input("Talk to Saheli...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    reply = generate_reply(user_input)

    st.session_state.chat.append(("assistant", reply))
    with st.chat_message("assistant"):
        st.write(reply)

# Sidebar
st.sidebar.title("About Saheli")
st.sidebar.write("Saheli is a student emotional support companion designed to provide a safe, non-judgmental conversation space.")
st.sidebar.write("This is a prototype demonstration for hackathon use.")
