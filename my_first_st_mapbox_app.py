import pandas
import pydeck
import streamlit as st


@st.cache
def load_waterpump_data():
    raw_data = pandas.read_csv("train_df_after_EDA.csv")
    return raw_data


df = load_waterpump_data()

st.write(df)

df = df[["longitude", "latitude", "population", "amount_tsh"]]

loc_layer = pydeck.Layer(
    type='ScatterplotLayer',
    data=df,
    get_position=["longitude", "latitude"],
    # auto_highlight=True,
    get_radius=500,
    get_fill_color=[180, 0, 200, 140],
    # pickable=True
)

layer_selectbox = st.selectbox("Choose layer:", ("Location", "Population", "Water Volume"))

pop_layer = pydeck.Layer(
    type='ColumnLayer',
    data=df,
    get_position=["longitude", "latitude"],
    get_elevation="population",
    elevation_scale=10,
    # radius=1000,
    get_fill_color=[180, 0, 200, 140],
    auto_highlight=True,
    pickable=True,
    extruded=True
)

water_layer = pydeck.Layer(
    type='ColumnLayer',
    data=df,
    get_position=["longitude", "latitude"],
    get_elevation="amount_tsh",
    elevation_scale=1,
    # radius=1000,
    get_fill_color=[180, 0, 200, 140],
    auto_highlight=True,
    pickable=True,
    extruded=True
)

layers = [loc_layer]
if layer_selectbox == "Population":
    layers = [pop_layer]
elif layer_selectbox == "Water Volume":
    layers = [water_layer]

initial_view = pydeck.ViewState(latitude=df.latitude.mean(),
                                longitude=df.longitude.mean())

tooltip = {
    "html": "<b>Longitude:</b> {longitude}<br> "
            "<b>Latitude:</b> {latitude}<br> "
            "<b>Population Served:</b> {population}<br>"
            "<b>Water Volume:</b> {amount_tsh}"
}

deck = pydeck.Deck(
    layers=layers,
    # initial_view_state=initial_view,
    # tooltip=tooltip,
    # map_provider="mapbox",
    # map_style="satellite"
)

st.pydeck_chart(deck)
