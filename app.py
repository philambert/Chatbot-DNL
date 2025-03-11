import streamlit as st
import random

# Définition des scénarios avec une conversation plus fluide
scenarios = {
    "jacket": [
        ("Customer: Good morning! I’m looking for a new jacket. Can you help me?", ["Of course! What style are you looking for?", "No, we don’t sell jackets.", "Maybe, what do you want?"]),
        ("Customer: I need something warm for winter.", ["We have wool jackets and down coats.", "We don’t have winter jackets.", "I don’t know."]),
        ("Customer: That sounds great! What sizes do you have?", ["We have sizes from S to XXL.", "We don’t sell sizes.", "Only one size is available."]),
        ("Customer: Can I try it on?", ["Yes, of course! The fitting rooms are over there.", "No, we don’t allow trying clothes.", "Maybe later."]),
        ("Customer: How much does it cost?", ["It costs 80 euros.", "It’s free today!", "I don’t know."]),
        ("Customer: Do you have any discounts?", ["Yes, we have a 10% discount today!", "No, we never do discounts.", "Ask the manager."]),
        ("Customer: Okay, I will buy it. Where can I pay?", ["You can pay at the checkout.", "We don’t accept payments.", "I don’t know."]),
        ("Customer: Thank you very much!", ["You’re welcome! Have a great day!", "Bye.", "Whatever."])
    ]
}

# Sélection d'un scénario aléatoire
scenario = random.choice(list(scenarios.values()))

# Stockage de l'état de la conversation
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "responses" not in st.session_state:
    st.session_state.responses = []

st.title("🛍️ Store Assistant Chatbot - AI Interaction")
st.write("You are the salesperson. Answer the customer's questions.")

# Récupérer la question et les choix de réponse
if st.session_state.current_question < len(scenario):
    question, choices = scenario[st.session_state.current_question]
    st.write(question)
    response = st.radio("Choose your response:", choices, key=st.session_state.current_question)

    if st.button("Submit Answer"):
        st.session_state.responses.append(response)
        if response == choices[0]:  # La meilleure réponse est toujours la première
            st.session_state.score += 1
        
        st.session_state.current_question += 1
        st.rerun()  # Recharge l'interface pour afficher la prochaine question
else:
    st.write("🎯 Your final evaluation:")
    st.write(f"You answered {st.session_state.score}/{len(scenario)} correctly!")
    if st.session_state.score < 5:
        st.write("You need more practice. Try again!")
    elif st.session_state.score < 7:
        st.write("Good job, but you can improve!")
    else:
        st.write("Excellent! You are ready for real customer interactions!")

    # Afficher les réponses de l'utilisateur
    st.write("Your responses:")
    for i, (question, choices) in enumerate(scenario):
        st.write(f"{question}\nYour answer: {st.session_state.responses[i]}")

    if st.button("Restart Chatbot"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.responses = []
        st.rerun()
