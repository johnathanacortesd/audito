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

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Variables de colores */
    :root {
        --primary-color: #6C63FF;
        --secondary-color: #FF6B6B;
        --success-color: #4ECDC4;
        --dark-bg: #1a1a2e;
        --card-bg: #16213e;
        --text-light: #e0e0e0;
    }
    
    /* Fondo principal con gradiente */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Estilo para los contenedores principales */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: slideDown 0.5s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Tarjetas de contenido */
    .feature-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.5);
    }
    
    /* Botones personalizados */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Animación de pulso para elementos importantes */
    @keyframes pulse {
        0% {
            box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.7);
        }
        70% {
            box-shadow: 0 0 0 10px rgba(102, 126, 234, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(102, 126, 234, 0);
        }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite;
    }
    
    /* Indicador de estado */
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        margin-right: 8px;
        animation: blink 2s infinite;
    }
    
    .status-active {
        background-color: #4ECDC4;
    }
    
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Tabs personalizados */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 10px;
        border-radius: 15px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 10px;
        color: white;
        font-weight: 600;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Alertas personalizadas */
    .stAlert {
        border-radius: 10px;
        border-left: 4px solid #667eea;
    }
    
    /* Input de contraseña */
    .stTextInput > div > div > input[type="password"] {
        border-radius: 10px;
        border: 2px solid #667eea;
        padding: 10px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input[type="password"]:focus {
        border-color: #764ba2;
        box-shadow: 0 0 0 3px rgba(118, 75, 162, 0.1);
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
                <div style='text-align: center; padding: 3rem; background: rgba(255,255,255,0.95); 
                border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin-top: 5rem;'>
                    <h2 style='color: #667eea; margin-bottom: 1rem;'>🔐 Acceso Seguro</h2>
                    <p style='color: #666; margin-bottom: 2rem;'>Ingresa tu contraseña para continuar</p>
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
        <div class='main-header' style='text-align: center;'>
            <h1 style='color: white; font-size: 3rem; margin-bottom: 0.5rem;'>
                🎙️ TranscribeAI Pro
            </h1>
            <p style='color: rgba(255,255,255,0.9); font-size: 1.2rem;'>
                Transcripción de audio potenciada por Whisper de OpenAI
            </p>
            <div style='margin-top: 1rem;'>
                <span class='status-indicator status-active'></span>
                <span style='color: rgba(255,255,255,0.8);'>Sistema operativo</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Botones de acción rápida
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📖 Ver Instrucciones", use_container_width=True):
            st.session_state.show_instructions = not st.session_state.show_instructions
    
    with col2:
        if st.button("🚀 Activar Modelo Alternativo", use_container_width=True):
            st.session_state.show_option2 = not st.session_state.show_option2
            if st.session_state.show_option2:
                st.success("✅ Modelo alternativo activado")
    
    with col3:
        if st.button("🔄 Recargar Aplicación", use_container_width=True):
            st.rerun()
    
    with col4:
        if st.button("ℹ️ Acerca de", use_container_width=True):
            st.info("TranscribeAI Pro v2.0 - Powered by OpenAI Whisper")
    
    # Mostrar instrucciones si está activado
    if st.session_state.show_instructions:
        with st.container():
            st.markdown("""
                <div class='feature-card'>
                    <h3 style='color: #667eea;'>📚 Guía de Uso Rápido</h3>
                    <hr style='border-color: #e0e0e0;'>
                    <h4>🎯 Cómo usar TranscribeAI Pro:</h4>
                    <ol style='line-height: 1.8;'>
                        <li><strong>Prepara tu archivo:</strong> Asegúrate de que tu audio esté en formato MP3, WAV, M4A o MP4</li>
                        <li><strong>Selecciona el modelo:</strong>
                            <ul>
                                <li>🚀 <strong>Turbo:</strong> Más rápido, ideal para transcripciones urgentes</li>
                                <li>🎯 <strong>Estándar:</strong> Mayor precisión, recomendado para contenido complejo</li>
                            </ul>
                        </li>
                        <li><strong>Carga tu archivo:</strong> Arrastra o selecciona tu archivo en el área designada</li>
                        <li><strong>Espera el resultado:</strong> La transcripción aparecerá automáticamente</li>
                        <li><strong>Descarga:</strong> Copia o descarga el texto transcrito</li>
                    </ol>
                    
                    <h4 style='margin-top: 1.5rem;'>💡 Consejos Pro:</h4>
                    <ul style='line-height: 1.8;'>
                        <li>✨ Para mejores resultados, usa archivos con audio claro y mínimo ruido de fondo</li>
                        <li>⏱️ Los archivos más largos tardarán más en procesarse</li>
                        <li>🌍 Whisper soporta múltiples idiomas automáticamente</li>
                        <li>🔧 Si el modelo principal falla, activa el modelo alternativo con el botón superior</li>
                    </ul>
                    
                    <h4 style='margin-top: 1.5rem;'>⚠️ Limitaciones:</h4>
                    <ul style='line-height: 1.8;'>
                        <li>📏 Tamaño máximo de archivo: 25 MB (modelo Turbo) / 50 MB (modelo Estándar)</li>
                        <li>⏳ Duración máxima recomendada: 30 minutos</li>
                        <li>📁 Formatos soportados: MP3, WAV, M4A, MP4, WEBM, OGG</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    
    # Separador visual
    st.markdown("<hr style='border: 1px solid rgba(255,255,255,0.2); margin: 2rem 0;'>", unsafe_allow_html=True)
    
    # Tabs para los modelos
    tab1, tab2 = st.tabs(["🚀 Modelo Turbo (Recomendado)", "🎯 Modelo Estándar"])
    
    with tab1:
        st.markdown("""
            <div class='feature-card'>
                <h3 style='color: #667eea;'>⚡ Whisper Large v3 Turbo</h3>
                <p style='color: #666;'>
                    <strong>Velocidad optimizada</strong> - Ideal para transcripciones rápidas con excelente precisión.
                    Procesamiento hasta 2x más rápido que el modelo estándar.
                </p>
                <div style='display: flex; gap: 1rem; margin-top: 1rem;'>
                    <span style='background: #e8f5e9; color: #2e7d32; padding: 0.25rem 0.75rem; border-radius: 20px;'>
                        ⚡ Alta velocidad
                    </span>
                    <span style='background: #fff3e0; color: #f57c00; padding: 0.25rem 0.75rem; border-radius: 20px;'>
                        🎯 95% precisión
                    </span>
                    <span style='background: #e3f2fd; color: #1976d2; padding: 0.25rem 0.75rem; border-radius: 20px;'>
                        🌍 50+ idiomas
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Iframe del modelo Turbo
        with st.spinner('Cargando modelo Turbo...'):
            iframe_code_turbo = """
            <iframe
                src="https://hf-audio-whisper-large-v3-turbo.hf.space"
                frameborder="0"
                width="100%"
                height="700"
                style="border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);"
            ></iframe>
            """
            components.html(iframe_code_turbo, height=720, scrolling=True)
    
    with tab2:
        if st.session_state.show_option2:
            st.markdown("""
                <div class='feature-card'>
                    <h3 style='color: #764ba2;'>🎯 Whisper Large v3 Estándar</h3>
                    <p style='color: #666;'>
                        <strong>Máxima precisión</strong> - Modelo completo para transcripciones detalladas.
                        Recomendado para contenido técnico o con terminología especializada.
                    </p>
                    <div style='display: flex; gap: 1rem; margin-top: 1rem;'>
                        <span style='background: #fce4ec; color: #c2185b; padding: 0.25rem 0.75rem; border-radius: 20px;'>
                            🎯 Máxima precisión
                        </span>
                        <span style='background: #f3e5f5; color: #7b1fa2; padding: 0.25rem 0.75rem; border-radius: 20px;'>
                            📝 Puntuación mejorada
                        </span>
                        <span style='background: #e0f2f1; color: #00796b; padding: 0.25rem 0.75rem; border-radius: 20px;'>
                            🔍 Detección de hablantes
                        </span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            # Iframe del modelo Estándar
            with st.spinner('Cargando modelo Estándar...'):
                iframe_code_standard = """
                <iframe
                    src="https://hf-audio-whisper-large-v3.hf.space"
                    frameborder="0"
                    width="100%"
                    height="600"
                    style="border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);"
                ></iframe>
                """
                components.html(iframe_code_standard, height=620, scrolling=True)
        else:
            st.markdown("""
                <div class='feature-card' style='text-align: center; padding: 3rem;'>
                    <h3 style='color: #764ba2;'>🔒 Modelo Estándar Desactivado</h3>
                    <p style='color: #666; margin: 1.5rem 0;'>
                        Este modelo está actualmente desactivado para optimizar el rendimiento.
                        <br>Actívalo solo si necesitas máxima precisión o si el modelo Turbo no está disponible.
                    </p>
                    <p style='color: #999; font-size: 0.9rem;'>
                        💡 Tip: Usa el botón "🚀 Activar Modelo Alternativo" en la parte superior para habilitarlo
                    </p>
                </div>
                """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
        <div style='text-align: center; margin-top: 3rem; padding: 2rem; 
        background: rgba(255,255,255,0.1); border-radius: 15px;'>
            <p style='color: rgba(255,255,255,0.8);'>
                Desarrollado con ❤️ usando Streamlit y OpenAI Whisper
                <br>
                <small>© 2024 TranscribeAI Pro - Todos los derechos reservados</small>
            </p>
        </div>
        """, unsafe_allow_html=True)
