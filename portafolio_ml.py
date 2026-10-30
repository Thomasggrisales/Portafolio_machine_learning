import streamlit as st
from PIL import Image

# Configuración opcional para que la página use todo el ancho disponible
st.set_page_config(page_title="Portafolio ML", layout="wide")

st.title("Portafolio de Machine Learning")
st.markdown("---")

with st.sidebar:
    st.title("Sobre este portafolio")
    st.info(
        "El Machine Learning permite a los sistemas aprender de los datos para "
        "identificar patrones, hacer predicciones y clasificar información sin "
        "ser programados explícitamente para cada tarea."
    )
    st.divider()
    st.subheader("Recursos adicionales")
    st.write("En el siguiente enlace puedes encontrar más páginas y ejercicios prácticos:")
    st.link_button("Ir a los ejercicios", "https://sites.google.com/view/aplicacionesdeia/inicio", use_container_width=True)

# Creamos las 3 columnas
col1, col2, col3 = st.columns(3)

# ================= COLUMNA 1 =================
with col1:
    with st.container(border=True):
        st.subheader("Predictor en vivo")
        try:
            st.image(Image.open("predictor.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Ecuación Normal vs Gradiente Descendente.")
        st.link_button("Ver Aplicación", "https://machinelearningclass.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Consumo vs Hora")
        try:
            st.image(Image.open("knn.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Clasificación de datos usando el algoritmo KNN.")
        st.link_button("Ver Aplicación", "https://machinelearnings4.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Regresión a Red Neuronal")
        try:
            st.image(Image.open("proyecto7.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Exploración de neuronas artificiales y funciones de activación.")
        st.link_button("Ver Aplicación", "https://machinelearnings7.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Recomendador Semántico")
        try:
            st.image(Image.open("proyecto10.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Búsqueda por significado dentro de un diccionario de referencia.")
        st.link_button("Ver Aplicación", "https://machinelearnings10.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("RNN: Consumo de energía")
        try:
            st.image(Image.open("proyecto13.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Predicción de energía con patrón semanal usando redes recurrentes.")
        st.link_button("Ver Aplicación", "https://machinelearnings13.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Reconocimiento de Imágenes")
        try:
            st.image(Image.open("proyecto16.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Uso de modelos entrenados previamente en Teachable Machine.")
        st.link_button("Ver Aplicación", "https://machinelearnings16visioncomb.streamlit.app/", use_container_width=True)

# ================= COLUMNA 2 =================
with col2:
    with st.container(border=True):
        st.subheader("Predictor de Seguro")
        try:
            st.image(Image.open("predictor_compra.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Predicción de compra de seguros usando datos históricos.")
        st.link_button("Ver Aplicación", "https://machinelearnings2class.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Árboles de Decisión")
        try:
            st.image(Image.open("arboles.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Demostración del funcionamiento de un árbol de decisión.")
        st.link_button("Ver Aplicación", "https://machinelearnings5.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Reconocimiento MNIST")
        try:
            st.image(Image.open("proyecto8.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Identificación de dígitos manuscritos subiendo tu propio modelo.")
        st.link_button("Ver Aplicación", "https://machinelearnings8.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Texto a Audio")
        try:
            st.image(Image.open("proyecto11.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Conversión automática de texto escrito a formato de audio.")
        st.link_button("Ver Aplicación", "https://machinelearnings11.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Generador LSTM")
        try:
            st.image(Image.open("proyecto14.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Generación de texto mediante Redes Neuronales Recurrentes.")
        st.link_button("Ver Aplicación", "https://machinelearnings14.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Chatbot AI")
        try:
            st.image(Image.open("chat.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Interfaz conversacional impulsada por inteligencia artificial.")
        st.link_button("Ver Aplicación", "https://machinelearnings17chat.streamlit.app/", use_container_width=True)

# ================= COLUMNA 3 =================
with col3:
    with st.container(border=True):
        st.subheader("Agrupamiento K-Means")
        try:
            st.image(Image.open("k-means.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Técnicas de clusterización agrupando datos con K-Means.")
        st.link_button("Ver Aplicación", "https://machinelearnings3.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Consumo de energía")
        try:
            st.image(Image.open("energia.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Análisis gráfico del consumo total frente a la hora del día.")
        st.link_button("Ver Aplicación", "https://machinelearnings6.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Análisis de Sentimiento")
        try:
            st.image(Image.open("proyecto9.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Medición de la polaridad y subjetividad de fragmentos de texto.")
        st.link_button("Ver Aplicación", "https://machinelearnings9.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Traductor por Voz")
        try:
            st.image(Image.open("proyecto12.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Sistema que escucha el audio y traduce según tu configuración.")
        st.link_button("Ver Aplicación", "https://machinelearnings12.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Detección YOLOv5")
        try:
            st.image(Image.open("proyecto15.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Detección de objetos en tiempo real en imágenes usando YOLOv5.")
        st.link_button("Ver Aplicación", "https://machinelearnings15yolov5.streamlit.app/", use_container_width=True)

    with st.container(border=True):
        st.subheader("Vision Quest")
        try:
            st.image(Image.open("visionquest.png"), use_column_width=True)
        except FileNotFoundError:
            st.warning("Imagen no disponible")
        st.caption("Exploración profunda interactiva de la aplicación Vision Quest.")
        st.link_button("Ver Aplicación", "https://machinelearninfgs18visionquest.streamlit.app/", use_container_width=True)
