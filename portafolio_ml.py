import streamlit as st
from PIL import Image, ImageOps

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

# ================= FUNCIÓN PARA ESTANDARIZAR IMÁGENES =================
def procesar_imagen(ruta):
    """
    Abre la imagen y la recorta a un formato 16:9 (ej. 800x450)
    centrando el contenido. Evita barras de scroll en los contenedores.
    """
    try:
        img = Image.open(ruta)
        # Ajusta el tamaño de recorte (ancho, alto). 800x450 mantiene proporción 16:9.
        img_estandar = ImageOps.fit(img, (800, 450), Image.Resampling.LANCZOS)
        return img_estandar
    except FileNotFoundError:
        return None

# Creamos las 3 columnas
col1, col2, col3 = st.columns(3)

# Definimos una altura estándar ajustada para las tarjetas
ALTO_TARJETA = 420

# ================= COLUMNA 1 =================
with col1:
    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Predictor en vivo")
        img = procesar_imagen("predictor.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Ecuación Normal vs Gradiente Descendente.")
        st.link_button("Ver Aplicación", "https://machinelearningclass.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Consumo vs Hora")
        img = procesar_imagen("knn.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Clasificación de datos usando el algoritmo KNN.")
        st.link_button("Ver Aplicación", "https://machinelearnings4.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Regresión a Red Neuronal")
        img = procesar_imagen("proyecto7.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Exploración de neuronas artificiales y funciones de activación.")
        st.link_button("Ver Aplicación", "https://machinelearnings7.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Recomendador Semántico")
        img = procesar_imagen("proyecto10.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Búsqueda por significado dentro de un diccionario de referencia.")
        st.link_button("Ver Aplicación", "https://machinelearnings10.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("RNN: Consumo de energía")
        img = procesar_imagen("proyecto13.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Predicción de energía con patrón semanal usando redes recurrentes.")
        st.link_button("Ver Aplicación", "https://machinelearnings13.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Reconocimiento de Imágenes")
        img = procesar_imagen("proyecto16.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Uso de modelos entrenados previamente en Teachable Machine.")
        st.link_button("Ver Aplicación", "https://machinelearnings16visioncomb.streamlit.app/", use_container_width=True)

# ================= COLUMNA 2 =================
with col2:
    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Predictor de Seguro")
        img = procesar_imagen("predictor_compra.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Predicción de compra de seguros usando datos históricos.")
        st.link_button("Ver Aplicación", "https://machinelearnings2class.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Árboles de Decisión")
        img = procesar_imagen("arboles.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Demostración del funcionamiento de un árbol de decisión.")
        st.link_button("Ver Aplicación", "https://machinelearnings5.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Reconocimiento MNIST")
        img = procesar_imagen("proyecto8.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Identificación de dígitos manuscritos subiendo tu propio modelo.")
        st.link_button("Ver Aplicación", "https://machinelearnings8.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Texto a Audio")
        img = procesar_imagen("proyecto11.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Conversión automática de texto escrito a formato de audio.")
        st.link_button("Ver Aplicación", "https://machinelearnings11.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Generador LSTM")
        img = procesar_imagen("proyecto14.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Generación de texto mediante Redes Neuronales Recurrentes.")
        st.link_button("Ver Aplicación", "https://machinelearnings14.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Chatbot AI")
        img = procesar_imagen("chat.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Interfaz conversacional impulsada por inteligencia artificial.")
        st.link_button("Ver Aplicación", "https://machinelearnings17chat.streamlit.app/", use_container_width=True)

# ================= COLUMNA 3 =================
with col3:
    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Agrupamiento K-Means")
        img = procesar_imagen("k-means.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Técnicas de clusterización agrupando datos con K-Means.")
        st.link_button("Ver Aplicación", "https://machinelearnings3.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Consumo de energía")
        img = procesar_imagen("energia.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Análisis gráfico del consumo total frente a la hora del día.")
        st.link_button("Ver Aplicación", "https://machinelearnings6.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Análisis de Sentimiento")
        img = procesar_imagen("proyecto9.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Medición de la polaridad y subjetividad de fragmentos de texto.")
        st.link_button("Ver Aplicación", "https://machinelearnings9.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Traductor por Voz")
        img = procesar_imagen("proyecto12.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Sistema que escucha el audio y traduce según tu configuración.")
        st.link_button("Ver Aplicación", "https://machinelearnings12.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Detección YOLOv5")
        img = procesar_imagen("proyecto15.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Detección de objetos en tiempo real en imágenes usando YOLOv5.")
        st.link_button("Ver Aplicación", "https://machinelearnings15yolov5.streamlit.app/", use_container_width=True)

    with st.container(border=True, height=ALTO_TARJETA):
        st.subheader("Vision Quest")
        img = procesar_imagen("visionquest.png")
        if img: st.image(img, use_column_width=True)
        else: st.warning("Imagen no disponible")
        st.caption("Exploración profunda interactiva de la aplicación Vision Quest.")
        st.link_button("Ver Aplicación", "https://machinelearninfgs18visionquest.streamlit.app/", use_container_width=True)
