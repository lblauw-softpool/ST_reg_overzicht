import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("📊 Regressietesten Viewer")

# Bestand uploaden
uploaded_file = st.file_uploader("Kies een Excel-bestand", type=["xlsx", "xls"])

if uploaded_file is not None:
    # Excel inladen
    df = pd.read_excel(uploaded_file)

    # Instellingen
    rows_per_page = 20

    # Houd de huidige pagina bij in de sessie
    if "page" not in st.session_state:
        st.session_state.page = 0

    # Functies voor navigatie
    def next_page():
        if (st.session_state.page + 1) * rows_per_page < len(df):
            st.session_state.page += 1

    def prev_page():
        if st.session_state.page > 0:
            st.session_state.page -= 1

    # Paginering berekenen
    start = st.session_state.page * rows_per_page
    end = start + rows_per_page
    subset = df.iloc[start:end]

    # Weergave
    st.write(f"Toont rijen {start+1} t/m {min(end, len(df))} van {len(df)}")
    st.dataframe(subset, width="stretch")

    # Navigatieknoppen
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Vorige", on_click=prev_page)
    with col2:
        st.button("Volgende ➡️", on_click=next_page)

else:
    st.info("⬆️ Upload hierboven een Excel-bestand om te beginnen.")
