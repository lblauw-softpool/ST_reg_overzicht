import streamlit as st
import json

# Maak een lege placeholder voor de titel
title_placeholder = st.empty()
title_placeholder.title("📊 Regressietesten Viewer")

# Sidebar met upload en toggle knop
st.sidebar.header("Bestandsbeheer")
uploaded_file = st.sidebar.file_uploader("Upload hier je testcase JSON-bestand", type="json")

# Initialiseer toggle status in session_state
if 'show_metadata' not in st.session_state:
    st.session_state.show_metadata = False

def toggle_metadata():
    st.session_state.show_metadata = not st.session_state.show_metadata

if uploaded_file is not None:
    try:
        data = json.load(uploaded_file)
        testcase_title = data.get("metadata", {}).get("Testcase", "Onbekende Testcase")

        # Update titel in placeholder
        title_placeholder.title(f"📊 testcase: {testcase_title}")

        # Dynamische knop met toggle functie
        btn_label = "Verberg metadata" if st.session_state.show_metadata else "Toon metadata"
        st.sidebar.button(btn_label, on_click=toggle_metadata)

        # Metadata tonen/verbergen
        if st.session_state.show_metadata:
            st.sidebar.markdown("### Metadata inhoud:")
            metadata = data.get("metadata", {})
            for key, value in metadata.items():
                st.sidebar.markdown(f"- **{key}**: {value}")

    except json.JSONDecodeError:
        st.sidebar.error("Ongeldig JSON bestand, probeer het opnieuw met een correct JSON bestand.")
else:
    st.sidebar.info("Upload een JSON bestand om te beginnen.")
