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
GENMI_API_KEY = "AIzaSyCKRUfnJNBeYa8FcHwxitsQryeIIrY0080"  # Replace with your actual API key
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
















# import google.generativeai as genai
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import pywhatkit
# import pyjokes
# import os
# import sys
# import requests
# import logging
# from PIL import Image
# from io import BytesIO
# from requests import get
# from bs4 import BeautifulSoup
# from PyQt6.QtWidgets import QApplication
# from PyQt6 import QtCore
# from desktop_2 import JarvisOverlayGUI

# # Configure logging
# logging.basicConfig(filename="gemini_queries.log", level=logging.INFO)

# # Set up Google Gemini API
# GEMINI_API_KEY = "AIzaSyCKRUfnJNBeYa8FcHwxitsQryeIIrY0080"  # Replace with your actual API key
# genai.configure(api_key=GEMINI_API_KEY)

# def query_gemini_text(query):
#     """
#     Send a text query to Google Gemini and return the response.
#     This is for standard text-based interactions.
#     """
#     try:
#         model = genai.GenerativeModel('gemini-1.5-flash-latest')
#         response = model.generate_content(query)
        
#         # Extract token usage details if available
#         total_tokens = response.usage_metadata.total_tokens if hasattr(response, 'usage_metadata') else 'N/A'
#         tokens_left = response.usage_metadata.tokens_left if hasattr(response, 'usage_metadata') else 'N/A'
        
#         # Log the interaction
#         logging.info(f"Text Query: {query}\nResponse: {response.text}\nTotal Tokens Used: {total_tokens}\nTokens Left: {tokens_left}\n")
        
#         return f"{response.text}\n\n(Tokens Used: {total_tokens}, Tokens Left: {tokens_left})"
    
#     except Exception as e:
#         error_message = f"Error in text query: {e}"
#         logging.error(error_message)
#         return error_message

# def query_gemini_image(query):
#     """
#     Generate an image based on the query using Gemini Pro Vision.
#     The generated image will be saved in an 'image_generation' folder.
#     """
#     try:
#         # Use the Pro Vision model for image generation
#         model = genai.GenerativeModel('gemini-1.5-pro-vision')
        
#         # Create image generation directory if it doesn't exist
#         image_dir = "image_generation"
#         if not os.path.exists(image_dir):
#             os.makedirs(image_dir)
#             logging.info(f"Created directory: {image_dir}")
        
#         # Generate a timestamp for unique filename
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         image_filename = f"{image_dir}/gemini_image_{timestamp}.png"
        
#         # Format request for image generation
#         response = model.generate_content([{"text": f"Generate an image based on this description: {query}"}])
        
#         # Process the response
#         if hasattr(response, "candidates") and response.candidates:
#             # Extract image data
#             image_url = response.candidates[0].content.parts[0].inline_data.data
#             image_data = get(image_url).content
            
#             # Save the image
#             image = Image.open(BytesIO(image_data))
#             image.save(image_filename)
            
#             # Display the image
#             image.show()
            
#             logging.info(f"Image generated and saved to {image_filename}")
#             return f"Image generated and saved to {image_filename}"
#         else:
#             logging.warning("No image was generated in the response")
#             return "No image could be generated based on your query."
    
#     except Exception as e:
#         error_message = f"Error in image generation: {e}"
#         logging.error(error_message)
#         return error_message

# def query_gemini_code(query, language=None):
#     """
#     Generate code based on the query using Gemini.
#     The generated code will be saved in a file with the appropriate extension.
    
#     Args:
#         query (str): The code generation prompt
#         language (str, optional): Programming language to generate. If None, it will be extracted from the query.
#     """
#     try:
#         # Determine the programming language if not provided
#         if not language:
#             # Extract language from query if possible
#             common_languages = {
#                 "python": ".py",
#                 "javascript": ".js",
#                 "typescript": ".ts",
#                 "java": ".java",
#                 "c++": ".cpp",
#                 "c#": ".cs",
#                 "ruby": ".rb",
#                 "php": ".php",
#                 "go": ".go",
#                 "rust": ".rs",
#                 "swift": ".swift",
#                 "kotlin": ".kt",
#                 "html": ".html",
#                 "css": ".css",
#                 "sql": ".sql",
#                 "bash": ".sh",
#                 "powershell": ".ps1"
#             }
            
#             # Try to detect language from the query
#             detected_language = None
#             for lang in common_languages.keys():
#                 if lang.lower() in query.lower():
#                     detected_language = lang
#                     break
            
#             language = detected_language or "python"  # Default to Python if no language detected
        
#         # Get file extension
#         extension = common_languages.get(language.lower(), ".txt")
        
#         # Create code generation directory if it doesn't exist
#         code_dir = "code_generation"
#         if not os.path.exists(code_dir):
#             os.makedirs(code_dir)
#             logging.info(f"Created directory: {code_dir}")
        
#         # Generate timestamp for unique filename
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         code_filename = f"{code_dir}/generated_code_{timestamp}{extension}"
        
#         # Enhanced prompt for code generation
#         enhanced_query = f"""
#         Generate clean, well-commented, and functional {language} code for the following request:
#         {query}
        
#         Please provide only the code with appropriate comments. Do not include explanations outside of code comments.
#         """
        
#         # Use Gemini Pro for code generation
#         model = genai.GenerativeModel('gemini-1.5-pro')
#         response = model.generate_content(enhanced_query)
        
#         # Process response to extract code
#         code_content = response.text
        
#         # Remove markdown code blocks if present
#         if code_content.startswith("```") and code_content.endswith("```"):
#             code_content = code_content.split("```")[1]
#             if code_content.startswith(language):
#                 code_content = code_content[len(language):].strip()
        
#         # Save the generated code
#         with open(code_filename, 'w') as file:
#             file.write(code_content)
        
#         logging.info(f"Code generated and saved to {code_filename}")
#         return f"Code generated in {language} and saved to {code_filename}"
    
#     except Exception as e:
#         error_message = f"Error in code generation: {e}"
#         logging.error(error_message)
#         return error_message

# def process_query(query):
#     """
#     Process the user query and determine which type of response to generate.
#     """
#     query_lower = query.lower()
    
#     # Check if this is an image generation request
#     if any(phrase in query_lower for phrase in ["generate image", "create image", "draw", "picture of", "show me", "visualize"]):
#         return query_gemini_image(query)
    
#     # Check if this is a code generation request
#     elif any(phrase in query_lower for phrase in ["write code", "generate code", "code for", "program", "function", "script", "class"]):
#         # Try to extract language from query
#         language = None
#         for lang in ["python", "javascript", "java", "c++", "html", "css"]:
#             if lang in query_lower:
#                 language = lang
#                 break
        
#         return query_gemini_code(query, language)
    
#     # Default to text response
#     else:
#         return query_gemini_text(query)