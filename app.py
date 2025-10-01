import streamlit as st
import pandas as pd

# Brede layout
st.set_page_config(layout="wide")
if
st.title("📊 Regressietesten Viewer")

# Bestand uploaden
uploaded_file = st.file_uploader("Kies een Json-bestand", type=["json"])

if uploaded_file is not None:
    df = pd.read_json(uploaded_file)

    # Zoekbalk``
    query = st.text_input("🔍 Zoek in alle kolommen")
    if query:
        mask = df.apply(lambda row: row.astype(str).str.contains(query, case=False, na=False)).any(axis=1)
        df = df[mask]

    # Dropdown voor aantal rijen per pagina
    rows_per_page = st.selectbox("Aantal rijen per pagina", [3, 5, 10, 20, 50, 100], index=3)

    # Huidige pagina
    if "page" not in st.session_state:
        st.session_state.page = 0

    def next_page():
        if (st.session_state.page + 1) * rows_per_page < len(df):
            st.session_state.page += 1

    def prev_page():
        if st.session_state.page > 0:
            st.session_state.page -= 1

    # Subset tonen
    start = st.session_state.page * rows_per_page
    end = start + rows_per_page
    subset = df.iloc[start:end]

    # Bewerkbare tabel met groter lettertype
    st.data_editor(subset, width="stretch", hide_index=True)

    # Navigatie
    st.write(f"Toont rijen {start+1} t/m {min(end, len(df))} van {len(df)}")
    col1, col2 = st.columns(2)
    with col1:
        st.button("⬅️ Vorige", on_click=prev_page)
    with col2:
        st.button("Volgende ➡️", on_click=next_page)

else:
    st.info("⬆️ Upload hierboven een .json-testcase-bestand om te beginnen.")
