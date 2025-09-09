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
    
    /* Tarjetas de contenido modo oscuro */
    .dark-card {
        background: #1E293B;
        border-radius: 16px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        border: 1px solid #334155;
        transition: all 0.3s ease;
    }
    
    .dark-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 50px rgba(124, 58, 237, 0.3);
        border-color: #7C3AED;
    }
    
    /* Tarjeta de instrucciones específica */
    .instructions-card {
        background: linear-gradient(135deg, #1E293B 0%, #334155 100%);
        border-radius: 20px;
        padding: 2.5rem;
        margin: 2rem 0;
        border: 2px solid #7C3AED;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
    }
    
    .instructions-card h3 {
        color: #A78BFA !important;
        font-size: 1.8rem;
        margin-bottom: 1rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .instructions-card h4 {
        color: #C4B5FD !important;
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-size: 1.3rem;
    }
    
    .instructions-card p, 
    .instructions-card li,
    .instructions-card span {
        color: #E0E7FF !important;
        line-height: 1.8;
        font-size: 1.05rem;
    }
    
    .instructions-card strong {
        color: #FBBF24 !important;
        font-weight: 600;
    }
    
    .instructions-card ul, 
    .instructions-card ol {
        margin-left: 1.5rem;
    }
    
    .instructions-card li {
        margin: 0.8rem 0;
    }
    
    .instructions-card hr {
        border-color: #7C3AED !important;
        margin: 1.5rem 0;
        opacity: 0.3;
    }
    
    /* Highlight especial para el primer paso */
    .first-step {
        background: linear-gradient(135deg, #7C3AED20 0%, #EC489920 100%);
        border: 2px solid #7C3AED;
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin: 1.5rem 0;
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
    
    .feature-badge:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
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
    
    .model-card h3 {
        color: #F1F5F9 !important;
        margin-bottom: 1rem;
    }
    
    .model-card p {
        color: #CBD5E1 !important;
        line-height: 1.6;
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
    
    /* Animación de pulso */
    @keyframes pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(124, 58, 237, 0.7);
        }
        70% {
            box-shadow: 0 0 0 15px rgba(124, 58, 237, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(124, 58, 237, 0);
        }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
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
    
    /* Tabs personalizados modo oscuro */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #1E293B;
        padding: 12px;
        border-radius: 16px;
        border: 1px solid #334155;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 12px;
        color: #CBD5E1 !important;
        font-weight: 600;
        padding: 12px 24px;
        transition: all 0.3s ease;
        border: 1px solid transparent;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(124, 58, 237, 0.1);
        border-color: #7C3AED;
        color: #F1F5F9 !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #7C3AED 0%, #6D28D9 100%);
        color: white !important;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.4);
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
    
    .stTextInput > div > div > input[type="password"]::placeholder {
        color: #64748B !important;
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
    
    .login-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(124, 58, 237, 0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
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
    
    /* Alertas y mensajes */
    .stAlert {
        background: #1E293B !important;
        color: #F1F5F9 !important;
        border-radius: 12px;
        border-left: 4px solid #7C3AED;
        border: 1px solid #334155;
    }
    
    div[data-testid="stExpander"] {
        background: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
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
        # Contenedor de login mejorado
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
                <div class='login-container'>
                    <h2 style='color: #F1F5F9; margin-bottom: 1rem; text-align: center; font-size: 2.5rem; position: relative; z-index: 1;'>
                        🔐 Acceso Seguro
                    </h2>
                    <p style='color: #CBD5E1; margin-bottom: 2rem; text-align: center; position: relative; z-index: 1;'>
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
                <span style='color: rgba(255,255,255,0.9); font-weight: 500;'>Sistema operativo • Conectado a GitHub</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Botones de acción rápida
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📖 Ver Instrucciones", use_container_width=True, key="btn_instructions"):
            st.session_state.show_instructions = not st.session_state.show_instructions
    
    with col2:
        if st.button("🚀 Activar Modelo Alternativo", use_container_width=True, key="btn_model"):
            st.session_state.show_option2 = not st.session_state.show_option2
            if st.session_state.show_option2:
                st.success("✅ Modelo alternativo activado correctamente")
    
    with col3:
        if st.button("🔄 Recargar Aplicación", use_container_width=True, key="btn_reload"):
            st.rerun()
    
    with col4:
        if st.button("ℹ️ Acerca de", use_container_width=True, key="btn_about"):
            st.info("TranscribeAI Pro v2.0 - Desarrollado con Streamlit y OpenAI Whisper")
    
    # Mostrar instrucciones si está activado
    if st.session_state.show_instructions:
        with st.container():
            st.markdown("""
                <div class='instructions-card'>
                    <h3>📚 Guía Completa de Uso</h3>
                    <hr>
                    
                    <div class='first-step'>
                        <h4>🎯 Paso 1: Acceder a la interfaz de carga</h4>
                        <p><strong>IMPORTANTE:</strong> En la interfaz de Hugging Face que aparece abajo:</p>
                        <ol>
                            <li>Haz clic en la pestaña <strong>"Audio file"</strong> (no en "Microphone")</li>
                            <li>Aparecerá el botón para cargar tu archivo de audio</li>
                            <li>Selecciona o arrastra tu archivo de audio</li>
                        </ol>
                    </div>
                    
                    <h4>📋 Pasos completos para transcribir:</h4>
                    <ol>
                        <li><strong>Selecciona el modelo:</strong>
                            <ul>
                                <li>🚀 <strong>Turbo (Pestaña 1):</strong> 2x más rápido, ideal para la mayoría de casos</li>
                                <li>🎯 <strong>Estándar (Pestaña 2):</strong> Mayor precisión para contenido técnico</li>
                            </ul>
                        </li>
                        <li><strong>Carga tu archivo:</strong>
                            <ul>
                                <li>Haz clic en <strong>"Audio file"</strong> en la interfaz de abajo</li>
                                <li>Selecciona tu archivo (MP3, WAV, M4A, MP4, WEBM, OGG)</li>
                                <li>Espera a que se cargue completamente</li>
                            </ul>
                        </li>
                        <li><strong>Configura opciones (opcional):</strong>
                            <ul>
                                <li>Task: Selecciona "transcribe" o "translate"</li>
                                <li>Return timestamps: Activa si necesitas marcas de tiempo</li>
                            </ul>
                        </li>
                        <li><strong>Inicia la transcripción:</strong>
                            <ul>
                                <li>Haz clic en el botón <strong>"Submit"</strong></li>
                                <li>Espera el procesamiento (la velocidad depende del tamaño)</li>
                            </ul>
                        </li>
                        <li><strong>Obtén tu resultado:</strong>
                            <ul>
                                <li>El texto aparecerá en el área de resultados</li>
                                <li>Puedes copiarlo directamente con el botón de copiar</li>
                            </ul>
                        </li>
                    </ol>
                    
                    <h4>💡 Consejos Profesionales:</h4>
                    <ul>
                        <li>✨ <strong>Calidad de audio:</strong> Archivos con audio claro dan mejores resultados</li>
                        <li>🎯 <strong>Idioma automático:</strong> Whisper detecta el idioma automáticamente</li>
                        <li>⏱️ <strong>Tiempo de procesamiento:</strong> ~1 minuto por cada 10 minutos de audio en modo Turbo</li>
                        <li>🔄 <strong>Si falla:</strong> Activa el modelo alternativo con el botón superior</li>
                        <li>📝 <strong>Puntuación:</strong> El modelo añade puntuación automáticamente</li>
                    </ul>
                    
                    <h4>⚠️ Limitaciones Técnicas:</h4>
                    <ul>
                        <li>📏 <strong>Tamaño máximo:</strong> 25 MB (Turbo) / 50 MB (Estándar)</li>
                        <li>⏳ <strong>Duración máxima:</strong> 30 minutos recomendado</li>
                        <li>📁 <strong>Formatos:</strong> MP3, WAV, M4A, MP4, WEBM, OGG</li>
                        <li>🌐 <strong>Conexión:</strong> Requiere internet estable</li>
                    </ul>
                    
                    <h4>🆘 Solución de Problemas:</h4>
                    <ul>
                        <li>Si el modelo no responde → Recarga la página</li>
                        <li>Si el archivo no se carga → Verifica el formato y tamaño</li>
                        <li>Si la transcripción es incorrecta → Prueba el modelo Estándar</li>
                        <li>Si hay timeout → Divide el audio en partes más pequeñas</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    
    # Separador visual
    st.markdown("<hr style='border: 1px solid #334155; margin: 3rem 0;'>", unsafe_allow_html=True)
    
    # Tabs para los modelos
    tab1, tab2 = st.tabs(["🚀 Modelo Turbo (Recomendado)", "🎯 Modelo Estándar"])
    
    with tab1:
        st.markdown("""
            <div class='model-card'>
                <h3>⚡ Whisper Large v3 Turbo</h3>
                <p>
                    Versión optimizada para velocidad sin sacrificar calidad. 
                    Procesamiento hasta 2x más rápido manteniendo una precisión del 95%.
                </p>
                <div style='margin-top: 1.5rem;'>
                    <span class='feature-badge badge-speed'>⚡ Alta velocidad</span>
                    <span class='feature-badge badge-accuracy'>🎯 95% precisión</span>
                    <span class='feature-badge badge-language'>🌍 50+ idiomas</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Aviso importante
        st.info("💡 **Recuerda:** Haz clic en la pestaña **'Audio file'** en la interfaz de abajo para cargar tu archivo")
        
        # Iframe del modelo Turbo
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
    
    with tab2:
        if st.session_state.show_option2:
            st.markdown("""
                <div class='model-card'>
                    <h3>🎯 Whisper Large v3 Estándar</h3>
                    <p>
                        Modelo completo con máxima precisión. Ideal para contenido técnico, 
                        múltiples hablantes o terminología especializada.
                    </p>
                    <div style='margin-top: 1.5rem;'>
                        <span class='feature-badge badge-accuracy'>🏆 Máxima precisión</span>
                        <span class='feature-badge badge-language'>📝 Puntuación mejorada</span>
                        <span class='feature-badge badge-speed'>🔍 Detección de contexto</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Aviso importante
            st.info("💡 **Recuerda:** Haz clic en la pestaña **'Audio file'** en la interfaz de abajo para cargar tu archivo")
            
            # Iframe del modelo Estándar
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
            st.markdown("""
                <div class='dark-card' style='text-align: center; padding: 4rem;'>
                    <h3 style='color: #F1F5F9; margin-bottom: 1.5rem;'>🔒 Modelo Estándar Desactivado</h3>
                    <p style='color: #CBD5E1; margin-bottom: 2rem; font-size: 1.1rem;'>
                        Este modelo está desactivado para optimizar el rendimiento de la aplicación.
                        <br><br>
                        Actívalo solo si necesitas máxima precisión o si el modelo Turbo no está disponible.
                    </p>
                    <div class='pulse-animation' style='display: inline-block; padding: 1rem 2rem; 
                         background: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%); 
                         border-radius: 12px; margin-top: 1rem;'>
                        <p style='color: white; margin: 0; font-weight: 600;'>
                            👆 Usa el botón "Activar Modelo Alternativo" arriba
                        </p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Footer mejorado
    st.markdown("""
        <div class='footer'>
            <p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>
                Desarrollado con ❤️ usando Streamlit y OpenAI Whisper
            </p>
            <p style='font-size: 0.9rem; opacity: 0.8;'>
                © 2024 TranscribeAI Pro • Conectado a GitHub • v2.0
            </p>
        </div>
        """, unsafe_allow_html=True)
