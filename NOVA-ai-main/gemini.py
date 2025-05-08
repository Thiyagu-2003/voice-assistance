import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
import sys
import requests
import logging
from PIL import Image
from io import BytesIO
from requests import get
from bs4 import BeautifulSoup
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtCore
from desktop_2 import JarvisOverlayGUI

# Configure logging
logging.basicConfig(filename="gemini_queries.log", level=logging.INFO)

# Set up Google Gemini API
GENMI_API_KEY = "Replace with your actual gemini API key"  # Replace with your actual API key
genai.configure(api_key=GENMI_API_KEY)

# def query_google_gemini(query, is_image_request=False):
#     """Send a query to Google Gemini and return the response or image."""
#     try:
#         model_name = "gemini-1.5-pro-vision" if is_image_request else "gemini-1.5-flash-latest"
#         model = genai.GenerativeModel(model_name)
        
#         if is_image_request:
#             response = model.generate_content([{"text": query}])
#             if hasattr(response, "candidates") and response.candidates:
#                 image_url = response.candidates[0].content.parts[0].inline_data.data
#                 image_data = get(image_url).content
#                 image = Image.open(BytesIO(image_data))
#                 image_path = "generated_image.png"
#                 image.save(image_path)
#                 image.show()
#                 return "Image downloaded and displayed."
#             else:
#                 return "No image generated."
#         else:
#             response = model.generate_content(query)
            
#             # More robust way to handle usage metadata
#             usage_info = ""
#             if hasattr(response, 'usage_metadata'):
#                 # Get all available attributes dynamically
#                 metadata_attrs = vars(response.usage_metadata)
#                 usage_details = ", ".join([f"{k}: {v}" for k, v in metadata_attrs.items()])
#                 usage_info = f"\n\n(Usage Metadata: {usage_details})"
            
#             return f"{response.text}{usage_info}"
    
#     except Exception as e:
#         error_message = f"Error: {e}"
#         logging.error(error_message)
#         return error_message



#+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
def query_google_gemini(query, is_image_request=False):
    """Send a query to Google Gemini and return the response or image."""
    try:
        model_name = "gemini-1.5-pro-vision" if is_image_request else "gemini-1.5-flash-latest"
        model = genai.GenerativeModel(model_name)
        
        if is_image_request:
            response = model.generate_content([{"text": query}])
            if hasattr(response, "candidates") and response.candidates:
                image_url = response.candidates[0].content.parts[0].inline_data.data
                image_data = get(image_url).content
                image = Image.open(BytesIO(image_data))
                image_path = "generated_image.png"
                image.save(image_path)
                image.show()
                return "Image downloaded and displayed."
            else:
                return "No image generated."
        else:
            response = model.generate_content(query)
            
            # Check what token usage fields are available in the current API version
            token_info = ""
            if hasattr(response, 'usage_metadata'):
                # Get available token-related attributes safely
                metadata = response.usage_metadata
                
                # Try to get common token fields with fallbacks
                prompt_tokens = getattr(metadata, 'prompt_token_count', 'N/A')
                completion_tokens = getattr(metadata, 'candidates_token_count', 'N/A')
                total_tokens = getattr(metadata, 'total_token_count', 'N/A')
                
                # Format as a separate line that will be printed but not spoken
                token_info = f"\n\nTokens - Prompt: {prompt_tokens}, Completion: {completion_tokens}, Total: {total_tokens}"
            
            return f"{response.text}{token_info}"
    
    except Exception as e:
        error_message = f"Error: {e}"
        logging.error(error_message)
        return error_message
