import streamlit as st
import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def get_image_analysis(prompt, image):
    try:
        if image is not None:
           
            if prompt:
                response = model.generate_content([prompt, image])
            else:
                response = model.generate_content([image])
        elif prompt:  # If no image, process only the prompt
            response = model.generate_content([prompt])
        else:
            response = "Error: No input provided!"
        
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


st.set_page_config(page_title="OptifyAI 🧠", page_icon="🧠", layout="wide")

st.markdown("<h1 style='text-align: center; font-weight: bold; font-size: 40px;'>OptifyAI <span style='color: #ff6347;'>🧠</span></h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Upload an image or enter a prompt to analyze! 📸</h3>", unsafe_allow_html=True)

prompt = st.text_input("**Enter a prompt (optional):**", placeholder="e.g., Describe this image...")

uploaded_file = st.file_uploader("**Upload an image**", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

if st.button("🔍 Analyze Image & Text"):
    with st.spinner("🔄 Analyzing..."):
        response = get_image_analysis(prompt, image)
    st.subheader("**Response:**")
    st.write(response)

st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ by OptifyAI(Arihant Jain) | Powered by Gemini Vision AI</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Disclaimer: This app is for demonstration purposes only.</p>", unsafe_allow_html=True)