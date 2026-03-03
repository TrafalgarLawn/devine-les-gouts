import streamlit as st

st.set_page_config(page_title="Le Test des Goûts", page_icon="📸")

# Base de données avec des liens Imgur (beaucoup plus stables pour l'affichage direct)
celebs = [
    # --- CAUCASIENNES ---
    {"nom": "Margot Robbie", "url": "https://i.imgur.com/Bf79X76.jpg"},
    {"nom": "Scarlett Johansson", "url": "https://i.imgur.com/f0WfNId.jpg"},
    {"nom": "Ana de Armas", "url": "https://i.imgur.com/vH9v5m6.jpg"},
    {"nom": "Zendaya", "url": "https://i.imgur.com/v8tT9oX.jpg"},
    {"nom": "Jenna Ortega", "url": "https://i.imgur.com/9C0D39B.jpg"},
    {"nom": "Sydney Sweeney", "url": "https://i.imgur.com/7YfL7kC.jpg"},
    {"nom": "Emma Watson", "url": "https://i.imgur.com/fMvC3Uu.jpg"},
    {"nom": "Jennifer Lawrence", "url": "https://i.imgur.com/Xp7A8O3.jpg"},
    {"nom": "Kristen Stewart", "url": "https://i.imgur.com/mO2XpYp.jpg"},
    {"nom": "Florence Pugh", "url": "https://i.imgur.com/9796Y8V.jpg"},
    {"nom": "Taylor Swift", "url": "https://i.imgur.com/6S6MshJ.jpg"},
    {"nom": "Gal Gadot", "url": "https://i.imgur.com/6L0X66y.jpg"},
    {"nom": "Elizabeth Olsen", "url": "https://i.imgur.com/B9qGf9u.jpg"},
    {"nom": "Lily-Rose Depp", "url": "https://i.imgur.com/fVzXm9v.jpg"},
    {"nom": "Elle Fanning", "url": "https://i.imgur.com/hY6W9O9.jpg"},

    # --- ASIATIQUES ---
    {"nom": "Jisoo", "url": "https://i.imgur.com/mE0q9tB.jpg"},
    {"nom": "Hoyeon Jung", "url": "https://i.imgur.com/D8mU2C7.jpg"},
    {"nom": "Dilraba Dilmurat", "url": "https://i.imgur.com/pYv6S9m.jpg"},
    {"nom": "Anna Sawai", "url": "https://i.imgur.com/fW9Z9D9.jpg"},
    {"nom": "Gemma Chan", "url": "https://i.imgur.com/8Yv6Z9S.jpg"},
]

st.title("🎯 Le Jeu des Goûts")
st.markdown("### Devine si cette personne plaît à ton ami !")

tab1, tab2 = st.tabs(["🔒 MODE AMI (Réglages)", "🎮 MODE JOUEUR (Le Quiz)"])

with tab1:
    st.header("Section réservée à l'ami")
    st.write("Coche 'Oui' ou 'Non' pour chaque photo.")
    choices = {}
    for person in celebs:
        st.subheader(person['nom'])
        st.image(person['url'], width=300)
        res = st.radio(f"Est-ce qu'elle te plaît ?", ["Non", "Oui"], key=f"ami_{person['nom']}")
        choices[person['nom']] = res
        st.write("---")
    
    if st.button("Valider mes goûts"):
        st.session_state['votes_ami'] = choices
        st.success("C'est enregistré ! Passe le téléphone au suivant.")

with tab2:
    if 'votes_ami' not in st.session_state:
        st.warning("L'ami doit d'abord enregistrer ses choix dans l'onglet 1.")
    else:
        st.header("Le test de connaissance !")
        score = 0
        for person in celebs:
            st.image(person['url'], width=300)
            dev = st.radio(f"D'après toi, est-ce qu'elle plaît à ton ami ?", ["Non", "Oui"], key=f"jeu_{person['nom']}")
            if dev == st.session_state['votes_ami'][person['nom']]:
                score += 1
            st.write("---")
        
        if st.button("Afficher mon score"):
            st.balloons()
            total = len(celebs)
            st.metric("Résultat final", f"{score} / {total}")
            if score == total:
                st.success("L'âme sœur ! Tu connais tout !")
            elif score > total/2:
                st.info("Pas mal, tu as l'essentiel.")
            else:
                st.error("Tu devrais peut-être plus lui parler...")
