import requests
import streamlit as st

# URL de votre fonction Azure
azure_function_url = "https://functionappforserverlessapp.azurewebsites.net/api/httptriggernofonction?user_id="

# Créer une zone de saisie pour l'ID utilisateur
user_id = st.text_input("Entrez votre ID utilisateur")

# Envoyer une requête HTTP à la fonction Azure lorsque l'utilisateur appuie sur le bouton "Recommander"
if st.button("Recommander"):
    # Ajouter l'ID utilisateur à la requête
    params = {"user_id": user_id}

    # Envoyer la requête à la fonction Azure
    response = requests.get(azure_function_url, params=params)

    # Afficher la réponse de la fonction Azure dans l'interface utilisateur
    if response.status_code == 200:
        recommended_articles = response.text
        st.success(f"Recommandations pour l'utilisateur {user_id}: {recommended_articles}")
    else:
        st.error("Erreur lors de la récupération des recommandations.")
