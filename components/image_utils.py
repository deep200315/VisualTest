import base64
import streamlit as st

# Function to encode an uploaded image in base64
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

# Function to encode a local image to base64
def load_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Function to display image with custom size using HTML
def display_image_with_size(image, width, height):
    base64_image = encode_image(image)
    image_type = image.type.split('/')[1]  # Get the image type (e.g., png, jpg)
    # Create the HTML image tag with custom width and height
    img_tag = f"<img src='data:image/{image_type};base64,{base64_image}' width='{width}' height='{height}'/>"
    st.markdown(img_tag, unsafe_allow_html=True)
