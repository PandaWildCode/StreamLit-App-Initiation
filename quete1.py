import streamlit as st
import pandas as pd
from PIL import Image

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)

# Configuration générale de la page

st.set_page_config(
    page_title="Pandawane App",
    page_icon="🎵",
    layout="wide"
)

try:
    audio_file = open("C:/Codage/Testeur/Stream/celebrate.mp3", "rb")  # chemin vers ton audio
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3', start_time=0)
except FileNotFoundError:
    st.warning("L'audio de fond n'a pas été trouvé.")

# Titre principal

st.title("Bienvenue sur le site web de Pandawane")
st.text("Indiquez votre arrondissement de récupération :")
arrondissements = df['pickup_borough'].dropna().unique()

choix = st.selectbox("Choisissez votre arrondissement :", arrondissements)

if choix == "Manhattan":
    try:
        img = Image.open("C:/Codage/Testeur/Stream/manhattan.jpg.jpg")
        st.image(img, caption="Manhattan", width=700)
    except FileNotFoundError:
        st.warning("L'image de Manhattan n'a pas été trouvée.")
    st.write("Manhattan, le cœur économique de New York.")

elif choix == "Bronx":
    try:
        img = Image.open("C:/Codage/Testeur/Stream/bronx.jpg")
        st.image(img, caption="Bronx", width=700)
    except FileNotFoundError:
        st.warning("L'image du Bronx n'a pas été trouvée.")
    st.write("Le Bronx, la culture urbaine.")

elif choix == "Queens":
    try:
        img = Image.open("C:/Codage/Testeur/Stream/queens.jpg")
        st.image(img, caption="Queens", width=700)
    except FileNotFoundError:
        st.warning("L'image de Queens n'a pas été trouvée.")
    st.write("Queens, cultures et de cuisines du monde.")
elif choix == "Brooklyn":
    try:
        img = Image.open("C:/Codage/Testeur/Stream/brooklyn.jpg")
        st.image(img, caption="brooklyn", width=700)
    except FileNotFoundError:
        st.warning("L'image de Brooklyn n'a pas été trouvée.")
    st.write("Brooklyn, son pont et ses quartiers branchés.")
else:
    st.info(f"Aucune image ou description disponible pour {choix}.")

