import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Le Test des Goûts", page_icon="📸")

# Base de données simplifiée des célébrités (URLs publiques d'images)
# Note : Pour un site pro, il faudrait héberger tes propres images.
celebs = [
    {"nom": "Margot Robbie", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Margot_Robbie_at_2019_Cannes_Film_Festival.jpg/800px-Margot_Robbie_at_2019_Cannes_Film_Festival.jpg"},
    {"nom": "Jisoo (Blackpink)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Kim_Ji-soo_at_a_press_conference_for_Snowdrop_in_December_2021.jpg/800px-Kim_Ji-soo_at_a_press_conference_for_Snowdrop_in_December_2021.jpg"},
    {"nom": "Zendaya", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Zendaya_at_the_2019_Emmy_Awards.jpg/800px-Zendaya_at_the_2019_Emmy_Awards.jpg"},
    {"nom": "Hoyeon Jung", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Jung_Ho-yeon_at_2022_Critics_Choice_Awards.jpg/800px-Jung_Ho-yeon_at_2022_Critics_Choice_Awards.jpg"},
    {"nom": "Scarlett Johansson", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Scarlett_Johansson_by_Gage_Skidmore_2.jpg/800px-Scarlett_Johansson_by_Gage_Skidmore_2.jpg"},
    {"nom": "Dilraba Dilmurat", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Dilraba_Dilmurat_at_the_2019_Cosmo_Glam_Night.jpg"},
]

st.title("🎯 Le Jeu des Goûts")

# Système d'onglets pour séparer l'Ami des Joueurs
tab1, tab2 = st.tabs(["🔒 Mode Ami (Choix)", "🎮 Mode Joueur (Devine)"])

with tab1:
    st.header("Étape 1 : L'ami fait ses choix")
    st.write("L'ami doit dire discrètement qui lui plaît.")
    choices = {}
    for person in celebs:
        res = st.radio(f"Est-ce que {person['nom']} te plaît ?", ["Non", "Oui"], key=f"ami_{person['nom']}")
        choices[person['nom']] = res
    
    if st.button("Enregistrer mes choix"):
        st.session_state['votes_ami'] = choices
        st.success("Choix enregistrés ! Passe maintenant l'écran aux autres.")

with tab2:
    if 'votes_ami' not in st.session_state:
        st.warning("L'ami doit d'abord enregistrer ses choix dans l'onglet 1 !")
    else:
        st.header("Étape 2 : Devine !")
        score = 0
        for person in celebs:
            st.image(person['img'], width=300)
            devinette = st.radio(f"Est-ce que tu penses qu'elle plaît à ton ami ?", ["Non", "Oui"], key=f"jeu_{person['nom']}")
            
            if devinette == st.session_state['votes_ami'][person['nom']]:
                score += 1
        
        if st.button("Voir mon score final"):
            st.balloons()
            st.metric("Score final", f"{score}/{len(celebs)}")
