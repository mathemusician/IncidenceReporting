import base64
from pathlib import Path
import pandas as pd
import streamlit
import os
from pathlib import Path

import streamlit as st
from PIL import Image

file_dir = Path(os.path.dirname(os.path.abspath(__file__)))



def main():
    # New LOGO that is resizd toreduce the amount of space between the logo and photo
    img = Image.open(file_dir/"Images"/"logo-print.png")
    st.image(img, width= 250,use_column_width=200)

    # img = Image.open("/Users/CARLOSPARLOUR/Documents/Python/IncidenceReporting/Images/logo-print.png")
    # st.image(img, width= 250,use_column_width=200)

    img2 = Image.open(file_dir/"Images"/"background.jpeg")
    st.image(img2, width= 960,)

    # img2 = Image.open("/Users/CARLOSPARLOUR/Documents/Python/IncidenceReporting/Images/background.jpeg")
    # st.image(img2, width=960)

    #Title
    st.header("Incidents Reporting")

    with st.form("my_form"):
        st.write("Please Fill Out the Information Below")

        submitted = st.form_submit_button("Submit")
# HEAD
        if submitted:
            # Fetch Data from db
            st.write("slider", slider_val, "checkbox", checkbox_val)


if __name__ == "__main__":
    main()


# def img_to_bytes(img_path):
#     img_bytes = Path(img_path).read_bytes()
#     encoded = base64.b64encode(img_bytes).decode()
#     return encoded
#
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
#
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )
