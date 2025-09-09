import streamlit as st
import streamlit.components.v1 as components
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="TranscribeAI Pro", 
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS PERSONALIZADOS MODO OSCURO ---
st.markdown("""
    <style>
    /* Variables de colores para modo oscuro */
    :root {
        --primary-color: #7C3AED;
        --secondary-color: #EC4899;
        --success-color: #10B981;
        --bg-dark: #0F172A;
        --card-dark: #1E293B;
        --text-primary: #F1F5F9;
        --text-secondary: #CBD5E1;
        --border-color: #334155;
    }
    
    /* Fondo principal oscuro con gradiente sutil */
    .stApp {
        background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
    }
    
    /* Header principal */
    .main-header {
        background: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%);
        padding: 2.5rem;
        border-radius: 24px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(124, 58, 237, 0.3);
        animation: slideDown 0.6s ease-out;
        border: 1px solid rgba(124, 58, 237, 0.2);
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Modelo card específico */
    .model-card {
        background: #1E293B;
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
        border: 1px solid #334155;
        position: relative;
        overflow: hidden;
    }
    
    .model-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #7C3AED, #EC4899);
    }
    
    /* Badges de características */
    .feature-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.3rem;
        font-weight: 600;
        font-size: 0.9rem;
        border: 1px solid;
        transition: all 0.3s ease;
    }
    
    .badge-speed {
        background: rgba(16, 185, 129, 0.2);
        color: #10B981;
        border-color: #10B981;
    }
    
    .badge-accuracy {
        background: rgba(251, 191, 36, 0.2);
        color: #FBBF24;
        border-color: #FBBF24;
    }
    
    .badge-language {
        background: rgba(59, 130, 246, 0.2);
        color: #3B82F6;
        border-color: #3B82F6;
    }
    
    /* Botones personalizados modo oscuro */
    .stButton > button {
        background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%);
        color: white !important;
        border: 1px solid #7C3AED;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #6D28D9 0%, #7C3AED 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(124, 58, 237, 0.5);
        border-color: #A78BFA;
    }
    
    /* Indicador de estado */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
        background: #10B981;
        box-shadow: 0 0 10px #10B981;
        animation: blink 2s infinite;
    }
    
    @keyframes blink {
        0%, 100% { 
            opacity: 1; 
            box-shadow: 0 0 10px #10B981;
        }
        50% { 
            opacity: 0.5;
            box-shadow: 0 0 5px #10B981;
        }
    }
    
    /* Input de contraseña modo oscuro */
    .stTextInput > div > div > input[type="password"] {
        background: #1E293B !important;
        border: 2px solid #334155 !important;
        color: #F1F5F9 !important;
        border-radius: 12px;
        padding: 12px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input[type="password"]:focus {
        border-color: #7C3AED !important;
        box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.2);
        background: #0F172A !important;
    }
    
    /* Login container */
    .login-container {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border-radius: 24px;
        padding: 3rem;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
        border: 2px solid #7C3AED;
        margin-top: 5rem;
        position: relative;
        overflow: hidden;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        margin-top: 4rem;
        padding: 2.5rem;
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border-radius: 20px;
        border: 1px solid #334155;
        color: #94A3B8;
    }
    
    /* Contenedor desactivado */
    .disabled-container {
        background: #1E293B;
        border-radius: 16px;
        padding: 3rem;
        text-align: center;
        border: 2px dashed #334155;
        margin: 2rem 0;
    }
    
    /* Animación de pulso */
    @keyframes pulse {
        0% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
        100% {
            transform: scale(1);
        }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    /* Mejoras para los iframes */
    iframe {
        border-radius: 16px !important;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.5) !important;
        border: 2px solid #334155 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIÓN PARA LA CONTRASEÑA ---
def check_password():
    """Devuelve True si el usuario ha introducido la contraseña correcta."""
    def password_entered():
        """Comprueba si la contraseña introducida por el usuario es correcta."""
        if st.session_state["password"] == st.secrets["APP_PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False
    
    if "password_correct" not in st.session_state or not st.session_state["password_correct"]:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div class='login-container'>
                    <h2 style='color: #F1F5F9; margin-bottom: 1rem; text-align: center; font-size: 2.5rem;'>
                        🔐 Acceso Seguro
                    </h2>
                    <p style='color: #CBD5E1; margin-bottom: 2rem; text-align: center;'>
                        Ingresa tu contraseña para acceder a TranscribeAI Pro
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            st.text_input(
                "Contraseña", 
                type="password", 
                on_change=password_entered, 
                key="password",
                placeholder="Introduce tu contraseña aquí..."
            )
            
            if "password_correct" in st.session_state and not st.session_state["password_correct"]:
                st.error("🚫 Contraseña incorrecta. Por favor, inténtalo de nuevo.")
        
        return False
    else:
        return True

# --- INICIALIZAR ESTADOS ---
if 'show_option2' not in st.session_state:
    st.session_state.show_option2 = False

if 'show_instructions' not in st.session_state:
    st.session_state.show_instructions = False

if 'show_turbo' not in st.session_state:
    st.session_state.show_turbo = True

# --- CÓDIGO PRINCIPAL DE LA APP ---
if check_password():
    # Header principal con animación
    st.markdown("""
        <div class='main-header'>
            <h1 style='color: white; font-size: 3.5rem; margin-bottom: 0.5rem; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);'>
                🎙️ TranscribeAI Pro
            </h1>
            <p style='color: rgba(255,255,255,0.95); font-size: 1.3rem; text-align: center;'>
                Transcripción de audio profesional con Whisper de OpenAI
            </p>
            <div style='text-align: center; margin-top: 1.5rem;'>
                <span class='status-indicator'></span>
                <span style='color: rgba(255,255,255,0.9); font-weight: 500;'>Sistema operativo</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Solo 4 botones principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("⚡ Modelo Rápido", use_container_width=True, help="Activar modelo Turbo"):
            st.session_state.show_turbo = True
            st.session_state.show_option2 = False
            st.session_state.show_instructions = False
            st.success("✅ Modelo Turbo activado")
    
    with col2:
        if st.button("🎯 Modelo Alternativo", use_container_width=True, help="Activar modelo Estándar"):
            st.session_state.show_option2 = True
            st.session_state.show_turbo = False
            st.session_state.show_instructions = False
            st.success("✅ Modelo Estándar activado")
    
    with col3:
        if st.button("📖 Instrucciones", use_container_width=True, help="Ver guía de uso"):
            st.session_state.show_instructions = not st.session_state.show_instructions
            if st.session_state.show_instructions:
                st.session_state.show_turbo = False
                st.session_state.show_option2 = False
    
    with col4:
        if st.button("🔄 Recargar", use_container_width=True, help="Reiniciar aplicación"):
            st.session_state.show_instructions = False
            st.rerun()
    
    # Separador visual
    st.markdown("<hr style='border: 1px solid #334155; margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Mostrar contenido según el estado
    if st.session_state.show_instructions:
        # Mostrar las instrucciones
        st.markdown("""
            ### 🎯 Cómo transcribir tu audio en 5 pasos:
            
            **1️⃣ Primero lo primero:**
            En la interfaz que aparece abajo, busca y haz clic en la pestaña que dice **"Audio file"** 
            (no uses "Microphone"). Esto es súper importante para poder cargar tu archivo.
            
            **2️⃣ Sube tu archivo:**
            Una vez en "Audio file", verás un botón para cargar. Puedes arrastrar tu archivo 
            o hacer clic para buscarlo en tu computadora. Acepta archivos MP3, WAV, M4A, MP4 y más.
            
            **3️⃣ Espera que cargue:**
            Verás una barra de progreso mientras se sube el archivo. Si tu archivo es grande, puede tomar unos segundos.
            Una vez cargado, aparecerá el nombre del archivo y el botón **"Submit"** debajo.
            
            **4️⃣ Dale a transcribir:**
            Cuando termine de cargar, haz clic en el botón **"Submit"** o **"Transcribe"**.
            El modelo empezará a trabajar su magia 🪄
            
            **5️⃣ ¡Listo! Copia tu texto:**
            El resultado aparecerá en la caja de texto de abajo. Puedes copiarlo con el 
            botón de copiar o seleccionarlo todo con Ctrl+A (o Cmd+A en Mac).
            
            ---
            
            ### 💡 Tips para mejores resultados:
            
            🎤 **Audio limpio = mejor transcripción**
            Entre menos ruido de fondo, mejor será el resultado.
            
            ⏱️ **Paciencia con archivos largos**
            Un podcast de 30 minutos puede tardar 2-3 minutos en procesarse.
            
            🌍 **Funciona en cualquier idioma**
            Whisper detecta automáticamente el idioma. ¡Habla en español, inglés o lo que quieras!
            
            📝 **Puntuación automática**
            No te preocupes por los puntos y comas, el modelo los añade solo.
            
            ---
            
            ### ⚠️ Límites a tener en cuenta:
            
            📦 **Tamaño máximo:** 25 MB para el modelo rápido, 50 MB para el alternativo
            
            ⏳ **Duración recomendada:** Hasta 30 minutos para mejores resultados
            
            🔌 **Necesitas internet:** La transcripción se hace en la nube
            
            ---
            
            ### 🆘 ¿Algo no funciona?
            
            😵 **Si no responde:** Dale al botón "🔄 Recargar" arriba
            
            🐢 **Si va muy lento:** Prueba el "⚡ Modelo Rápido"
            
            ❌ **Si da error:** Verifica que tu archivo no pase de 25 MB
            
            🔄 **Si necesitas más precisión:** Cambia al "🎯 Modelo Alternativo"
            """)
    
    elif st.session_state.show_turbo:
        # Mostrar modelo Turbo
        st.markdown("""
            <div class='model-card'>
                <h3 style='color: #F1F5F9;'>⚡ Modelo Turbo - Activo</h3>
                <p style='color: #CBD5E1;'>
                    Versión optimizada para velocidad. Procesa hasta 2x más rápido con excelente precisión.
                </p>
                <div style='margin-top: 1.5rem;'>
                    <span class='feature-badge badge-speed'>⚡ Alta velocidad</span>
                    <span class='feature-badge badge-accuracy'>🎯 95% precisión</span>
                    <span class='feature-badge badge-language'>🌍 50+ idiomas</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.info("💡 **Recuerda:** Haz clic en la pestaña **'Audio file'** en la interfaz de abajo para cargar tu archivo")
        
        with st.spinner('⏳ Cargando modelo Turbo...'):
            iframe_code_turbo = """
            <iframe
                src="https://hf-audio-whisper-large-v3-turbo.hf.space"
                frameborder="0"
                width="100%"
                height="750"
                style="border-radius: 16px; box-shadow: 0 15px 40px rgba(0,0,0,0.5); border: 2px solid #334155;"
            ></iframe>
            """
            components.html(iframe_code_turbo, height=770, scrolling=True)
    
    elif st.session_state.show_option2:
        # Mostrar modelo Estándar
        st.markdown("""
            <div class='model-card'>
                <h3 style='color: #F1F5F9;'>🎯 Modelo Estándar - Activo</h3>
                <p style='color: #CBD5E1;'>
                    Modelo completo con máxima precisión. Ideal para contenido técnico o con múltiples hablantes.
                </p>
                <div style='margin-top: 1.5rem;'>
                    <span class='feature-badge badge-accuracy'>🏆 Máxima precisión</span>
                    <span class='feature-badge badge-language'>📝 Puntuación mejorada</span>
                    <span class='feature-badge badge-speed'>🔍 Mejor contexto</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.info("💡 **Recuerda:** Haz clic en la pestaña **'Audio file'** en la interfaz de abajo para cargar tu archivo")
        
        with st.spinner('⏳ Cargando modelo Estándar...'):
            iframe_code_standard = """
            <iframe
                src="https://hf-audio-whisper-large-v3.hf.space"
                frameborder="0"
                width="100%"
                height="650"
                style="border-radius: 16px; box-shadow: 0 15px 40px rgba(0,0,0,0.5); border: 2px solid #334155;"
            ></iframe>
            """
            components.html(iframe_code_standard, height=670, scrolling=True)
    
    else:
        # Ningún modelo seleccionado
        st.markdown("""
            <div class='disabled-container'>
                <h3 style='color: #F1F5F9;'>🤔 Ningún modelo seleccionado</h3>
                <p style='color: #CBD5E1; font-size: 1.1rem; margin-top: 1rem;'>
                    Por favor, selecciona un modelo usando los botones de arriba:
                </p>
                <div style='margin-top: 2rem;' class='pulse-animation'>
                    <p style='color: #A78BFA; font-size: 1.2rem;'>
                        ⚡ Modelo Rápido - Para transcripciones veloces<br>
                        🎯 Modelo Alternativo - Para máxima precisión
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div class='footer'>
            <p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>
                Desarrollado con 🤖 usando Streamlit y OpenAI Whisper
            </p>
            <p style='font-size: 0.9rem; opacity: 0.8;'>
                © 2025 Johnathan Cortés • v2.0
            </p>
        </div>
        """, unsafe_allow_html=True)
