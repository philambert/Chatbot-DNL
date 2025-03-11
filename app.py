import streamlit as st
import random

# Définition des scénarios interactifs
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
    ],
    "electronics": [
        "Customer: Hi, I need a new smartphone.",
        "Customer: What is the best model for photography?",
        "Customer: Does it come with a warranty?",
        "Customer: How much storage does it have?",
        "Customer: Can I see a demo?",
        "Customer: Do you have any trade-in options?",
        "Customer: Okay, I will buy it. How can I pay?",
        "Customer: Thank you!"
    ]
}

# Initialisation de l'état de la conversation
if "scenario_name" not in st.session_state:
    st.session_state.scenario_name = random.choice(list(scenarios.keys()))
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "responses" not in st.session_state:
    st.session_state.responses = []
if "total_score" not in st.session_state:
    st.session_state.total_score = 0

# Titre de l'application
st.title("🛍️ Store Assistant Chatbot - AI Interaction")
st.write("You are the salesperson. Type your response to the customer's questions.")

# Sélecteur de scénario interactif
selected_scenario = st.selectbox("Choose a scenario:", list(scenarios.keys()), index=list(scenarios.keys()).index(st.session_state.scenario_name))
if selected_scenario != st.session_state.scenario_name:
    st.session_state.scenario_name = selected_scenario
    st.session_state.current_question = 0
    st.session_state.responses = []
    st.session_state.total_score = 0
    st.rerun()

# Charger le scénario actuel
scenario = scenarios[st.session_state.scenario_name]

# Affichage de la progression
st.progress(st.session_state.current_question / len(scenario))

# Fonction d'évaluation des réponses
def evaluate_response(response):
    if len(response.strip()) < 5:
        return 1  # Réponse trop courte
    elif len(response.strip()) < 15:
        return 2  # Réponse correcte mais courte
    elif "discount" in response.lower() or "price" in response.lower() or "size" in response.lower():
        return 4  # Réponse pertinente
    else:
        return 3  # Réponse acceptable

# Gestion de la conversation
if st.session_state.current_question < len(scenario):
    question = scenario[st.session_state.current_question]
    st.markdown(f"**{question}**")
    response = st.text_area("Your response:", key=f"response_{st.session_state.current_question}")

    if st.button("Submit Answer"):
        if response.strip():  # Vérifier que la réponse n'est pas vide
            score = evaluate_response(response)
            st.session_state.total_score += score  # Ajouter le score de la réponse
            st.session_state.responses.append((response, score))  # Stocker réponse + score
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.warning("Please enter a response before submitting.")
else:
    # Évaluation finale
    max_score = len(scenario) * 4
    final_score = (st.session_state.total_score / max_score) * 5  # Note sur 5 étoiles

    st.success("🎯 You completed the conversation!")
    st.write(f"**Scenario:** {st.session_state.scenario_name}")
    st.write(f"✅ Your total score: {st.session_state.total_score}/{max_score}")
    
    # Affichage de l'évaluation avec étoiles ⭐⭐⭐⭐⭐
    star_rating = "⭐" * round(final_score) + "☆" * (5 - round(final_score))
    st.write(f"**Your rating: {star_rating} ({round(final_score, 1)}/5)**")

    # Afficher les réponses de l'utilisateur
    st.write("## Your responses and feedback:")
    for i, (question, response_data) in enumerate(zip(scenario, st.session_state.responses)):
        response, score = response_data
        st.markdown(f"**{question}**")
        st.write(f"➡️ **Your response:** {response}")
        st.write(f"📝 **Score:** {score}/4")
        st.markdown("---")

    if st.button("Restart Chatbot"):
        st.session_state.current_question = 0
        st.session_state.responses = []
        st.session_state.total_score = 0
        st.rerun()
