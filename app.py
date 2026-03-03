import streamlit as st

st.set_page_config(page_title="Le Test des Goûts", page_icon="📸")

# --- CONFIGURATION ---
USER = "TrafalgarLawn" 
REPO = "devine-les-gouts"
CODE_SECRET = "6969"

NOMS = [
    "Margot Robbie", "Scarlett Johansson", "Ana de Armas", "Zendaya", "Jenna Ortega",
    "Sydney Sweeney", "Emma Watson", "Jennifer Lawrence", "Kristen Stewart", "Florence Pugh",
    "Taylor Swift", "Gal Gadot", "Elizabeth Olsen", "Lily-Rose Depp", "Elle Fanning",
    "Jisoo", "Hoyeon Jung", "Dilraba Dilmurat", "Anna Sawai", "Gemma Chan"
]

def get_github_url(index):
    # Mise à jour du chemin pour inclure le dossier /images/
    return f"https://raw.githubusercontent.com/{USER}/{REPO}/main/images/{index+1}.jpg"

st.title("🎯 Le Jeu des Goûts")
st.write("---")

tab1, tab2 = st.tabs(["🔒 MODE AMI", "🎮 MODE JOUEUR"])

with tab1:
    st.header("L'ami choisit ses préférences")
    choices = {}
    for i, nom in enumerate(NOMS):
        st.subheader(nom)
        st.image(get_github_url(i), width=300)
        res = st.radio(f"Elle te plaît ?", ["Non", "Oui"], key=f"ami_{i}")
        choices[nom] = res
        st.divider()
    
    if st.button("Enregistrer mes choix"):
        st.session_state['votes_ami'] = choices
        st.success("Choix enregistrés ! L'onglet Joueur est maintenant verrouillé.")

with tab2:
    if 'votes_ami' not in st.session_state:
        st.warning("L'ami doit d'abord voter dans l'onglet 1.")
    else:
        st.header("Zone Protégée")
        
        # Système de vérification du code
        if 'auth_joueur' not in st.session_state:
            st.session_state['auth_joueur'] = False

        if not st.session_state['auth_joueur']:
            saisie = st.text_input("Entre le code secret pour commencer le test :", type="password")
            if saisie == CODE_SECRET:
                st.session_state['auth_joueur'] = True
                st.rerun()
            elif saisie != "":
                st.error("Code incorrect !")
        else:
            # Si le code est bon, on affiche le jeu
            st.success("Code correct ! Bonne chance.")
            score = 0
            for i, nom in enumerate(NOMS):
                st.image(get_github_url(i), width=300)
                dev = st.radio(f"Ça lui plaît ({nom}) ?", ["Non", "Oui"], key=f"jeu_{i}")
                if dev == st.session_state['votes_ami'][nom]:
                    score += 1
                st.divider()
            
            if st.button("Voir mon Score"):
                st.balloons()
                st.metric("Résultat final", f"{score} / {len(NOMS)}")
                
                # Option pour réinitialiser et cacher à nouveau le jeu
                if st.button("Terminer et verrouiller"):
                    st.session_state['auth_joueur'] = False
                    st.rerun()
