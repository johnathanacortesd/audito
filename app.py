import streamlit as st
import streamlit.components.v1 as components

# --- FUNCIÓN PARA LA CONTRASEÑA ---
def check_password():
    """Devuelve True si el usuario ha introducido la contraseña correcta."""

    def password_entered():
        """Comprueba si la contraseña introducida por el usuario es correcta."""
        if st.session_state["password"] == st.secrets["APP_PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # No almacenar la contraseña en el estado
        else:
            st.session_state["password_correct"] = False

    # Si la contraseña aún no ha sido validada, mostrar el campo para introducirla
    if "password_correct" not in st.session_state or not st.session_state["password_correct"]:
        st.text_input(
            "Ingresa la contraseña para acceder", type="password", on_change=password_entered, key="password"
        )
        if "password_correct" in st.session_state and not st.session_state["password_correct"]:
            st.error("😕 Contraseña incorrecta. Por favor, inténtalo de nuevo.")
        return False
    else:
        return True

# --- CÓDIGO PRINCIPAL DE LA APP ---

# Título de la página que se ve en la pestaña del navegador
st.set_page_config(page_title="App de Transcripción", layout="wide")

# Verificar la contraseña
if check_password():
    # Si la contraseña es correcta, mostramos el contenido
    st.title("🎙️ App de Transcripción de Audio con Whisper")
    st.write("Esta aplicación te permite utilizar dos versiones del modelo Whisper de OpenAI para transcribir archivos de audio. Simplemente sube tu archivo en la opción que prefieras.")

    # --- OPCIÓN 1: Whisper Large V3 Turbo ---
    st.header("Opción 1: Whisper Large v3 Turbo (Más rápido)")
    st.markdown("Este modelo está optimizado para una mayor velocidad.")

    # Código del iframe para el primer modelo
    iframe_code_1 = """
    <iframe
        src="https://hf-audio-whisper-large-v3-turbo.hf.space"
        frameborder="0"
        width="100%"
        height="800"
    ></iframe>
    """
    components.html(iframe_code_1, height=820, scrolling=True)


    # --- OPCIÓN 2: Whisper Large V3 ---
    st.header("Opción 2: Whisper Large v3 (Estándar)")
    st.markdown("Este es el modelo base, puede ser ligeramente más lento.")

    # Código del iframe para el segundo modelo
    iframe_code_2 = """
    <iframe
        src="https://hf-audio-whisper-large-v3.hf.space"
        frameborder="0"
        width="100%"
        height="600"
    ></iframe>
    """
    components.html(iframe_code_2, height=620, scrolling=True)
