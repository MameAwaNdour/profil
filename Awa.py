import streamlit as st

# ------------------ Données du CV ------------------ #
fonction = "GEOMATICIEN"
nom = "Mame Awa Ndour"
adresse = "Thiaroye "
email = "ndour1662@gmail.com"

objectif = (
    "Étudiant en 2eme année en géomatique au Centre d'Entreprenariat et de "
    "Développement Technique, je souhaite mettre en pratique mes compétences "
    "et engranger de l'expérience au près de votre entreprise."
)

diplomes = [
    "Technicien Supérieur en géomatique – CEDT le G15 – 2026",
    "Baccalauréat – Lycée de mbao – 2021",
    "BFEM – Lycée de Bokhol  – 2019"
]

competences = [
    "Capacité à manipuler PostgreSQL, WampServer pour la création de bases de données",
    "Connaissance en Système d’Information Géographique",
    "Confection de cartes sur QGIS et ArcGIS",
    "Confection de plans 2D avec AutoCAD et 3D avec SketchUp",
    "Collecte de données avec drone",
    "Collecte de données avec téléphone (Mobile Topographer, QField, Locus GIS, MGRS UTM GPS, UTM GEO MAP)",
    "Collecte de données avec Station Totale Robotisée et GPS différentiel",
    "Capacité à piloter un drone",
    "Traitement d'images de drone avec Agisoft Metashape, PIX4D Mapper, Global Mapper",
    "Connaissance en webmapping (HTML)",
    "Connaissance en télédétection",
    "Traitement d'images satellitaires avec Erdas Imagine et ENVI",
    "Maîtrise des logiciels bureautiques : Word, Excel, PowerPoint, Access"
]

langues = [
    "Français : bonne maîtrise",
    "Anglais : maîtrise moyenne"
]



# ------------------ Interface Streamlit ------------------ #

st.set_page_config(page_title="CV", page_icon="📄", layout="wide")

# En-tête
st.title("Mame Awa Ndour")
st.header(fonction)
st.subheader("Ndour")

col1, col2, col3 , col4 = st.columns(4)
with col1:
    st.markdown(f"Nom : {nom}")
with col2:
    st.markdown(f"Adresse : {adresse}")
with col3:
    
with col4:
    st.markdown(f"Email : {email}")

st.markdown("---")

# Objectif
st.header("Objectif professionnel")
st.write(objectif)

# Diplômes
st.header("Diplômes et études")
for d in diplomes:
    st.markdown(f"- {d}")

# Compétences
st.header("Compétences")
for c in competences:
    st.markdown(f"- {c}")

# Langues et divers en colonnes
col_lang, col_div = st.columns(2)

with col_lang:
    st.header("Langues")
    for l in langues:
        st.markdown(f"- {l}")

with col_div:
    st.header("Divers")
    for d in divers:
        st.markdown(f"- {d}")


    st.markdown(f"- {l}")