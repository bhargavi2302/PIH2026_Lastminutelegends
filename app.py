import streamlit as st
import random
import datetime

st.set_page_config(page_title="Saheli.ai", page_icon="🌸", layout="centered")

# ---------------- SESSION MEMORY ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "journal" not in st.session_state:
    st.session_state.journal = []

# ---------------- HEADER ----------------
st.title("🌸 Saheli.ai")
st.write("Your AI-Powered Student Emotional Companion")
st.write("Talk freely. I listen without judging.")

# ---------------- MOOD + JOURNAL ----------------
st.sidebar.header("🧠 Feelings Corner")

mood = st.sidebar.selectbox(
    "How do you feel today?",
    ["Happy","Stressed","Anxious","Sad","Overwhelmed","Lonely"]
)

entry = st.sidebar.text_area("Write about your day")

if st.sidebar.button("Save Entry"):
    date = datetime.datetime.now().strftime("%d %b %Y")
    st.session_state.journal.append(f"{date} — {mood}: {entry}")
    st.sidebar.success("Saved safely")

st.sidebar.subheader("Past Entries")
for e in st.session_state.journal[-5:]:
    st.sidebar.write("•", e)

# ---------------- RESPONSE ENGINE ----------------
def detect_topic(text):
    text=text.lower()

    if any(w in text for w in ["exam","marks","cgpa","assignment","study"]):
        return "academic"
    if any(w in text for w in ["placement","internship","career"]):
        return "career"
    if any(w in text for w in ["alone","lonely","ignored"]):
        return "lonely"
    if any(w in text for w in ["breakup","relationship","crush"]):
        return "relationship"
    if any(w in text for w in ["panic","anxiety","scared"]):
        return "panic"
    return "general"

def generate_reply(msg):
    topic = detect_topic(msg)

    replies={
        "academic":[
            "Exams feel heavy sometimes. Let’s break it into one small step — what subject worries you?",
            "You don’t have to solve everything today. Start small."
        ],
        "career":[
            "Everyone’s timeline is different. You are not behind.",
            "Placements don’t define your capability."
        ],
        "lonely":[
            "I’m here with you. Want to tell me what happened?",
            "Feeling left out hurts. When did this start?"
        ],
        "relationship":[
            "Mixed signals can be confusing. What part hurt you most?",
            "Your feelings are valid here."
        ],
        "panic":[
            "Take a slow breath with me… inhale 4 seconds… exhale slowly.",
            "You’re safe right now. Stay with me."
        ],
        "general":[
            "I’m listening. Tell me more.",
            "You can share anything here."
        ]
    }

    return random.choice(replies[topic])

# ---------------- CHAT UI ----------------
st.header("💬 Talk to Saheli")

for role,msg in st.session_state.chat:
    with st.chat_message(role):
        st.write(msg)

user_input = st.chat_input("Type your thoughts...")

if user_input:
    st.session_state.chat.append(("user",user_input))
    with st.chat_message("user"):
        st.write(user_input)

    reply = generate_reply(user_input)

    st.session_state.chat.append(("assistant",reply))
    with st.chat_message("assistant"):
        st.write(reply)

# ---------------- WELLNESS ----------------
st.header("🌿 Relaxation Space")

if st.button("Start 1-minute calm exercise"):
    st.write("Breathe in 4 sec → Hold 4 sec → Exhale 6 sec (repeat 5 times)")

st.video("https://www.youtube.com/watch?v=inpok4MKVLM")

# ---------------- DAILY TIP ----------------
tips=[
"Drink water and stretch for 2 minutes.",
"Step outside sunlight for 5 minutes.",
"Write one worry and one solution.",
"Message someone you trust."
]
st.sidebar.header("Daily Tip")
st.sidebar.write(random.choice(tips))
