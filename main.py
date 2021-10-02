import base64
from pathlib import Path
import pandas as pd
import streamlit
import streamlit as st
from PIL import Image


def main():
    # run streamlit using command line **streamlit run /Users/CARLOSPARLOUR/Documents/Python/IncidenceReporting/main.py**
    # this will grab the images and display them
    #Change depending on your
    img = Image.open("/Users/CARLOSPARLOUR/Documents/Python/IncidenceReporting/Images/ConocoPhillips-Logo-Small.png")
    st.image(img, width=175, use_column_width=200)

    img2 = Image.open("/Users/CARLOSPARLOUR/Documents/Python/IncidenceReporting/Images/background.jpeg")
    st.image(img2, width=1260)

    #Title
    st.header("Incidents Reporting")

    with st.form("my_form"):
        st.write("Please Fill Out Information Below")
        # used for the submit button
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

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
