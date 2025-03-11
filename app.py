import streamlit as st
import random

# Définition des scénarios
scenarios = {
    "jacket": [
        ("Customer: Good morning! I’m looking for a new jacket. Can you help me?",
         ["Hello! Of course, I can help. What type of jacket are you looking for?",
          "Hi! No, we don't have jackets today.",
          "Maybe, what do you want?"]),
        ("Customer: I would like something stylish but also warm for winter. Do you have any recommendations?",
         ["Yes, we have a stylish wool jacket that is perfect for winter.",
          "No, we only sell summer clothes.",
          "I don’t know, maybe you should check online?"]),
        ("Customer: That sounds great! What sizes do you have?",
         ["We have sizes from S to XXL.",
          "We don’t sell sizes.",
          "Only one size is available."]),
        ("Customer: I usually wear a medium. Can I try it on?",
         ["Yes, of course! The fitting rooms are over there.",
          "No, we don’t allow trying jackets.",
          "Maybe later."]),
        ("Customer: It fits well! How much is it?",
         ["It costs 80 euros.",
          "It’s free today!",
          "I don’t know."])
    ]
}

# Sélection d'un scénario au hasard
scenario = random.choice(list(scenarios.values()))

# Stockage de l'état de la conversation
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0

st.title("🛍️ Store Assistant Chatbot")
st.write("You are the salesperson. Choose the best response for each question!")

# Récupérer la question et les choix
question, choices = scenario[st.session_state.current_question]
st.write(question)

# Interface de choix
response = st.radio("Choose your response:", choices, key=st.session_state.current_question)

# Bouton pour passer à la question suivante
if st.button("Submit Answer"):
    if response == choices[0]:  # La meilleure réponse est toujours la première
        st.session_state.score += 1
    
    # Passer à la question suivante
    if st.session_state.current_question < len(scenario) - 1:
        st.session_state.current_question += 1
        st.rerun()  # Recharge l'interface pour afficher la prochaine question
    else:
        st.write(f"🎯 Your final score: {st.session_state.score}/{len(scenario)}")
        st.write("Thank you for playing!")
        
