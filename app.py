import streamlit as st
st.write("Hello World")

import pandas as pd

# Titre principal de l'application
st.title("The title of my page")

# Titre de section important
st.header("An Important Header")

# Sous-titre
st.subheader("A Secondary Header")

# Texte simple
st.text("My classic text")

# Texte avec mise en forme Markdown et emoji
st.markdown(':rainbow: :rainbow: My markdown')

# Création du DataFrame
data = pd.DataFrame({
    "Cards": ['Name 1', 'Name 2', 'Name 3', 'Name 4'],
    "Quantity": [0, 1, 0, 3]
})

# Affichage du DataFrame
st.write(data)  # ou st.dataframe(data) pour un affichage interactif

if st.button("Ajouter"):
    st.write("+1")
    