import streamlit as st
import requests

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")

st.title("🤖 TalentScout Hiring Assistant")
st.write("AI-powered initial screening chatbot for tech roles")

# ------------------ OLLAMA HELPER ------------------
def query_ollama(prompt: str) -> str:
    """
    Sends a prompt to a locally running Ollama model and returns the response.
    Ollama must be running on http://localhost:11434
    """
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        return response.json().get("response", "")
    except Exception:
        return "I am unable to generate questions right now. Please try again later."

# ------------------ SESSION STATE INIT ------------------
if "current_stage" not in st.session_state:
    st.session_state.current_stage = 0

if "candidate" not in st.session_state:
    st.session_state.candidate = {}

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I’m the TalentScout Hiring Assistant. I’ll ask a few questions to understand your profile. You can type 'exit' anytime to stop."
        }
    ]

# ------------------ DISPLAY CHAT ------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ------------------ QUESTIONS FLOW ------------------
questions = [
    "What is your full name?",
    "What is your email address?",
    "How many years of experience do you have?",
    "What position(s) are you applying for?",
    "Where are you currently located?",
    "Please list your tech stack (languages, frameworks, tools)."
]

keys = [
    "name",
    "email",
    "experience",
    "position",
    "location",
    "tech_stack"
]

# ------------------ USER INPUT ------------------
user_input = st.chat_input("Type your response here...")

if user_input:
    # Exit handling
    if user_input.lower() in ["exit", "quit", "bye"]:
        st.session_state.messages.append(
            {"role": "assistant", "content": "Thank you for your time! We will get back to you soon. 👋"}
        )
        st.stop()

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    stage = st.session_state.current_stage

    # Store candidate response
    if stage < len(keys):
        st.session_state.candidate[keys[stage]] = user_input

    st.session_state.current_stage += 1

    # Ask next question
    if st.session_state.current_stage < len(questions):
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": questions[st.session_state.current_stage]
            }
        )

    # Generate technical questions
    elif st.session_state.current_stage == len(questions):
        tech_stack = st.session_state.candidate.get("tech_stack", "")

        prompt = f"""
You are a technical interviewer.
Generate 3 to 5 clear technical interview questions to assess a candidate's proficiency
in the following tech stack:

{tech_stack}

Only list the questions.
"""

        tech_questions = query_ollama(prompt)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Great! Here are a few technical questions for you:\n\n" + tech_questions
            }
        )

    # End conversation
    else:
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Thank you for completing the initial screening. Our team will review your responses and contact you soon."
            }
        )

    st.rerun()
