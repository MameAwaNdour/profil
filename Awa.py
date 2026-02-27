import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Mon Portfolio",
    page_icon="💼",
    layout="wide"
)

# Barre latérale
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller vers :", ["Accueil", "À propos", "Projets", "Compétences", "Contact"])

# Page Accueil
if page == "Accueil":
    st.title("👋 Bienvenue sur mon Portfolio")
    st.write("Je suis **Ndour Awa**, passionnée par la technologie et l'innovation.")
    st.image("https://via.placeholder.com/800x300", use_container_width=True)
    st.markdown("### 🚀 Objectif")
    st.write("Créer des solutions innovantes adaptées aux besoins des entreprises.")

# Page À propos
elif page == "À propos":
    st.title("🙋‍♀️ À propos de moi")
    st.write("""
    Je suis spécialisée en :
    - 🌍 Géomatique
    - 📊 Analyse de données
    - 💻 Développement web
    """)
    st.info("Disponible pour des stages et collaborations.")

# Page Projets
elif page == "Projets":
    st.title("📂 Mes Projets")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Projet 1")
        st.write("Application d'analyse spatiale avec Python.")
        st.button("Voir plus")

    with col2:
        st.subheader("Projet 2")
        st.write("Dashboard interactif avec Streamlit.")
        st.button("Voir plus")

# Page Compétences
elif page == "Compétences":
    st.title("🛠 Compétences")

    st.write("### Programmation")
    st.progress(85)
    st.write("Python")

    st.write("### Analyse de données")
    st.progress(75)
    st.write("Pandas, NumPy")

    st.write("### SIG")
    st.progress(80)
    st.write("QGIS, ArcGIS")

# Page Contact
elif page == "Contact":
    st.title("📩 Contact")

    with st.form("contact_form"):
        nom = st.text_input("Votre nom")
        email = st.text_input("Votre email")
        message = st.text_area("Votre message")
        submit = st.form_submit_button("Envoyer")

        if submit:
            st.success("Message envoyé avec succès !")

    st.write("📧 Email : awa.ndour@email.com")
    st.write("🌍 Localisation : Dakar, Sénégal")
