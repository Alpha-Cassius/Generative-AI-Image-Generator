# Generative-AI-Image-Generator

Code Description 🧑‍💻

The project is built using Python and leverages the CustomTkinter library for a modern and customizable GUI. It interacts with the Hugging Face API to generate images based on text prompts. Below is an overview of the key components of the code:

Libraries and JSON Setup:
The code imports essential libraries like customtkinter for GUI creation, requests for API interaction, and PIL (Pillow) for image manipulation. It also reads a JSON file (IMG_GENERATION_MODELS.json) that contains model names and their respective API URLs for dynamic model selection.

App Class Initialization:
The App class inherits from CTk and serves as the main window for the application. Upon initialization, the app configures a sleek black-themed window and places various elements like labels, text boxes, and buttons.

User Interface:

Prompt Entry: A multi-line text box where the user inputs the text prompt for image generation.
Model Selection: A combo box that allows the user to select different AI models for image generation, dynamically updating the API URL.
Generate and Save Buttons: The generate button sends the prompt to the Hugging Face model via an API call, while the save button allows the user to save the generated image.
Image Generation:
The generate function sends a POST request with the user’s prompt to the selected AI model API. Upon receiving the generated image, it resizes it to fit within the display area and updates the app window with the image.

Save Functionality:
The save_image function allows users to save the generated image locally in .png or .jpg formats using a file dialog.

Model Selection:
The change_model function dynamically changes the API URL based on the selected model, enabling flexibility in generating different types of artwork.
