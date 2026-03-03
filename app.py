import streamlit as st

st.set_page_config(page_title="Le Test des Goûts", page_icon="📸")

# --- CONFIGURATION ---
USER = "TrafalgarLawn" 
REPO = "devine-les-gouts"
CODE_SECRET = "6969"

# Ta liste de célébrités avec les extensions vérifiées
CELEBS_DATA = [
    {"nom": "Margot Robbie", "ext": "jpg"}, {"nom": "Scarlett Johansson", "ext": "jpg"},
    {"nom": "Ana de Armas", "ext": "jpg"}, {"nom": "Zendaya", "ext": "jpg"},
    {"nom": "Jenna Ortega", "ext": "jpg"}, {"nom": "Sydney Sweeney", "ext": "jpg"},
    {"nom": "Emma Watson", "ext": "jpg"}, {"nom": "Jennifer Lawrence", "ext": "jpg"},
    {"nom": "Kristen Stewart", "ext": "jpg"}, {"nom": "Florence Pugh", "ext": "jpg"},
    {"nom": "Taylor Swift", "ext": "jpg"}, {"nom": "Gal Gadot", "ext": "jpg"},
    {"nom": "Elizabeth Olsen", "ext": "jpg"}, {"nom": "Lily-Rose Depp", "ext": "jpg"},
    {"nom": "Elle Fanning", "ext": "png"}, {"nom": "Jisoo", "ext": "jpg"},
    {"nom": "Hoyeon Jung", "ext": "jpg"}, {"nom": "Dilraba Dilmurat", "ext": "jpg"},
    {"nom": "Anna Sawai", "ext": "jpg"}, {"nom": "Gemma Chan", "ext": "jpg"}
]

def get_github_url(index):
    ext = CELEBS_DATA[index]["ext"]
    return f"https://raw.githubusercontent.com/{USER}/{REPO}/main/images/{index+1}.{ext}"

st.title("🎯 Le Jeu des Goûts")
st.write("---")

tab1, tab2 = st.tabs(["🔒 MODE AMI", "🎮 MODE JOUEUR"])

with tab1:
    st.header("L'ami choisit ses préférences")
    choices = {}
    for i, person in enumerate(CELEBS_DATA):
        st.subheader(person['nom'])
        st.image(get_github_url(i), width=300)
        res = st.radio(f"Elle te plaît ?", ["Non", "Oui"], key=f"ami_{i}")
        choices[person['nom']] = res
        st.divider()
    
    if st.button("Enregistrer mes choix"):
        st.session_state['votes_ami'] = choices
        st.success("Choix enregistrés ! L'ami peut passer le téléphone.")

with tab2:
    if 'votes_ami' not in st.session_state:
        st.warning("L'ami doit d'abord voter dans l'onglet 1.")
    else:
        # --- SYSTÈME DE VÉROUILLAGE ---
        if 'authentifie' not in st.session_state:
            st.session_state['authentifie'] = False

        if not st.session_state['authentifie']:
            st.subheader("🔐 Section protégée")
            saisie = st.text_input("Entre le code secret pour jouer :", type="password")
            if st.button("Valider le code"):
                if saisie == CODE_SECRET:
                    st.session_state['authentifie'] = True
                    st.rerun() # Relance pour afficher le jeu
                else:
                    st.error("Code incorrect !")
        else:
            # --- LE JEU (Une fois déverrouillé) ---
            st.success("Accès autorisé ! Devine les goûts de ton ami.")
            score = 0
            for i, person in enumerate(CELEBS_DATA):
                st.image(get_github_url(i), width=300)
                dev = st.radio(f"Ça lui plaît ({person['nom']}) ?", ["Non", "Oui"], key=f"jeu_{i}")
                if dev == st.session_state['votes_ami'][person['nom']]:
                    score += 1
                st.divider()
            
            if st.button("Voir mon Score Final"):
                st.balloons()
                st.metric("Résultat", f"{score} / {len(CELEBS_DATA)}")
                
                # Bouton pour refermer la session si besoin
                if st.button("Se déconnecter / Verrouiller"):
                    st.session_state['authentifie'] = False
                    st.rerun()
