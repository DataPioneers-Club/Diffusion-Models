# Introduction to Diffusion Models
Diffusion models are a class of generative models that have gained popularity for their ability to generate high-quality images and other types of data. 
These models are based on the idea of gradually transforming a simple, structured distribution into a complex one that closely resembles real-world data.
The process is akin to "diffusing" information through a medium, starting with noise and refining it step by step until a clear image or data sample is produced.
# How Diffusion Models Work
The diffusion process involves two main phases: the forward process and the reverse process.
* Forward Process: In this phase, the model gradually adds noise to the data, effectively destroying its structure. This process can be thought of as a Markov chain where each step adds a small amount of noise, 
  eventually turning the data into pure noise.
* Reverse Process: The reverse process is where the magic happens. Starting from noise, the model learns to reverse the diffusion process, step by step, to reconstruct the original data. By learning to denoise at 
  each step, the model is able to generate new data samples that are highly realistic and resemble the original data distribution.

# Objectives of Diffusion Models
* Data Generation: To create new data samples that are indistinguishable from real-world data. This includes generating realistic images, audio, text, and other forms of data.

* Denoising: Diffusion models are designed to remove noise from data, which makes them useful for tasks like image restoration, where the goal is to recover the original image from a noisy version.

* Data Understanding: By modeling the distribution of data, diffusion models help in understanding the underlying structure and relationships within the data.

* Anomaly Detection: They can be used to identify outliers or anomalies by modeling what "normal" data looks like, making them applicable in fields like cybersecurity, finance, and healthcare.

# Applications of Diffusion Models
* Image Generation: One of the most popular applications is in generating high-quality images. Models like DALL·E and Stable Diffusion use diffusion techniques to create realistic images from textual descriptions.

* Image Inpainting: Diffusion models can fill in missing parts of images, making them useful for image restoration and editing tasks where parts of an image are corrupted or missing.

* Text-to-Image Synthesis: These models can generate images from text prompts, a task that combines natural language processing with image generation.
# Technology 
* Python
* Hugging Face API
* Gradio
# Website 
![Screenshot 2024-08-18 115959](https://github.com/user-attachments/assets/01c308e4-8da9-4186-b0bd-0866bd1df7e1)
![Screenshot 2024-08-18 120142](https://github.com/user-attachments/assets/5931d40b-3447-4d80-9c78-40d5239a3b76)

## How to run 
* You have to create **API Token** on Hugging Face and create a .env file in that write this code ```bash HUGGING_FACE_API_KEY = Your api key ``` 
```bash
git clone https://github.com/DataPioneers-Club/Diffusion-Models
```
Run these commnad in terminal 
```bash
python interface.py
```
# Pre-Trained models 
The code where pre-trained model can be used is still in working it will be uploaded as soon as it is done 

# Detail Analysis on Diffusion Models 
* This is the [Video](https://www.youtube.com/watch?v=a4Yfz2FxXiY&t=8s) which i referred.
* [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sjy9odlSSy0RBVgMTgP7s99NXsqglsUL?usp=sharing)

# License
The software is available under the [MIT License](https://github.com/DataPioneers-Club/Diffusion-Models/blob/main/LICENSE).

# Contact
If you have any questions, feel free to [open an issue](https://github.com/DataPioneers-Club/Diffusion-Models/issues) or contact [Akarshan Gupta](https://github.com/AkarshanGupta/AkarshanGupta).


