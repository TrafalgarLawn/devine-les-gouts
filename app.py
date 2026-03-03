import streamlit as st

st.set_page_config(page_title="Le Jeu des Goûts", page_icon="📸")

# On utilise un service de redimensionnement/proxy (wsrv.nl) pour forcer l'affichage
def get_proxy_img(url):
    return f"https://wsrv.nl/?url={url}&w=400&output=jpg"

# Liste de 20 célébrités avec liens directs simplifiés
celebs = [
    # CAUCASIENNES
    {"nom": "Margot Robbie", "url": "https://image.tmdb.org/t/p/main/cv1S3uS8X9fbaC99pFuSsts3pS3.jpg"},
    {"nom": "Scarlett Johansson", "url": "https://image.tmdb.org/t/p/main/69Sns9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Ana de Armas", "url": "https://image.tmdb.org/t/p/main/3vxv9uGv9D3Ssa6mCqA686FnYdf.jpg"},
    {"nom": "Jenna Ortega", "url": "https://image.tmdb.org/t/p/main/mB9Y8pG63p4pS8I9mB1p9Y8pG63.jpg"},
    {"nom": "Sydney Sweeney", "url": "https://image.tmdb.org/t/p/main/9979t699p6S6mCqA686FnYdf.jpg"},
    {"nom": "Emma Watson", "url": "https://image.tmdb.org/t/p/main/hY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Jennifer Lawrence", "url": "https://image.tmdb.org/t/p/main/vY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Kristen Stewart", "url": "https://image.tmdb.org/t/p/main/pY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Florence Pugh", "url": "https://image.tmdb.org/t/p/main/tY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Taylor Swift", "url": "https://image.tmdb.org/t/p/main/oY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Gal Gadot", "url": "https://image.tmdb.org/t/p/main/fZ1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Elizabeth Olsen", "url": "https://image.tmdb.org/t/p/main/wY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Lily-Rose Depp", "url": "https://image.tmdb.org/t/p/main/2O9p78STuR7Wn8S.jpg"},
    {"nom": "Elle Fanning", "url": "https://image.tmdb.org/t/p/main/f60fR78STuR7Wn8S.jpg"},
    {"nom": "Victoria Pedretti", "url": "https://image.tmdb.org/t/p/main/mB1p9Y8pG63p4pS8I9mB1p9.jpg"},

    # ASIATIQUES
    {"nom": "Jisoo", "url": "https://image.tmdb.org/t/p/main/aY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Hoyeon Jung", "url": "https://image.tmdb.org/t/p/main/bY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Dilraba Dilmurat", "url": "https://image.tmdb.org/t/p/main/cY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Anna Sawai", "url": "https://image.tmdb.org/t/p/main/dY1S9oetA96Ym966T7tBqG8f6S.jpg"},
    {"nom": "Gemma Chan", "url": "https://image.tmdb.org/t/p/main/eY1S9oetA96Ym966T7tBqG8f6S.jpg"},
]

st.title("🎯 Le Jeu des Goûts")

tab1, tab2 = st.tabs(["🔒 MODE AMI", "🎮 MODE JOUEUR"])

with tab1:
    st.header("Préférences de l'Ami")
    choices = {}
    for person in celebs:
        st.subheader(person['nom'])
        # On force l'affichage via le proxy wsrv.nl
        st.image(get_proxy_img(person['url']), width=250)
        res = st.radio(f"Elle te plaît ?", ["Non", "Oui"], key=f"ami_{person['nom']}")
        choices[person['nom']] = res
        st.divider()
    
    if st.button("Enregistrer les choix"):
        st.session_state['votes_ami'] = choices
        st.success("Choix enregistrés !")

with tab2:
    if 'votes_ami' not in st.session_state:
        st.warning("L'ami doit voter en premier !")
    else:
        st.header("Devine !")
        score = 0
        for person in celebs:
            st.image(get_proxy_img(person['url']), width=250)
            dev = st.radio(f"Est-ce que ça lui plaît ?", ["Non", "Oui"], key=f"jeu_{person['nom']}")
            if dev == st.session_state['votes_ami'][person['nom']]:
                score += 1
            st.divider()
        
        if st.button("Score Final"):
            st.balloons()
            st.markdown(f"### Résultat : {score} / {len(celebs)}")
