import os
import requests
import gradio as gr
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

# Load your Hugging Face API token from the .env file
load_dotenv()
API_TOKEN = os.getenv("HUGGING_FACE_API_KEY")

# Endpoints for the Hugging Face models
MODEL_ENDPOINTS = {
    "Stable Diffusion v1-4": "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4",
    "Anything v4.0": "https://api-inference.huggingface.co/models/andite/anything-v4.0",
}

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_image(prompt, model_name):
    api_url = MODEL_ENDPOINTS[model_name]
    payload = {"inputs": prompt}
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            image = Image.open(BytesIO(response.content))
            return image
        except Exception as e:
            return f"Error processing image: {e}"
    else:
        return f"Error: {response.status_code}, {response.text}"

# Create the Gradio interface
iface = gr.Interface(
    fn=generate_image,
    inputs=[
        gr.Textbox(
            label="Enter your prompt",
            placeholder="Example prompts: 'A futuristic city skyline at sunset', 'A fantasy forest with glowing trees', 'A robot in a steampunk world'"
        ),
        gr.Radio(choices=list(MODEL_ENDPOINTS.keys()), label="Choose a model")
    ],
    outputs="image",
    title="Multi-Model Diffusion Image Generator",
    description="Enter a prompt and generate an image using different diffusion models via Hugging Face API.",
    examples=[
        ["A futuristic city skyline at sunset", "Stable Diffusion v1-4"],
        ["A fantasy forest with glowing trees", "Anything v4.0"],
        ["A robot in a steampunk world", "Stable Diffusion v1-4"]
    ]
)

# Launch the interface
iface.launch()
