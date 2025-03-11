import streamlit as st
import random

def chatbot():
    st.title("🛍️ Store Assistant Chatbot")
    st.write("You are the salesperson. Choose the best response for each question!")

    scenarios = {
        "jacket": [
            ("Customer: Good morning! I’m looking for a new jacket. Can you help me?",
             ["Hello! Of course, I can help. What type of jacket are you looking for?",
              "Hi! No, we don't have jackets today.",
              "Maybe, what do you want?"])
        ]
    }

    scenario = random.choice(list(scenarios.values()))

    score = 0
    for question, choices in scenario:
        st.write(question)
        response = st.radio("Choose your response:", choices)
        if response == choices[0]:  # La meilleure réponse est toujours la première
            score += 1

    st.write(f"Your final score: {score}/{len(scenario)}")

if __name__ == "__main__":
    chatbot() 
