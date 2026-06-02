import os
import streamlit as st
import base64
from openai import OpenAI
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Función para codificar la imagen
def encode_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except FileNotFoundError:
        return "Error: Imagen no encontrada."

# Configuración de página
st.set_page_config(page_title='NeuroPanel Rosa', page_icon="🌸", layout="wide")

# Estilos Rosita Pastel
st.markdown("""
<style>
    /* Fondo rosa pastel */
    .stApp {
        background: linear-gradient(135deg, #fce7f3, #fbcfe8);
    }
    
    /* Sidebar rosa */
    section[data-testid="stSidebar"] {
        background-color: #f9a8d4 !important;
    }
    
    h1, h2, h3 {
        color: #9d174d !important;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    .stButton>button {
        background-color: #ec4899 !important;
        color: white !important;
        border-radius: 20px !important;
        border: none;
        font-weight: bold;
    }
    
    .stTextInput>div>div>input {
        border: 2px solid #f472b6 !important;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Título y presentación
st.title('🌸 NeuroPanel Pink')
with st.sidebar:
    st.subheader("¡Bienvenido!")
    st.write("Tu asistente creativo para interpretar bocetos usando Inteligencia Artificial.")

st.subheader("Dibuja tu idea aquí y deja que la IA la interprete")

# Configuración del Canvas
stroke_width = st.sidebar.slider('Grosor del trazo', 1, 30, 8)
canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 1)",
    stroke_width=stroke_width,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=300,
    width=400,
    drawing_mode="freedraw",
    key="canvas_rosita",
)

# API Key
ke = st.text_input('🔑 Ingresa tu Clave de OpenAI', type="password")
analyze_button = st.button("✨ Analizar mi dibujo", type="primary")

# Procesamiento
if canvas_result.image_data is not None and ke and analyze_button:
    client = OpenAI(api_key=ke)
    
    with st.spinner("🎀 Procesando tu boceto con ternura..."):
        # Guardar y codificar
        input_numpy_array = canvas_result.image_data.astype('uint8')
        input_image = Image.fromarray(input_numpy_array, 'RGBA')
        input_image.save('boceto_rosa.png')
        base64_image = encode_image_to_base64("boceto_rosa.png")
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe de manera creativa y amable en español qué aparece en este dibujo."},
                        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
                    ]
                }]
            )
            
            respuesta = response.choices[0].message.content
            st.markdown("### 🎀 Resultado del Análisis:")
            st.success(respuesta)
            
        except Exception as e:
            st.error(f"Ups, ocurrió algo: {e}")

elif analyze_button and not ke:
    st.warning("⚠️ Necesito tu clave API para empezar la magia.")
