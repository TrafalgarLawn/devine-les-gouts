import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Le Test des Goûts", page_icon="📸", layout="centered")

# Base de données avec plus de noms (mélange Caucasiennes / Asiatiques)
celebs = [
    {"nom": "Margot Robbie", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Margot_Robbie_at_2019_Cannes_Film_Festival.jpg/800px-Margot_Robbie_at_2019_Cannes_Film_Festival.jpg"},
    {"nom": "Jisoo (Blackpink)", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Kim_Ji-soo_at_a_press_conference_for_Snowdrop_in_December_2021.jpg/800px-Kim_Ji-soo_at_a_press_conference_for_Snowdrop_in_December_2021.jpg"},
    {"nom": "Zendaya", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Zendaya_at_the_2019_Emmy_Awards.jpg/800px-Zendaya_at_the_2019_Emmy_Awards.jpg"},
    {"nom": "Hoyeon Jung", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Jung_Ho-yeon_at_2022_Critics_Choice_Awards.jpg/800px-Jung_Ho-yeon_at_2022_Critics_Choice_Awards.jpg"},
    {"nom": "Scarlett Johansson", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Scarlett_Johansson_by_Gage_Skidmore_2.jpg/800px-Scarlett_Johansson_by_Gage_Skidmore_2.jpg"},
    {"nom": "Dilraba Dilmurat", "img": "https://upload.wikimedia.org/wikipedia/commons/1/1d/Dilraba_Dilmurat_at_the_2019_Cosmo_Glam_Night.jpg"},
    {"nom": "Jennifer Lawrence", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Jennifer_Lawrence_in_2016.jpg/800px-Jennifer_Lawrence_in_2016.jpg"},
    {"nom": "Anna Sawai", "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Anna_Sawai_2024.jpg/800px-Anna_Sawai_2024.jpg"},
]

st.title("🎯 Le Jeu des Goûts")
st.write("---")

# Système d'onglets
tab1, tab2 = st.tabs(["🔒 MODE AMI (Choix)", "🎮 MODE JOUEUR (Devine)"])

with tab1:
    st.header("L'ami choisit ses préférences")
    st.info("Réponds honnêtement, les autres ne voient pas tes réponses ici !")
    
    choices = {}
    for person in celebs:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(person['img'], width=150)
        with col2:
            st.subheader(person['nom'])
            res = st.radio(f"Elle te plaît ?", ["Non", "Oui"], key=f"ami_{person['nom']}")
            choices[person['nom']] = res
        st.write("---")
    
    if st.button("Enregistrer mes choix définitifs"):
        st.session_state['votes_ami'] = choices
        st.success("C'est enregistré ! Donne maintenant le téléphone/PC au joueur.")

with tab2:
    if 'votes_ami' not in st.session_state:
        st.warning("L'ami doit d'abord remplir l'onglet 'MODE AMI' !")
    else:
        st.header("Alors, tu connais bien ses goûts ?")
        score = 0
        
        for person in celebs:
            st.image(person['img'], width=300)
            devinette = st.radio(f"Est-ce que tu penses qu'elle plaît à ton ami ?", ["Non", "Oui"], key=f"jeu_{person['nom']}")
            
            # Vérification (cachée jusqu'à la fin)
            if devinette == st.session_state['votes_ami'][person['nom']]:
                score += 1
            st.write("---")
        
        if st.button("Calculer mon Score final"):
            st.balloons()
            st.markdown(f"## Ton score : {score} / {len(celebs)}")
            
            performance = (score / len(celebs)) * 100
            if performance == 100:
                st.success("Incroyable ! Tu le/la connais par cœur !")
            elif performance >= 50:
                st.info("Pas mal ! Tu as une bonne intuition.")
            else:
                st.error("Ouh là... Tu ne connais pas du tout ses goûts !")
