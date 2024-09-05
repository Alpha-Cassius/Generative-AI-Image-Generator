"""
---
Cassius' AI Image Generator 🎨🖼️

The app allows you to:

- **Generate images** from a user-provided text prompt.
- **Choose different AI models** to suit your artistic needs.
- **Save** the generated images locally in PNG or JPEG format.

Feel free to experiment with different prompts and models, and let your creativity run wild! 🎉
"""

# Importing modules
import customtkinter as ctk
from customtkinter import filedialog
import requests, io, json, tkinter
from PIL import Image, ImageTk

# Load available models from a JSON file
# This JSON file should have model names as keys and their respective API URLs as values.
with open(r'assets/IMG_GENERATION_MODELS.json', 'r') as file:
    data = json.load(file)
    values_list = list(data.values())

# Set a default API URL (change "Artistic" to whatever model you want as the default)
API_URL = data["Artistic"]
# Set authorization headers (replace "YOUR_HUGGING_FACE_API_KEY" with your actual key)
headers = {"Authorization": f"Bearer YOUR_HUGGING_FACE_API_KEY"}

# Configure the appearance mode and default color theme for the customtkinter window
ctk.set_appearance_mode("black")  # Use dark mode
ctk.set_default_color_theme("dark-blue")  # Set a color theme

# Create the main application class inheriting from CTk (customtkinter)
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configure window size and other parameters
        self.default_window_width = 1200
        self.default_window_height = 800
        self.authorization_token = ""
        self.configure(fg_color='black')  # Set background color to black

        # Set window title and dimensions
        self.title("Image Generator")
        self.geometry(f"{self.default_window_width}x{self.default_window_height}")

        # Add labels, entry box, buttons, and other widgets
        # Main title label
        self.windowlabel = ctk.CTkLabel(self, text="Cassius' Image Generator",
                                        font=ctk.CTkFont(size=30, weight="bold"), padx=50, pady=50, text_color="white")
        self.windowlabel.pack()

        # Prompt label
        self.promptlabel = ctk.CTkLabel(self, text="Prompt:",
                                        font=ctk.CTkFont(family="Times New Roman", size=20, weight="bold"),
                                        text_color="white")
        self.promptlabel.place(x=70, y=100)

        # Textbox for user to input a prompt
        self.promptentry = ctk.CTkTextbox(self, width=self.default_window_width-300, height=100, wrap='word')
        self.promptentry.pack(padx=60, pady=20, side='left', anchor='n')

        # ComboBox to allow user to select different models
        available_models = list(data.keys())  # Get available model names from the JSON file
        self.modelcomboBox = ctk.CTkComboBox(master=self, width=self.default_window_width/4, height=30, values=available_models,
                                             border_width=2, text_color="white", dropdown_fg_color='black',
                                             button_hover_color='blue', fg_color='black', command=self.change_model)
        self.modelcomboBox.place(x=self.default_window_width-200, y=140)

        # Generate Image button
        self.generatebutton = ctk.CTkButton(master=self, text="Generate Image", width=self.default_window_width/4, height=30,
                                            fg_color="transparent", hover_color='blue', border_width=2, text_color="white",
                                            command=self.generate)
        self.generatebutton.place(x=self.default_window_width-200, y=200)

        # Save Image button
        self.savebutton = ctk.CTkButton(master=self, text="Save Image", width=self.default_window_width/8, height=30,
                                        fg_color="transparent", hover_color='blue', border_width=2, text_color="white",
                                        command=self.save_image)
        self.savebutton.place(x=self.default_window_width+120, y=200)

        # Label to display generated images
        self.imagelabel = ctk.CTkLabel(self, text="", width=self.default_window_width-300, height=400, fg_color="black")
        self.imagelabel.place(x=self.default_window_width/4, y=300)

        # Initialize variables to keep track of the generated image for saving later
        self.generated_image = None
        self.pil_image = None

    # Function to generate an image from the prompt using the selected model's API
    def generate(self):
        def query(payload):
            # Send a POST request to the Hugging Face API
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        # Get the user input (prompt) from the text box
        image_bytes = query({"inputs": self.promptentry.get("1.0", "end-1c")})

        # Open the image using PIL (Pillow)
        image = Image.open(io.BytesIO(image_bytes))

        # Resize the image to fit within the label
        max_width = self.imagelabel.winfo_width()
        max_height = self.imagelabel.winfo_height()
        image.thumbnail((max_width, max_height), Image.ANTIALIAS)

        # Store the PIL image for saving later
        self.pil_image = image
        self.generated_image = ImageTk.PhotoImage(image)

        # Display the generated image in the imagelabel
        self.imagelabel.configure(image=self.generated_image)

    # Function to save the generated image to the user's device
    def save_image(self):
        if self.pil_image is not None:
            # Open a file dialog for the user to select the save location and file name
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("JPEG files", "*.jpg"),
                                                                ("All files", "*.*")])

            if file_path:
                # Save the image to the specified location
                self.pil_image.save(file_path)
                print(f"Image saved to {file_path}")
        else:
            # Print an error message if no image has been generated
            print("Error: No image generated to save")

    # Function to change the selected model and update the API URL
    def change_model(self, selected_model):
        global API_URL
        # Change the global API_URL based on the selected model
        API_URL = data[selected_model]
        print(f"Model changed to: {selected_model}, API_URL updated to: {API_URL}")

# Main entry point of the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
