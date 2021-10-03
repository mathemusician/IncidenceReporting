import base64
from pathlib import Path
import pandas as pd
import streamlit
import os
from pathlib import Path
import numpy as np
import pydeck as pdk
import random

import streamlit as st
from PIL import Image

file_dir = Path(os.path.dirname(os.path.abspath(__file__)))
DATE_TIME = "date/time"
DATA_URL = file_dir / "data.csv"


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
extra = load_data("/Users/CARLOSPARLOUR/Documents/Python/IncidenceReporting/heatmap-data.csv")
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
    global lat
    img = Image.open(file_dir / "Images" / "logo-print.png")
    st.image(img, width=200, use_column_width=200)

    img2 = Image.open(file_dir / "Images" / "background.jpeg")
    st.image(img2,
             caption="No task is so important that we can’t take the time to do it safely. A safe company is a successful company.")

    # st.image(img2, width=1260)

    # Title
    st.header("Incidents Reporting")
    # test_data = pd.concat([data]*20, ignore_index=True)

    latitudes = ["29.07393266320772", "38.83889745592545", "67.28150241774922", "65.76861506352907",
                 "27.850857403798024", "31.400790392869073", "32.14315679366797", "29.7828109", "69.5259183676525",
                 "-38.41968552700519"]
    longitudes = ["-95.74462745592294", "-90.07362745592292", "8.899795546234275", "7.891749990422023",
                  "-98.58710217513708", "-103.5499547076863", "-102.18566929860735", "-95.618529",
                  "-152.13526519858635", "142.6508871470676"]
    basenames = ["Sweeny Refinery", "Wood River Refinery", "SNE-1 well", "Warka well", "Eagle Ford Well",
                 "Permian Basin Well", "Midland Well", "Houston office", "Alphine well", "Otway Basin Well"]
    baseIDS = ["B02512", "B09768", "B06567", "B08798", "B04673", "B05767", "B06376", "B02783", "B04237", "B06788"]
    csv_location = [0,0,0]

    with st.form("my_form"):
        st.write("Please Fill Out the Information Below")
        # used for date in CSV file
        date = st.date_input("Enter Date")
        # Used for incidents csv file, DOES NOT PREVENT OR CHECK FOR IDENTICAL NUMBERS YET
        incident_number = random.randint(100000, 9999999)
        # Used to select incident typer
        incident_type = st.selectbox("Select Type or Incident", ("Trip/Fall", "Heavy Equipment Violation", "Other"))
        # Used for

        location = st.selectbox("Select location, If not available select other and add in description below",
                                (
                                    "Sweeny Refinery", "Wood River Refinery", "SNE-1 well", "Warka well",
                                    "Eagle Ford Well",
                                    "Permian Basin Well", "Midland Well", "Houston office",))

        if location == "Sweeny Refinery":
            csv_location[0] = basenames[0]
            csv_location[1] = longitudes[0]
            csv_location[2] = latitudes[0]
        elif location == "Wood River Refinery":
            csv_location[0] = basenames[1]
            csv_location[1] = longitudes[1]
            csv_location[2] = latitudes[1]
        elif location == "SNE-1 well":
            csv_location[0] = basenames[2]
            csv_location[1] = longitudes[2]
            csv_location[2] = latitudes[2]
        elif location == "Warka well":
            csv_location[0] = basenames[3]
            csv_location[1] = longitudes[3]
            csv_location[2] = latitudes[3]
        elif location == "Eagle Ford Well":
            csv_location[0] = basenames[4]
            csv_location[1] = longitudes[4]
            csv_location[2] = latitudes[4]
        elif location == "Permian Basin Well":
            csv_location[0] = basenames[5]
            csv_location[1] = longitudes[5]
            csv_location[2] = latitudes[5]
        elif location == "Eagle Ford Well":
            csv_location[0] = basenames[6]
            csv_location[1] = longitudes[6]
            csv_location[2] = latitudes[6]
        elif location == "Midland Well":
            csv_location[0] = basenames[7]
            csv_location[1] = longitudes[7]
            csv_location[2] = latitudes[7]
        elif location == "Houston office":
            csv_location[0] = basenames[8]
            csv_location[1] = longitudes[8]
            csv_location[2] = latitudes[8]
        else:
            csv_location[0] = basenames[8]
            csv_location[1] = longitudes[8]
            csv_location[2] = latitudes[8]

        description = st.text_area("Enter a brief description, Include time, Number of people Involved and if Medical attention was required.")
        uploaded_file = st.file_uploader("Choose a file")
        # if uploaded_file is not None:
        # df = pd.read_csv(uploaded_file)
        # st.write(dataframe)

        submitted = st.form_submit_button("Submit")
        if submitted:
            # Fetch Data from db
            st.write("Submitted. Thank you for your dedication to safety.")
            # ##### used for the location
            base_ID = csv_location[0]
            long_ID = csv_location[1]
            lang_ID = csv_location[2]
            print(csv_location[0], csv_location[1], csv_location[2])

    # print(test_data[["lat", "lon"]])

    # used to display the map
    with st.form("my_map"):

        map_display = st.selectbox("View our current Incidents",
                                   ("", "Trip/Fall", "Heavy Equipment Violation", "Other"))
        submitted = st.form_submit_button("Submit")
        if submitted:
            if map_display == "Trip/Fall":
                # st.write("slider", slider_val, "checkbox", checkbox_val)
                map(extra, midpoint[0], midpoint[1], 11)
            if map_display == "Heavy Equipment Violation":
                st.text("not ready")
            if map_display == "other":
                st.text("not ready")

    # map(extra, midpoint[0], midpoint[1], 11)



if __name__ == "__main__":
    main()
