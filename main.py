import streamlit as st
from components import load_base64_image, encode_image, get_image_description
from utils import generate_test_instructions, get_llm_answer

api_key = st.secrets["OPEN_AI_API_KEY"]

icon_base64 = load_base64_image("assets/icon1.png")  

st.markdown(
    f"""
    <h1 style='display: flex; align-items: center;'>
        <img src='data:image/png;base64,{icon_base64}' 
             style='width:60px;height:60px;margin-right:15px;'> 
        VisualTestAI
    </h1>
    """, unsafe_allow_html=True
)

# File uploader to upload multiple images
uploaded_images = st.file_uploader("Upload multiple images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
context_text = st.text_input("Ask about the test instructions or provide additional context:")

# Initialize a variable to store descriptions
descriptions = []

# Initialize a session state to store test instructions
if 'test_instructions' not in st.session_state:
    st.session_state.test_instructions = {}

# Process uploaded images if any
if uploaded_images:
    # Create a container for each image and its testing instructions
    col1, col2 = st.columns([1, 1]) 
    with col1:
        for i, image in enumerate(uploaded_images):
            # Display the image
            st.image(image, caption=f"Uploaded Image: {image.name}", width=350)
            # Encode the image in base64
            base64_image = encode_image(image)
            # Generate and store the image description
            description = get_image_description(base64_image, api_key)
            descriptions.append(description)

    with col2:
        # Display a button to generate test instructions for all images
        if st.button("Generate Test Instructions."):
            # Generate and store the test instructions in session state
            for i, description in enumerate(descriptions):
                test_instructions = generate_test_instructions(description, api_key)
                st.session_state.test_instructions[f"Image {i+1}"] = test_instructions

    # Display the test instructions if they exist in session state
    for i in range(len(uploaded_images)):
        if f"Image {i+1}" in st.session_state.test_instructions:
            st.write(f"**Image {i+1} Test Instructions:**")
            st.write(st.session_state.test_instructions[f"Image {i+1}"])


    if context_text:
        combined_test_instructions = ""
        for i in range(len(uploaded_images)):
            if f"Image {i+1}" in st.session_state.test_instructions:
                combined_test_instructions += f"\nImage {i+1} Test Instructions: {st.session_state.test_instructions[f'Image {i+1}']}"

        
            response = get_llm_answer(context_text, combined_test_instructions)  
            st.write("**Response to your query:**")
            st.write(response)
