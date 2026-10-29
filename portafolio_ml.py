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
    image = Image.open("predictor.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos un Predictor en vivo: Ecuación Normal vs Gradiente Descendente")
    url = "https://machinelearningclass.streamlit.app/"
    st.write(f"Predictor: [Enlace]({url})")

    st.subheader("Consumo Total vs Hora del Día")
    image = Image.open("knn.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo clasificar datos usando el algoritmo KNN.")
    url = "https://machinelearnings4.streamlit.app/"
    st.write(f"KNN: [Enlace]({url})")

    st.subheader("Regresión a Red Neuronal")
    image = Image.open("proyecto7.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos qué hace una neurona artificial y su función de activación.")
    url = "https://machinelearnings7.streamlit.app/"
    st.write(f"Red Neuronal: [Enlace]({url})")

    st.subheader("Recomendador Semántico")
    image = Image.open("proyecto10.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos un sistema que busca por significado dentro de un diccionario de referencia.")
    url = "https://machinelearnings10.streamlit.app/"
    st.write(f"Recomendador: [Enlace]({url})")

    st.subheader("RNN: Consumo de energía")
    image = Image.open("proyecto13.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos redes neuronales recurrentes para predecir el consumo de energía con patrón semanal.")
    url = "https://machinelearnings13.streamlit.app/"
    st.write(f"RNN: [Enlace]({url})")

    st.subheader("Reconocimiento de Imágenes")
    image = Image.open("proyecto16.jpg")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos reconocimiento de imágenes usando un modelo entrenado en Teachable Machine.")
    url = "https://machinelearnings16visioncomb.streamlit.app/"
    st.write(f"Reconocimiento: [Enlace]({url})")

with col2:
    st.subheader("Predictor de compra de seguro")
    image = Image.open("predictor_compra.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo predecir la compra de un seguro. ")
    url = "https://machinelearnings2class.streamlit.app/"
    st.write(f"Compra: [Enlace]({url})")

    st.subheader("Árboles de Decisión")
    image = Image.open("arboles.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo funciona un árbol de decisión.")
    url = "https://machinelearnings5.streamlit.app/"
    st.write(f"Árbol de Decisión: [Enlace]({url})")

    st.subheader("Reconocimiento de Dígitos")
    image = Image.open("proyecto8.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos el reconocimiento de dígitos MNIST subiendo tu propio modelo.")
    url = "https://machinelearnings8.streamlit.app/"
    st.write(f"MNIST: [Enlace]({url})")

    st.subheader("Conversión de Texto a Audio")
    image = Image.open("proyecto11.jpg")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo convertir un texto escrito a formato de audio.")
    url = "https://machinelearnings11.streamlit.app/"
    st.write(f"Texto a Audio: [Enlace]({url})")

    st.subheader("Generador de Texto LSTM")
    image = Image.open("proyecto14.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos un generador de texto utilizando Redes Neuronales Recurrentes LSTM.")
    url = "https://machinelearnings14.streamlit.app/"
    st.write(f"LSTM: [Enlace]({url})")

    st.subheader("Chatbot AI")
    image = Image.open("chat.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos una interfaz conversacional o Chatbot.")
    url = "https://machinelearnings17chat.streamlit.app/"
    st.write(f"Chat: [Enlace]({url})")

with col3:
    st.subheader("Agrupamiento con K-Means")
    image = Image.open("k-means.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo agrupar datos usando K-Means.")
    url = "https://machinelearnings3.streamlit.app/"
    st.write(f"K-Means: [Enlace]({url})")

    st.subheader("Consumo de energia")
    image = Image.open("energia.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos el consumo de energia Total vs Hora del Día. ")
    url = "https://machinelearnings6.streamlit.app/"
    st.write(f"Consumo: [Enlace]({url})")

    st.subheader("Análisis de Sentimiento")
    image = Image.open("proyecto9.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos cómo medir la polaridad y subjetividad de un texto.")
    url = "https://machinelearnings9.streamlit.app/"
    st.write(f"Sentimiento: [Enlace]({url})")

    st.subheader("Traductor")
    image = Image.open("proyecto12.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos un traductor que escucha lo que le hablas y lo procesa.")
    url = "https://machinelearnings12.streamlit.app/"
    st.write(f"Traductor: [Enlace]({url})")

    st.subheader("Detección de Objetos en Imágenes")
    image = Image.open("proyecto15.jpg")
    st.image(image, width=190)
    st.write("En el siguiente enlace veremos detección de objetos en imágenes capturadas utilizando YOLOv5.")
    url = "https://machinelearnings15yolov5.streamlit.app/"
    st.write(f"YOLOv5: [Enlace]({url})")

    st.subheader("Vision Quest")
    image = Image.open("visionquest.png")
    st.image(image, width=190)
    st.write("En el siguiente enlace exploraremos la aplicación Vision Quest.")
    url = "https://machinelearninfgs18visionquest.streamlit.app/"
    st.write(f"Vision Quest: [Enlace]({url})")
