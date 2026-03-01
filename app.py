import streamlit as st
import random

st.set_page_config(page_title="Saheli.ai", page_icon="🌸")

# ---------------- MEMORY ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []
if "last_topic" not in st.session_state:
    st.session_state.last_topic = None

# ---------------- DETECT CONTEXT ----------------
def detect_context(text):
    text = text.lower()

    categories = {
        "academic": ["exam","marks","fail","cgpa","assignment","viva","study","backlog"],
        "career": ["placement","internship","resume","career","future","job"],
        "lonely": ["alone","lonely","ignored","friends","left out","nobody"],
        "relationship": ["crush","breakup","relationship","texted","reply","seen"],
        "panic": ["panic","anxiety","scared","can't breathe","heart racing"],
        "family": ["parents","pressure","expectations","home","family"],
    }

    for topic, words in categories.items():
        if any(w in text for w in words):
            return topic
    return "general"

# ---------------- RESPONSE ENGINE ----------------
def generate_reply(msg):
    topic = detect_context(msg)
    st.session_state.last_topic = topic

    responses = {
        "academic": [
            "That sounds stressful… academics can pile up quickly. What subject is worrying you the most?",
            "You don’t have to fix everything tonight. One small step counts — which topic feels manageable right now?",
            "Marks don’t define you, but I understand why they feel heavy. What part of it scares you most?"
        ],
        "career": [
            "It feels scary when everyone seems ahead. Careers rarely follow a straight line though.",
            "Comparison hurts more than failure sometimes. Are you worried about skills or opportunities?",
            "Many students feel lost before finding direction — what path were you hoping for?"
        ],
        "lonely": [
            "Feeling left out can be really painful. Do you want to tell me what happened?",
            "Sometimes we’re surrounded by people but still feel alone. When did this start?",
            "I’m here with you. Was it something someone did or just a feeling building up?"
        ],
        "relationship": [
            "Mixed signals confuse the mind a lot. What part bothered you most?",
            "Uncertainty in relationships drains energy. Are you overthinking their actions?",
            "Your feelings matter here — what were you hoping from them?"
        ],
        "panic": [
            "Stay with me. Take a slow breath in… hold… and release slowly.",
            "You’re okay right now. Try unclenching your jaw and relax your shoulders.",
            "Focus on 5 things you can see around you — grounding helps the mind settle."
        ],
        "family": [
            "Family expectations can feel heavy. Do you feel understood by them?",
            "It’s hard when love comes with pressure. What are they expecting from you?",
            "Sometimes we carry guilt even when trying our best. Want to talk about it?"
        ],
        "general": [
            "I’m listening. Tell me more about what’s been on your mind.",
            "You can share anything here — what’s bothering you today?",
            "Hmm… what part of this is affecting you the most?"
        ]
    }

    reply = random.choice(responses[topic])

    # follow-up awareness
    if topic == st.session_state.get("last_topic"):
        reply += "\n\nYou mentioned something similar earlier — has it been bothering you for a while?"

    return reply

# ---------------- UI ----------------
st.title("🌸 Saheli.ai")
st.caption("A supportive companion for college students")

# display chat
for role, msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)

# user input
user_input = st.chat_input("Talk to Saheli...")

if user_input:
    st.session_state.chat.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    reply = generate_reply(user_input)

    st.session_state.chat.append(("assistant", reply))
    with st.chat_message("assistant"):
        st.write(reply)

# sidebar
st.sidebar.title("Saheli Care Tools")

if st.sidebar.button("🧘 Calm Me"):
    st.sidebar.write("Breathe in 4 sec → Hold 4 sec → Exhale 6 sec. Repeat slowly.")

if st.sidebar.button("📝 Vent Out"):
    st.sidebar.write("Write freely. No one is judging you here.")

st.sidebar.write("Saheli provides emotional support — not a medical substitute.")
