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
    ],
    "shoes": [
        "Customer: Hello! I’m looking for comfortable running shoes.",
        "Customer: Do you have any recommendations?",
        "Customer: What colors are available?",
        "Customer: Can I test them before buying?",
        "Customer: What is the return policy?",
        "Customer: Do you offer any loyalty discounts?",
        "Customer: Alright, I’ll take them. Where do I pay?",
        "Customer: Thanks for your help!"
    ]
}

# Initialisation de l'état de la conversation
if "scenario_name" not in st.session_state:
    st.session_state.scenario_name = random.choice(list(scenarios.keys()))
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "responses" not in st.session_state:
    st.session_state.responses = []

# Titre de l'application
st.title("🛍️ Store Assistant Chatbot - AI Interaction")
st.write("You are the salesperson. Type your response to the customer's questions.")

# Sélecteur de scénario
selected_scenario = st.selectbox("Choose a scenario:", list(scenarios.keys()), index=list(scenarios.keys()).index(st.session_state.scenario_name))
if selected_scenario != st.session_state.scenario_name:
    st.session_state.scenario_name = selected_scenario
    st.session_state.current_question = 0
    st.session_state.responses = []
    st.rerun()

# Charger le scénario actuel
scenario = scenarios[st.session_state.scenario_name]

# Afficher la progression
st.progress(st.session_state.current_question / len(scenario))

# Gestion de la conversation
if st.session_state.current_question < len(scenario):
    question = scenario[st.session_state.current_question]
    st.markdown(f"**{question}**")
    response = st.text_area("Your response:", key=f"response_{st.session_state.current_question}")

    if st.button("Submit Answer"):
        if response.strip():  # Vérifier que la réponse n'est pas vide
            st.session_state.responses.append(response)
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.warning("Please enter a response before submitting.")
else:
    st.success("🎯 You completed the conversation!")
    st.write(f"You completed the **{st.session_state.scenario_name}** scenario with {len(scenario)} interactions!")
    
    # Afficher les réponses de l'utilisateur
    st.write("## Your responses:")
    for i, question in enumerate(scenario):
        st.markdown(f"**{question}**")
        st.write(f"➡️ {st.session_state.responses[i]}")
        st.markdown("---")

    if st.button("Restart Chatbot"):
        st.session_state.current_question = 0
        st.session_state.responses = []
        st.rerun()
