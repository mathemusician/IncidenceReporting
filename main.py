import base64
from pathlib import Path
import pandas as pd
import streamlit

import streamlit as st
from PIL import Image


def main():
    # print("hey there")


    img = Image.open("/Users/CARLOSPARLOUR/Documents/Python/practice/images/ConocoPhillips-Logo-Small.png")
    st.image(img, width= 150,use_column_width=200)

    img2 = Image.open("/Users/CARLOSPARLOUR/Documents/Python/practice/images/background.jpeg")
    st.image(img2, width= 1440,)


    st.header("Incidents Reporting")

    with st.form("my_form"):
        st.write("Please Fill Out Information Below")
        #slider_val = st.slider("Form slider")
        # checkbox_val = st.checkbox("Form checkbox")
        # Every form must have a submit button.

        submitted = st.form_submit_button("Submit")
        # if submitted:
        #     st.write("slider", slider_val, "checkbox", checkbox_val)

    # st.write("")

    # path = st.text_input('/Users/CARLOSPARLOUR/Documents/Python/practice/IncidentsReporting.csv')
    # if path:
    #     df = pd.read_csv(path)
    #     df


    # st.image("/Users/CARLOSPARLOUR/Documents/Python/practice/images/ConocoPhillips-Logo.png")
    # st.markdown
    # st.image("/Users/CARLOSPARLOUR/Documents/Python/practice/images/background.jpeg")







if __name__ == "__main__":
    main()


def simulate():
    img = Image.open("logo.jpg")
    st.image(img)
    print()
    # header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".formatimg_to_bytes("header.png")
    # st.markdown(header_html, unsafe_allow_html=True,)


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)
