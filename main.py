import streamlit as st

# Título de la aplicación
st.title("IdeaSpark")

# Archivo CSS para estilos
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Formulario para que el usuario ingrese sus intereses y habilidades
with st.form("idea_form"):
    # Intereses del usuario
    intereses = st.text_input("Tus Intereses (ej: IA, Educación):")

    # Habilidades del usuario
    habilidades = st.text_input("Tus Habilidades (ej: Python, NLP):")

    # Botón para generar ideas
    submitted = st.form_submit_button("Generar Ideas")

    # Función placeholder para generar ideas (se implementará más tarde)
    def generar_ideas(intereses, habilidades):
        # Aquí irá la lógica para conectar con Gemini o un modelo similar
        # y generar ideas de negocio basadas en los intereses y habilidades.
        # Por ahora, solo devolvemos un mensaje placeholder.
        return "Las ideas se mostrarán aquí."

    # Mostrar un mensaje cuando se haga clic en el botón
    if submitted:
        # Llama a la función generar_ideas (placeholder)
        ideas = generar_ideas(intereses, habilidades)

        # Muestra las ideas generadas (placeholder)
        st.write(ideas)