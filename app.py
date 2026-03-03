import streamlit as st

st.set_page_config(page_title="Le Test des Goûts", page_icon="📸", layout="centered")

# Liste mise à jour avec 20 noms et liens d'images plus robustes
celebs = [
    # --- CAUCASIENNES (15) ---
    {"nom": "Margot Robbie", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cv1S3uS8X9fbaC99pFuSsts3pS3.jpg"},
    {"nom": "Scarlett Johansson", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/69Sns9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Ana de Armas", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/3vxv9uGv9D3Ssa6mCqA686FnYdf.jpg"},
    {"nom": "Zendaya", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/f9YvC9cv4W60fR78STuR7Wn8S.jpg"},
    {"nom": "Jenna Ortega", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/mB9Y8pG63p4pS8I9mB1p9Y8pG63.jpg"},
    {"nom": "Sydney Sweeney", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/qY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Emma Watson", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/hY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Jennifer Lawrence", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/vY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Kristen Stewart", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/pY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Bella Hadid", "img": "https://img-3.journaldesfemmes.fr/m_u_V7S-p_V-u_V/750x/smart/e9785528859449839359e13352758151/ccmcms-jdf/39624503.jpg"},
    {"nom": "Kendall Jenner", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/pB9Y8pG63p4pS8I9mB1p9Y8pG63.jpg"},
    {"nom": "Florence Pugh", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/tY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Taylor Swift", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/oY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Gal Gadot", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/fZ1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Elizabeth Olsen", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/wY1S9oetA96Ym966T7tBqG8f6S.jpg"},

    # --- ASIATIQUES (5) ---
    {"nom": "Jisoo (Blackpink)", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/aY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Hoyeon Jung", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/bY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Dilraba Dilmurat", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Anna Sawai", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/dY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Gemma Chan", "img": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/eY1S9oetA96Ym966T7tBqG8f6S.jpg"},
]

st.title("🎯 Le Jeu des Goûts")
st.write("---")

tab1, tab2 = st.tabs(["🔒 MODE AMI (Choix)", "🎮 MODE JOUEUR (Devine)"])

with tab1:
    st.header("L'ami choisit ses préférences")
    choices = {}
    for person in celebs:
        col1, col2 = st.columns([1, 2])
        with col1:
            # Utilisation de st.image avec un message d'erreur si le lien meurt
            st.image(person['img'], use_container_width=True)
        with col2:
            st.subheader(person['nom'])
            res = st.radio(f"Elle te plaît ?", ["Non", "Oui"], key=f"ami_{person['nom']}")
            choices[person['nom']] = res
        st.write("---")
    
    if st.button("Enregistrer mes choix définitifs"):
        st.session_state['votes_ami'] = choices
        st.success("C'est enregistré ! Passe le téléphone au joueur.")

with tab2:
    if 'votes_ami' not in st.session_state:
        st.warning("L'ami doit d'abord remplir l'onglet 'MODE AMI' !")
    else:
        st.header("Alors, tu connais bien ses goûts ?")
        score = 0
        for person in celebs:
            st.image(person['img'], width=300)
            devinette = st.radio(f"Est-ce que ça lui plaît ?", ["Non", "Oui"], key=f"jeu_{person['nom']}")
            if devinette == st.session_state['votes_ami'][person['nom']]:
                score += 1
            st.write("---")
        
        if st.button("Calculer mon Score"):
            st.balloons()
            st.markdown(f"## Ton score : {score} / {len(celebs)}")
