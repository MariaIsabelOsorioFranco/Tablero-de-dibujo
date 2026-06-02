import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de página
st.set_page_config(page_title="DRAAW Pink", page_icon="🌸")

st.title("DRAAW 🌸")

# Estilos Rosa Pastel
st.markdown("""
<style>
/* Fondo degradado rosa pastel */
.stApp {
    background: linear-gradient(135deg, #fce7f3, #fbcfe8, #fdf2f8);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f9a8d4 !important;
}

h1, h2, h3 {
    color: #9d174d !important;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.subheader("🎨 Propiedades del tablero")
    
    st.subheader("Tamaño del tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)
    
    drawing_mode = st.selectbox(
        "Trazos",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )
    
    stroke_width = st.slider("Selecciona el tamaño de tu Trazo", 1, 30, 15)
    
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color del fondo", "#000000")

# Canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 105, 180, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)
