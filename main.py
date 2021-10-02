import base64
from pathlib import Path
import pandas as pd
import streamlit
import os
from pathlib import Path
import numpy as np
import pydeck as pdk

import streamlit as st
from PIL import Image

file_dir = Path(os.path.dirname(os.path.abspath(__file__)))
DATE_TIME = "date/time"
DATA_URL = file_dir/"data.csv"

@st.cache(persist=True)
def load_data(DATA_URL, nrows=None):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    try:
        data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    except KeyError:
        pass
    return data

data = load_data(DATA_URL)
extra = load_data("/Users/mosaicchurchhtx/Desktop/IncidenceReporting/heatmap-data.csv")
extra = extra.dropna()
# CREATING FUNCTION FOR MAPS

def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": float(lat),
            "longitude": float(lon),
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lng", "lat"],
                radius=100,
                elevation_scale=50,
                elevation_range=[0, 3000],
                pickable=True,
                extruded=True,
                coverage=1,
            ),
        ]
    ))

zoom_level = 12
midpoint = (np.average(extra['lat']), np.average(extra['lng']))


def main():
    img = Image.open(file_dir/"Images"/"ConocoPhillips-Logo-Small.png")
    st.image(img, width= 150,use_column_width=200)

    img2 = Image.open(file_dir/"Images"/"background.jpeg")
    st.image(img2, width= 1440,)

    st.image(img2, width=1260)

    #Title
    st.header("Incidents Reporting")

    # test_data = pd.concat([data]*20, ignore_index=True)

    # print(test_data[["lat", "lon"]])
    map(extra, midpoint[0], midpoint[1], 11)

    with st.form("my_form"):
        st.write("Please Fill Out the Information Below")

        submitted = st.form_submit_button("Submit")
        if submitted:
            # Fetch Data from db
            st.write("slider", slider_val, "checkbox", checkbox_val)


if __name__ == "__main__":
    main()