import streamlit as st
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
from google import genai
from google.genai import types

load_dotenv(override=True)

client = genai.Client()

st.title("🎨 AI Logo Generator")

logo_style = st.selectbox("Logo Style", ["minimalist", "modern", "traditional"])
company_area = st.selectbox("Industry", ["Health Care", "Software", "Fashion", "Education"])
company_name = st.text_input("Company Name")

if st.button("Generate Logo") and company_name:
    prompt = (
        f"A {logo_style} logo for a {company_area} company. "
        f"Include the company name '{company_name}'. "
        f"Flat design, professional, high quality."
    )

    with st.spinner("Generating logo..."):
        response = client.models.generate_images(
            model="imagen-2",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1
            )
        )

        image_bytes = response.generated_images[0].image.image_bytes
        image = Image.open(BytesIO(image_bytes))

        st.image(image, caption="Generated Logo", use_container_width=True)
