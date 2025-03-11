import streamlit as st
import random

# Définition des scénarios avec conversation libre
scenarios = {
    "jacket": [
        "Customer: Good morning! I’m looking for a new jacket. Can you help me?",
        "Customer: I need something warm for winter.",
        "Customer: That sounds great! What sizes do you have?",
        "Customer: Can I try it on?",
        "Customer: How much does it cost?",
        "Customer: Do you have any discounts?",
        "Customer: Okay, I will buy it. Where can I pay?",
        "Customer: Thank you very much!"
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
st.write("You are the salesperson. Type your response to the customer's questions.")

# Récupérer la question et permettre une réponse libre
if st.session_state.current_question < len(scenario):
    question = scenario[st.session_state.current_question]
    st.write(question)
    response = st.text_area("Your response:", key=st.session_state.current_question)

    if st.button("Submit Answer"):
        st.session_state.responses.append(response)
        
        # Passage à la question suivante
        st.session_state.current_question += 1
        st.rerun()  # Recharge l'interface pour afficher la prochaine question
else:
    st.write("🎯 Your final evaluation:")
    st.write(f"You completed the conversation with {len(scenario)} interactions!")
    
    # Afficher les réponses de l'utilisateur
    st.write("Your responses:")
    for i, question in enumerate(scenario):
        st.write(f"{question}\nYour answer: {st.session_state.responses[i]}")

    if st.button("Restart Chatbot"):
        st.session_state.current_question = 0
        st.session_state.responses = []
        st.rerun()
