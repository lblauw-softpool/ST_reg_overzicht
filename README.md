# ST_reg_overzicht
regessie in een prikkelarme omgeving via streamlit in de browser

1. Drag & Drop upload van excelbestanden
Gebruik st.file_uploader() met accept_multiple_files=True en type filter op .xlsx.

Dit zorgt voor een drag & drop inbox waar excelbestanden ingegooid kunnen worden.

2. Data inlezen uit excel (3-5 rijen)
Lees de excel met Pandas (pd.read_excel()) uit het geüploade bestand.

Beperk het overzicht tot de eerste 3-5 rijen met head().

3. Status toekennen per rij
Maak per rij een selectbox met opties:

Goed ✅

Goed met opmerking ✅ℹ️

Fout ❌

Fout met opmerking ❌ℹ️

4. Invulveld voor opmerking bij status met opmerking
Toon een tekstveld gekoppeld aan de rij als een status "met opmerking" wordt gekozen.

Gebruik hiervoor conditionele rendering in Streamlit.

5. Toevoegen van schermopnames (.png, .mp4, .gif)
Maak een uploadveld voor deze bestandsformaten, ook met drag & drop.

Koppel de uploads aan de bijbehorende regel (bijvoorbeeld regelnummer).

Verwerk titel in bestandsnaam, en bij meerdere bestanden voeg suffix toe: %titel-a, %titel-b, etc.
```python
Voorbeeld code snippet (vereenvoudigd)
python
import streamlit as st
import pandas as pd

st.title("Regressie Test Overzicht")

# 1. Upload excelbestanden
uploaded_files = st.file_uploader("Upload Excel bestanden", accept_multiple_files=True, type=['xlsx'])

if uploaded_files:
    for file in uploaded_files:
        df = pd.read_excel(file).head(5)  # lees de eerste 5 rijen
        
        # Tabel met statusvelden
        for idx, row in df.iterrows():
            st.write(f"Regel {idx+1}: {row.to_dict()}")
            
            status = st.selectbox(f"Status regel {idx+1}", 
                                  ['Goed ✅', 'Goed met opmerking ✅ℹ️', 'Fout ❌', 'Fout met opmerking ❌ℹ️'], 
                                  key=f"status_{file.name}_{idx}")
            
            if "met opmerking" in status:
                opmerking = st.text_input(f"Opmerking bij regel {idx+1}", key=f"opm_{file.name}_{idx}")
        
        # 5. Upload schermopnames voor deze file
        uploads = st.file_uploader(f"Upload schermopnames bij {file.name}", accept_multiple_files=True, type=['png','mp4','gif'], key=f"media_{file.name}")
        
        if uploads:
            for i, media_file in enumerate(uploads):
                # Verwerk naam met suffix a,b,c etc.
                suffix = chr(ord('a') + i)
                naam_met_info = f"{file.name}-regel-{i+1}-{suffix}-{media_file.name}"
                st.write(f"Geüpload: {naam_met_info}")
```
Deze basis kan verder uitgebreid worden met opslag en overzichtspagina, plus html5 video/image weergave voor de media uploads.

Met deze aanpak wordt voldaan aan je wens om excel te uploaden, rijen te tonen met statussen en opmerkingen, en schermopnames toe te voegen per regel in een gebruiksvriendelijke Streamlit interface.