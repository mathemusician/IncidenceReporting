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
    img = Image.open(file_dir/"images"/"ConocoPhillips-Logo-Small.png")
    st.image(img, width= 150,use_column_width=200)

    img2 = Image.open(file_dir/"images"/"background.jpeg")
    st.image(img2, width= 1440,)

    img2 = Image.open("/Users/CARLOSPARLOUR/Documents/Python/IncidenceReporting/Images/background.jpeg")
    st.image(img2, width=1260)

    #Title
    st.header("Incidents Reporting")

    with st.form("my_form"):
        st.write("Please Fill Out Information Below")

        submitted = st.form_submit_button("Submit")








if __name__ == "__main__":
    main()


# def simulate():
#     img = Image.open("logo.jpg")
#     st.image(img)
#     print()
#     # header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".formatimg_to_bytes("header.png")
#     # st.markdown(header_html, unsafe_allow_html=True,)
#
#
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
