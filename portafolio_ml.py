import streamlit as st
from PIL import Image

st.title("Aplicaciones de Machine Learning.")

with st.sidebar:
    st.subheader("Aplicaciones de Machine Learning.")
    parrafo = (
        "El Machine Learning permite a los sistemas aprender de los datos para "
        "identificar patrones, hacer predicciones y clasificar información sin "
        "ser programados explícitamente para cada tarea."
    )
    st.write(parrafo)

url_ml = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ml})")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Predictor en vivo")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("predictor.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos un Predictor en vivo: Ecuación Normal vs Gradiente Descendente")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://machinelearningclass.streamlit.app/"
    st.write(f"Predictor: [Enlace]({url})")

    st.subheader("Consumo Total vs Hora del Día")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("knn.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://machinelearnings4.streamlit.app/"
    st.write(f"KNN: [Enlace]({url})")

    

with col2:
    st.subheader("Predictor de compra de seguro")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("predictor_compra.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo predecir la compra de un seguro. ")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://machinelearnings2class.streamlit.app/"
    st.write(f"Compra: [Enlace]({url})")

    st.subheader("Árboles de Decisión")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("arboles.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://machinelearnings5.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")

with col3:
    st.subheader("Agrupamiento con K-Means")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("k-means.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo agrupar datos usando K-Means.")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://machinelearnings3.streamlit.app/"
    st.write(f"K-Means: [Enlace]({url})")

    st.subheader("Consumo de energia")
    # 👇 REEMPLAZA el nombre del archivo de imagen
    image = Image.open("energia.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos el consumo de energia Total vs Hora del Día. ")
    # 👇 REEMPLAZA la url por la de tu app en Streamlit Cloud
    url = "https://machinelearnings6.streamlit.app/"
    st.write(f"K-Means: [Enlace]({url})")

    
