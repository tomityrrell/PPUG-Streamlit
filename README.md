PPUG Presentation

- Intro to Streamlit (10 minutes)
    - Became interested in Streamlit after client demo of open-source NER models, including SpaCy
    - https://streamlit.io/
    - SpaCy Demo:  https://share.streamlit.io/ines/spacy-streamlit-demo/app.py
    - Text from PPUG Website:  https://www.princetonpy.org/
- Streamlit+PyTesseract Demo (20 minutes)
    - https://pypi.org/project/pytesseract/
    - Problem:  Visualize PyTesseract Ouput!
        - Data:  Images with text
        - Action:  Apply pytesseract and visualize bounding box info
    - Live code demo
        - First Steps
            - Import streamlit, PIL, Tesseract
            - Add file uploader, display image
            - Create button, call tesseract, view df
            - Add bounding boxes
            - Re-display image
        - Updates
            - Filter dataframe by conf
            - Restrict uploads to images/Look up file uploader documentation:  https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
            - Use placeholder for image:  https://docs.streamlit.io/knowledge-base/using-streamlit/insert-elements-out-of-order
- PSPS Project (10 minutes)
    - CPUC PSPS:  https://www.cpuc.ca.gov/PSPS/
    - Problem:  Visualize Weather Stations and related data
        - Data:  MesoNet Weather Stations at https://developers.synopticdata.com/mesonet/
        - Action:  Apply Gluonts for modeling https://ts.gluon.ai/
- Streamlit+PyDeck/Mapbox Demo (20 minutes)
    - PyDeck:  https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart
    - Mapbox API:  https://www.mapbox.com/
    - Problem:  Visualize Waterpumps and related data
        - Data:
            - Tanzania Water Pump Data:  https://www.kaggle.com/tatianasnwrt/pumpitup-challenge-dataset
            - Dataset Description:  https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/25/#features_list
        - Action: 
            - Plot pump locations
            - Plot population, water volume per pump
    - Live code demo
        - First steps
            - Import data with pandas, write
            - Filter needed columns
            - Create location layer
            - Create Deck
            - Plot map:  https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart
        - Updates
            - Cache data:  https://docs.streamlit.io/library/api-reference/performance/st.cache
            - Add initial view
            - Add tooltip
            - Add population layer
            - Add select box to switch layers