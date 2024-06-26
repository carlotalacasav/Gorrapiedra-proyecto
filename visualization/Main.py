import streamlit as st

st.set_page_config(
    page_title="Bike Availability Prediction",
    page_icon="👋",
)

st.title("Capstone Project")
st.subheader("Bike Availability Prediction")
st.sidebar.success("Select a page above.")

st.write("""
Benvinguts al nostre projecte de predicció de disponibilitat de bicicletes, fet per Carlota Lacasa, Alejandro Jaramillo, Alba Martínez i Marina Dalmau.

Més enllà del repositori de github amb els models, hem utilitzat streamlit per visualitzar resultats, tant d'anàlisi com de prediccions obtingudes al llarg del treball.
Això ens ha permès entendre amb més deteniment les dades i mostrar de forma més elaborada les observacions.
         
""")

st.markdown("""
#### Pàgines disponibles:

**👋 Home**
   - Aquesta pàgina serveix com a introducció al projecte. Aquí podeu trobar informació general sobre l'objectiu de l'aplicació de streamlit.

**🔋 Analysis by Capacity**
   - En aquesta secció es presenta l'anàlisi de la disponibilitat de bicicletes basada en la capacitat de les estacions. Inclou gràfics i taules per entendre millor com la capacitat afecta la disponibilitat.

**📍 Analysis by PostCode**
   - Aquesta pàgina mostra l'anàlisi de la disponibilitat de bicicletes segons el codi postal. Permet visualitzar les dades de diferents regions per identificar patrons i tendències.

**⌛ Analysis by Time**
   - En aquesta secció es presenta l'anàlisi temporal de la disponibilitat de bicicletes. Inclou gràfics que mostren com varia la disponibilitat al llarg dels anys, mesos, dies i fins i tot hores.

**🍂 Analysis by Weather**
   - Aquesta pàgina explora la relació entre les condicions climàtiques i la disponibilitat de bicicletes. S'hi poden trobar dades sobre com factors com la temperatura o la pluja influeixen en la disponibilitat.    

Gràcies per visitar el nostre projecte!
""")

st.markdown("""
### Referències
- [streamlit-folium](https://folium.streamlit.app/)
""")
