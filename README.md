# TalentScout Hiring Assistant 🤖

## Project Overview

The TalentScout Hiring Assistant is an AI-powered chatbot designed to support the initial screening of candidates for technical roles. The chatbot interacts with candidates through a conversational interface, collects essential profile information, and generates relevant technical interview questions based on the candidate’s declared tech stack.

This project was built as part of an **AI/ML Intern assignment** to demonstrate understanding of Large Language Models (LLMs), prompt design, and context-aware conversational flow.

---

## Features

* Interactive chat-based UI built using **Streamlit**
* Greets candidates and explains the screening process
* Collects candidate details:

  * Full Name
  * Email Address
  * Years of Experience
  * Desired Position(s)
  * Current Location
  * Tech Stack
* Dynamically generates **3–5 technical interview questions** based on the declared tech stack
* Maintains conversation context throughout the interaction
* Graceful exit handling using keywords like `exit`, `quit`, or `bye`
* No paid API usage

---

## Technology Stack

* **Programming Language:** Python
* **Frontend/UI:** Streamlit
* **LLM:** Open-source LLaMA model running locally via **Ollama**
* **Other Libraries:** requests

---

## Why Ollama (No API Key Used)

Instead of using a paid cloud-based LLM API, this project uses **Ollama** to run an open-source LLaMA model locally. This approach was chosen to:

* Avoid paid API dependencies
* Improve data privacy
* Enable local deployment
* Keep the project simple and cost-effective

No API key or internet-based LLM service is required.

---

## Installation & Setup Instructions

### Prerequisites

* Python 3.9 or above
* Ollama installed on the system

### Step 1: Install Ollama

Download and install Ollama from:

```
https://ollama.com
```

After installation, pull a model:

```
ollama pull llama3
```

---

### Step 2: Install Python Dependencies

Install required Python packages:

```
pip install -r requirements.txt
```

---

### Step 3: Run the Application

Start the Streamlit app using:

```
streamlit run app.py
```

The chatbot will open in your default web browser.

---

## Usage Guide

1. Launch the application
2. The chatbot greets you and begins the screening process
3. Answer the questions one by one
4. Enter your tech stack when prompted (e.g., Python, Django, MySQL)
5. The chatbot generates relevant technical interview questions
6. Type `exit` anytime to end the conversation

---

## Prompt Design Explanation

The LLM is used only for generating technical interview questions. A clear and role-based prompt is sent to the model, instructing it to act as a technical interviewer and generate concise, relevant questions based on the provided tech stack.

This ensures:

* Focused and relevant outputs
* Controlled and predictable responses
* Proper alignment with the hiring use case

---

## Data Handling & Privacy

* All candidate data is stored temporarily in session state
* No data is saved permanently or sent to external services
* This approach aligns with basic data privacy principles

---

## Challenges & Solutions

**Challenge:** Paid API dependency for LLMs
**Solution:** Used Ollama with a locally running open-source LLM

**Challenge:** Maintaining conversation context in Streamlit
**Solution:** Used `st.session_state` to track conversation stages and candidate responses

---

## Limitations

* The application is designed for local execution
* Ollama must be installed for LLM functionality
* No database or authentication system is implemented (by design)

---

## Demo

A short screen recording demonstrating the chatbot’s functionality is provided along with the source code.

---

## Conclusion

This project demonstrates how LLMs can be effectively integrated into a real-world hiring workflow using prompt engineering, clean logic, and a simple UI. It focuses on clarity, functionality, and explainability rather than over-engineering.
