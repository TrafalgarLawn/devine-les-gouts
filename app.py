import streamlit as st

st.set_page_config(page_title="Le Test des Goûts", page_icon="📸")

# --- CONFIGURATION ---
USER = "TrafalgarLawn" 
REPO = "devine-les-gouts"
CODE_SECRET = "6969"

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

# Initialisation des variables de session si elles n'existent pas
if 'authentifie' not in st.session_state:
    st.session_state['authentifie'] = False
if 'votes_ami' not in st.session_state:
    st.session_state['votes_ami'] = None

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
        st.success("Choix enregistrés ! Passe le téléphone au joueur.")

with tab2:
    if st.session_state['votes_ami'] is None:
        st.warning("L'ami doit d'abord voter dans l'onglet 1.")
    else:
        # Si pas encore authentifié, on affiche le formulaire de code
        if not st.session_state['authentifie']:
            with st.form("form_login"):
                st.subheader("🔐 Section protégée")
                code_saisi = st.text_input("Entre le code secret pour débloquer le test :", type="password")
                submit = st.form_submit_button("Valider")
                
                if submit:
                    if code_saisi == CODE_SECRET:
                        st.session_state['authentifie'] = True
                        st.rerun()
                    else:
                        st.error("Code incorrect ! Réessaie.")
        
        # Si authentifié, on affiche le jeu
        else:
            st.success("Accès autorisé !")
            if st.button("🔴 Verrouiller à nouveau"):
                st.session_state['authentifie'] = False
                st.rerun()
                
            st.write("---")
            score = 0
            for i, person in enumerate(CELEBS_DATA):
                st.image(get_github_url(i), width=300)
                dev = st.radio(f"Est-ce que ça lui plaît ({person['nom']}) ?", ["Non", "Oui"], key=f"jeu_{i}")
                if dev == st.session_state['votes_ami'][person['nom']]:
                    score += 1
                st.divider()
            
            if st.button("Calculer mon Score Final"):
                st.balloons()
                st.metric("Résultat", f"{score} / {len(CELEBS_DATA)}")
