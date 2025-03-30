# # # import cv2
# # # import numpy as np
# # # import pyaudio
# # # import threading
# # # import time
# # # from datetime import datetime

# # # class LaptopVoiceSmileCamera:
# # #     def __init__(self):
# # #         # Initialize laptop camera
# # #         self.cap = cv2.VideoCapture(0)  # 0 is typically the built-in webcam
        
# # #         # Set lower resolution for better performance on laptops
# # #         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# # #         self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
# # #         if not self.cap.isOpened():
# # #             raise IOError("Cannot open laptop webcam")
        
# # #         # Load face cascade and smile cascade
# # #         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# # #         self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        
# # #         # Audio settings - optimized for laptop microphones
# # #         self.FORMAT = pyaudio.paInt16
# # #         self.CHANNELS = 1
# # #         self.RATE = 22050  # Lower sample rate for laptop performance
# # #         self.CHUNK = 512   # Smaller chunk size
# # #         self.THRESHOLD = 1500  # Lower threshold for laptop microphones
        
# # #         # Voice detection variables
# # #         self.audio = pyaudio.PyAudio()
# # #         self.voice_detected = False
# # #         self.voice_detection_time = 0
# # #         self.voice_timeout = 2  # Voice detection remains valid for 2 seconds
        
# # #         # Smile detection variables
# # #         self.smile_detected = False
        
# # #         # Photo capture variables
# # #         self.last_capture_time = 0
# # #         self.capture_cooldown = 3  # Seconds between captures
# # #         self.photos_taken = 0
        
# # #         # Start voice detection in a separate thread
# # #         self.stop_thread = False
# # #         self.voice_thread = threading.Thread(target=self.detect_voice)
# # #         self.voice_thread.daemon = True
# # #         self.voice_thread.start()
    
# # #     def detect_voice(self):
# # #         """Continuously detect voice in background thread - optimized for laptop mic"""
# # #         try:
# # #             stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
# # #                                     rate=self.RATE, input=True,
# # #                                     frames_per_buffer=self.CHUNK)
            
# # #             print("Voice detection started")
            
# # #             # Calibration phase
# # #             print("Calibrating microphone - please be quiet for 3 seconds...")
# # #             calibration_samples = []
# # #             for i in range(30):  # Collect samples for 3 seconds
# # #                 data = np.frombuffer(stream.read(self.CHUNK, exception_on_overflow=False), dtype=np.int16)
# # #                 calibration_samples.append(np.abs(data).mean())
# # #                 time.sleep(0.1)
            
# # #             # Set threshold based on ambient noise
# # #             ambient_level = np.mean(calibration_samples)
# # #             self.THRESHOLD = ambient_level * 2.5  # Set threshold at 2.5x ambient noise
# # #             print(f"Calibration complete. Ambient level: {ambient_level}, Threshold: {self.THRESHOLD}")
            
# # #             while not self.stop_thread:
# # #                 try:
# # #                     data = np.frombuffer(stream.read(self.CHUNK, exception_on_overflow=False), dtype=np.int16)
# # #                     volume = np.abs(data).mean()
                    
# # #                     if volume > self.THRESHOLD:
# # #                         print(f"Voice detected! Volume: {volume}")
# # #                         self.voice_detected = True
# # #                         self.voice_detection_time = time.time()
# # #                     elif time.time() - self.voice_detection_time > self.voice_timeout:
# # #                         self.voice_detected = False
                        
# # #                     time.sleep(0.1)  # Small sleep to reduce CPU usage
# # #                 except Exception as e:
# # #                     print(f"Error in voice detection loop: {e}")
# # #                     time.sleep(0.5)  # Sleep and try again
                    
# # #         except Exception as e:
# # #             print(f"Error setting up audio stream: {e}")
# # #         finally:
# # #             try:
# # #                 stream.stop_stream()
# # #                 stream.close()
# # #             except:
# # #                 pass  # Stream might not have been created
    
# # #     def detect_smile(self, frame):
# # #         """Detect smile in the current frame - optimized for laptop cameras"""
# # #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# # #         # Equalize histogram to improve detection in varying laptop lighting
# # #         gray = cv2.equalizeHist(gray)
        
# # #         # More suitable parameters for laptop cameras
# # #         faces = self.face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(100, 100))
        
# # #         self.smile_detected = False
        
# # #         for (x, y, w, h) in faces:
# # #             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
# # #             roi_gray = gray[y:y+h, x:x+w]
# # #             roi_color = frame[y:y+h, x:x+w]
            
# # #             # Laptop-optimized smile detection parameters
# # #             smiles = self.smile_cascade.detectMultiScale(
# # #                 roi_gray, 
# # #                 scaleFactor=1.7, 
# # #                 minNeighbors=22, 
# # #                 minSize=(25, 25)
# # #             )
            
# # #             for (sx, sy, sw, sh) in smiles:
# # #                 cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
# # #                 self.smile_detected = True
        
# # #         return frame
    
# # #     def capture_photo(self, frame):
# # #         """Take a photo when both voice and smile are detected"""
# # #         current_time = time.time()
        
# # #         if (self.voice_detected and self.smile_detected and 
# # #                 current_time - self.last_capture_time > self.capture_cooldown):
# # #             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# # #             filename = f"smile_voice_photo_{timestamp}.jpg"
# # #             cv2.imwrite(filename, frame)
# # #             self.photos_taken += 1
# # #             print(f"Photo captured: {filename} (Total: {self.photos_taken})")
            
# # #             self.last_capture_time = current_time
            
# # #             # Display "Photo Taken!" message
# # #             height, width = frame.shape[:2]
# # #             cv2.putText(frame, "Photo Taken!", (width//4, height//2), 
# # #                         cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 4)
            
# # #             # Show the captured frame for a moment
# # #             cv2.imshow('Voice and Smile Camera', frame)
# # #             cv2.waitKey(1000)  # Display for 1 second
    
# # #     def run(self):
# # #         """Main method to run the camera"""
# # #         try:
# # #             print("Camera initialized. Preparing interface...")
# # #             time.sleep(1)  # Give the camera a moment to warm up
            
# # #             while True:
# # #                 ret, frame = self.cap.read()
# # #                 if not ret:
# # #                     print("Failed to grab frame - trying to reinitialize camera")
# # #                     self.cap.release()
# # #                     time.sleep(1)
# # #                     self.cap = cv2.VideoCapture(0)
# # #                     self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# # #                     self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# # #                     continue
                
# # #                 # Mirror the frame for more intuitive laptop usage
# # #                 frame = cv2.flip(frame, 1)
                
# # #                 # Process frame for smile detection
# # #                 frame = self.detect_smile(frame)
                
# # #                 # Display status
# # #                 status_text = f"Voice: {'Yes' if self.voice_detected else 'No'}, Smile: {'Yes' if self.smile_detected else 'No'}"
# # #                 cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
# # #                 # Display photo count
# # #                 cv2.putText(frame, f"Photos: {self.photos_taken}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                
# # #                 # Capture photo if conditions are met
# # #                 self.capture_photo(frame)
                
# # #                 # Show frame
# # #                 cv2.imshow('Voice and Smile Camera', frame)
                
# # #                 # Break loop on 'q' key or ESC
# # #                 key = cv2.waitKey(1) & 0xFF
# # #                 if key == ord('q') or key == 27:  # 27 is ESC key
# # #                     break
        
# # #         finally:
# # #             print(f"Shutting down. Total photos taken: {self.photos_taken}")
# # #             self.stop_thread = True
# # #             self.voice_thread.join(timeout=1)
# # #             self.cap.release()
# # #             self.audio.terminate()
# # #             cv2.destroyAllWindows()

# # # if __name__ == "__main__":
# # #     print("Starting Voice and Smile Camera for Laptop...")
# # #     print("The program will first calibrate your microphone.")
# # #     print("Speak and smile to take a photo!")
# # #     print("Press 'q' or ESC to quit")
    
# # #     try:
# # #         camera = LaptopVoiceSmileCamera()
# # #         camera.run()
# # #     except Exception as e:
# # #         print(f"Error: {e}")
# # #         import traceback
# # #         traceback.print_exc()
        
# # #         # Keep terminal window open if there's an error
# # #         input("Press Enter to exit...")


# # import cv2
# # import numpy as np
# # import pyaudio
# # import threading
# # import time
# # from datetime import datetime
# # import speech_recognition as sr

# # class VoiceCommandCamera:
# #     def __init__(self):
# #         # Initialize laptop camera
# #         self.cap = cv2.VideoCapture(0)  # 0 is typically the built-in webcam
        
# #         # Set lower resolution for better performance on laptops
# #         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# #         self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
# #         if not self.cap.isOpened():
# #             raise IOError("Cannot open laptop webcam")
        
# #         # Load face cascade and smile cascade
# #         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# #         self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        
# #         # Speech recognition trigger words
# #         self.trigger_words = ["cheese", "capture", "take a photo", "snapshot", "smile", "picture"]
        
# #         # Detection variables
# #         self.command_detected = False
# #         self.command_detection_time = 0
# #         self.command_timeout = 3  # Command detection remains valid for 3 seconds
# #         self.smile_detected = False
# #         self.last_recognized_command = ""
        
# #         # Photo capture variables
# #         self.last_capture_time = 0
# #         self.capture_cooldown = 2  # Seconds between captures
# #         self.photos_taken = 0
        
# #         # Speech recognition setup
# #         self.recognizer = sr.Recognizer()
# #         self.microphone = sr.Microphone()
        
# #         # Calibrate the recognizer for ambient noise
# #         print("Calibrating microphone for ambient noise - please be quiet for a moment...")
# #         with self.microphone as source:
# #             self.recognizer.adjust_for_ambient_noise(source, duration=2)
# #         print("Microphone calibrated!")
        
# #         # Start voice recognition in a separate thread
# #         self.stop_thread = False
# #         self.voice_thread = threading.Thread(target=self.recognize_speech)
# #         self.voice_thread.daemon = True
# #         self.voice_thread.start()
    
# #     def recognize_speech(self):
# #         """Continuously listen for speech commands in background thread"""
# #         print("Voice command recognition started")
# #         print(f"Listening for trigger words: {', '.join(self.trigger_words)}")
        
# #         while not self.stop_thread:
# #             try:
# #                 # Use the microphone as source
# #                 with self.microphone as source:
# #                     print("Listening...")
# #                     # Set timeout to prevent blocking indefinitely
# #                     audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)
                
# #                 try:
# #                     # Use Google's speech recognition
# #                     text = self.recognizer.recognize_google(audio).lower()
# #                     print(f"Recognized: {text}")
                    
# #                     # Check if any trigger word is in the recognized text
# #                     for word in self.trigger_words:
# #                         if word.lower() in text:
# #                             print(f"Trigger word detected: {word}")
# #                             self.command_detected = True
# #                             self.command_detection_time = time.time()
# #                             self.last_recognized_command = word
# #                             break
                            
# #                 except sr.UnknownValueError:
# #                     # Speech was unintelligible
# #                     pass
# #                 except sr.RequestError as e:
# #                     print(f"Could not request results; {e}")
# #                     time.sleep(2)  # Wait before trying again
                    
# #             except Exception as e:
# #                 print(f"Error in speech recognition: {e}")
# #                 time.sleep(1)
            
# #             # Check if command has timed out
# #             if time.time() - self.command_detection_time > self.command_timeout:
# #                 self.command_detected = False
    
# #     def detect_smile(self, frame):
# #         """Detect smile in the current frame - optimized for laptop cameras"""
# #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #         # Equalize histogram to improve detection in varying laptop lighting
# #         gray = cv2.equalizeHist(gray)
        
# #         # More suitable parameters for laptop cameras
# #         faces = self.face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(100, 100))
        
# #         self.smile_detected = False
        
# #         for (x, y, w, h) in faces:
# #             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
# #             roi_gray = gray[y:y+h, x:x+w]
# #             roi_color = frame[y:y+h, x:x+w]
            
# #             # Laptop-optimized smile detection parameters
# #             smiles = self.smile_cascade.detectMultiScale(
# #                 roi_gray, 
# #                 scaleFactor=1.7, 
# #                 minNeighbors=22, 
# #                 minSize=(25, 25)
# #             )
            
# #             for (sx, sy, sw, sh) in smiles:
# #                 cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
# #                 self.smile_detected = True
        
# #         return frame
    
# #     def capture_photo(self, frame):
# #         """Take a photo when a trigger word is spoken and smile is detected"""
# #         current_time = time.time()
        
# #         if (self.command_detected and self.smile_detected and 
# #                 current_time - self.last_capture_time > self.capture_cooldown):
# #             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# #             filename = f"command_photo_{timestamp}.jpg"
# #             cv2.imwrite(filename, frame)
# #             self.photos_taken += 1
# #             print(f"Photo captured: {filename} (Total: {self.photos_taken})")
            
# #             self.last_capture_time = current_time
            
# #             # Display "Photo Taken!" message with the command used
# #             height, width = frame.shape[:2]
# #             cv2.putText(frame, f"Photo Taken! ({self.last_recognized_command})", 
# #                        (width//6, height//2), 
# #                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)
            
# #             # Show the captured frame for a moment
# #             cv2.imshow('Voice Command Camera', frame)
# #             cv2.waitKey(1000)  # Display for 1 second
            
# #             # Reset command detection after capturing
# #             self.command_detected = False
    
# #     def run(self):
# #         """Main method to run the camera"""
# #         try:
# #             print("Camera initialized. Preparing interface...")
# #             time.sleep(1)  # Give the camera a moment to warm up
            
# #             while True:
# #                 ret, frame = self.cap.read()
# #                 if not ret:
# #                     print("Failed to grab frame - trying to reinitialize camera")
# #                     self.cap.release()
# #                     time.sleep(1)
# #                     self.cap = cv2.VideoCapture(0)
# #                     self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# #                     self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# #                     continue
                
# #                 # Mirror the frame for more intuitive laptop usage
# #                 frame = cv2.flip(frame, 1)
                
# #                 # Process frame for smile detection
# #                 frame = self.detect_smile(frame)
                
# #                 # Display status
# #                 command_status = self.last_recognized_command if self.command_detected else "None"
# #                 status_text = f"Command: {command_status}, Smile: {'Yes' if self.smile_detected else 'No'}"
# #                 cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
# #                 # Display photo count and instructions
# #                 cv2.putText(frame, f"Photos: {self.photos_taken}", (10, 60), 
# #                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
# #                 cv2.putText(frame, "Say: cheese, capture, take a photo, etc.", 
# #                            (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
# #                 # Capture photo if conditions are met
# #                 self.capture_photo(frame)
                
# #                 # Show frame
# #                 cv2.imshow('Voice Command Camera', frame)
                
# #                 # Break loop on 'q' key or ESC
# #                 key = cv2.waitKey(1) & 0xFF
# #                 if key == ord('q') or key == 27:  # 27 is ESC key
# #                     break
        
# #         finally:
# #             print(f"Shutting down. Total photos taken: {self.photos_taken}")
# #             self.stop_thread = True
# #             self.voice_thread.join(timeout=1)
# #             self.cap.release()
# #             cv2.destroyAllWindows()

# # if __name__ == "__main__":
# #     print("Starting Voice Command Camera...")
# #     print("Say one of these words while smiling to take a photo:")
# #     print("  - cheese")
# #     print("  - capture")
# #     print("  - take a photo")
# #     print("  - snapshot")
# #     print("  - smile")
# #     print("  - picture")
# #     print("Press 'q' or ESC to quit")
    
# #     try:
# #         camera = VoiceCommandCamera()
# #         camera.run()
# #     except Exception as e:
# #         print(f"Error: {e}")
# #         import traceback
# #         traceback.print_exc()
        
# #         # Keep terminal window open if there's an error
# #         input("Press Enter to exit...")


# import cv2
# import numpy as np
# import threading
# import time
# from datetime import datetime
# import speech_recognition as sr

# class VoiceCommandCamera:
#     def __init__(self):
#         # Initialize laptop camera
#         self.cap = cv2.VideoCapture(0)  # 0 is typically the built-in webcam
        
#         # Set lower resolution for better performance on laptops
#         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#         self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
#         if not self.cap.isOpened():
#             raise IOError("Cannot open laptop webcam")
        
#         # Load face cascade and smile cascade
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#         self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        
#         # Speech recognition trigger words
#         self.trigger_words = ["cheese", "capture", "take a photo", "snapshot", "smile", "picture"]
        
#         # Detection variables
#         self.command_detected = False
#         self.command_detection_time = 0
#         self.command_timeout = 3  # Command detection remains valid for 3 seconds
#         self.smile_detected = False
#         self.last_recognized_command = ""
        
#         # Photo capture variables
#         self.last_capture_time = 0
#         self.capture_cooldown = 2  # Seconds between captures
#         self.photos_taken = 0
#         self.show_capture_message = False
#         self.capture_message_time = 0
#         self.capture_message_duration = 1.5  # How long to show the "Photo Taken!" message
        
#         # Display toggles
#         self.show_debug_info = True  # Will be toggled with 'd' key
        
#         # Speech recognition setup
#         self.recognizer = sr.Recognizer()
#         self.microphone = sr.Microphone()
        
#         # Calibrate the recognizer for ambient noise
#         print("Calibrating microphone for ambient noise - please be quiet for a moment...")
#         with self.microphone as source:
#             self.recognizer.adjust_for_ambient_noise(source, duration=2)
#         print("Microphone calibrated!")
        
#         # Start voice recognition in a separate thread
#         self.stop_thread = False
#         self.voice_thread = threading.Thread(target=self.recognize_speech)
#         self.voice_thread.daemon = True
#         self.voice_thread.start()
    
#     def recognize_speech(self):
#         """Continuously listen for speech commands in background thread"""
#         print("Voice command recognition started")
#         print(f"Listening for trigger words: {', '.join(self.trigger_words)}")
        
#         while not self.stop_thread:
#             try:
#                 # Use the microphone as source
#                 with self.microphone as source:
#                     print("Listening...")
#                     # Set timeout to prevent blocking indefinitely
#                     audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)
                
#                 try:
#                     # Use Google's speech recognition
#                     text = self.recognizer.recognize_google(audio).lower()
#                     print(f"Recognized: {text}")
                    
#                     # Check if any trigger word is in the recognized text
#                     for word in self.trigger_words:
#                         if word.lower() in text:
#                             print(f"Trigger word detected: {word}")
#                             self.command_detected = True
#                             self.command_detection_time = time.time()
#                             self.last_recognized_command = word
#                             break
                            
#                 except sr.UnknownValueError:
#                     # Speech was unintelligible
#                     pass
#                 except sr.RequestError as e:
#                     print(f"Could not request results; {e}")
#                     time.sleep(2)  # Wait before trying again
                    
#             except Exception as e:
#                 print(f"Error in speech recognition: {e}")
#                 time.sleep(1)
            
#             # Check if command has timed out
#             if time.time() - self.command_detection_time > self.command_timeout:
#                 self.command_detected = False
    
#     def detect_smile(self, frame):
#         """Detect smile in the current frame - optimized for laptop cameras"""
#         # Make a clean copy of the frame before any annotations
#         clean_frame = frame.copy()
        
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         # Equalize histogram to improve detection in varying laptop lighting
#         gray = cv2.equalizeHist(gray)
        
#         # Detection flags
#         faces_found = False
#         smile_found = False
        
#         # More suitable parameters for laptop cameras
#         faces = self.face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(100, 100))
        
#         self.smile_detected = False
        
#         # Only add visualization if debug info is enabled
#         if self.show_debug_info:
#             for (x, y, w, h) in faces:
#                 faces_found = True
#                 cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#                 roi_gray = gray[y:y+h, x:x+w]
#                 roi_color = frame[y:y+h, x:x+w]
                
#                 # Laptop-optimized smile detection parameters
#                 smiles = self.smile_cascade.detectMultiScale(
#                     roi_gray, 
#                     scaleFactor=1.7, 
#                     minNeighbors=22, 
#                     minSize=(25, 25)
#                 )
                
#                 for (sx, sy, sw, sh) in smiles:
#                     smile_found = True
#                     cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
#                     self.smile_detected = True
#         else:
#             # Still do the detection but without visualization
#             for (x, y, w, h) in faces:
#                 faces_found = True
#                 roi_gray = gray[y:y+h, x:x+w]
                
#                 # Laptop-optimized smile detection parameters
#                 smiles = self.smile_cascade.detectMultiScale(
#                     roi_gray, 
#                     scaleFactor=1.7, 
#                     minNeighbors=22, 
#                     minSize=(25, 25)
#                 )
                
#                 if len(smiles) > 0:
#                     smile_found = True
#                     self.smile_detected = True
        
#         return frame, clean_frame, faces_found, smile_found
    
#     def capture_photo(self, frame, clean_frame):
#         """Take a photo when a trigger word is spoken and smile is detected"""
#         current_time = time.time()
        
#         if (self.command_detected and self.smile_detected and 
#                 current_time - self.last_capture_time > self.capture_cooldown):
#             timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#             filename = f"photo_{timestamp}.jpg"
            
#             # Save the clean frame without any overlays
#             cv2.imwrite(filename, clean_frame)
#             self.photos_taken += 1
#             print(f"Photo captured: {filename} (Total: {self.photos_taken})")
            
#             self.last_capture_time = current_time
            
#             # Set the capture message flag and time
#             self.show_capture_message = True
#             self.capture_message_time = current_time
            
#             # Reset command detection after capturing
#             self.command_detected = False
            
#             return True
#         return False
    
#     def run(self):
#         """Main method to run the camera"""
#         try:
#             print("Camera initialized. Preparing interface...")
#             print("Press 'd' to toggle debug information")
#             time.sleep(1)  # Give the camera a moment to warm up
            
#             while True:
#                 ret, frame = self.cap.read()
#                 if not ret:
#                     print("Failed to grab frame - trying to reinitialize camera")
#                     self.cap.release()
#                     time.sleep(1)
#                     self.cap = cv2.VideoCapture(0)
#                     self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#                     self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#                     continue
                
#                 # Mirror the frame for more intuitive laptop usage
#                 frame = cv2.flip(frame, 1)
                
#                 # Process frame for smile detection
#                 display_frame, clean_frame, faces_found, smile_found = self.detect_smile(frame.copy())
                
#                 # Check if capture message should be cleared
#                 current_time = time.time()
#                 if self.show_capture_message and current_time - self.capture_message_time > self.capture_message_duration:
#                     self.show_capture_message = False
                
#                 # Display debug information if enabled
#                 if self.show_debug_info:
#                     # Display status
#                     command_status = self.last_recognized_command if self.command_detected else "None"
#                     status_text = f"Command: {command_status}, Smile: {'Yes' if self.smile_detected else 'No'}"
#                     cv2.putText(display_frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                    
#                     # Display photo count and instructions
#                     cv2.putText(display_frame, f"Photos: {self.photos_taken}", (10, 60), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
#                     cv2.putText(display_frame, "Say: cheese, capture, take a photo, etc.", 
#                                (10, display_frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    
#                     # Display face/smile detection status
#                     detection_status = f"Face: {'Yes' if faces_found else 'No'}, Smile detected: {'Yes' if smile_found else 'No'}"
#                     cv2.putText(display_frame, detection_status, (10, 90), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
#                 # Capture photo if conditions are met (using the clean frame)
#                 photo_taken = self.capture_photo(display_frame, clean_frame)
                
#                 # Always show the "Photo Taken!" message if needed, even in non-debug mode
#                 if self.show_capture_message:
#                     height, width = display_frame.shape[:2]
#                     cv2.putText(display_frame, f"Photo Taken! ({self.last_recognized_command})", 
#                                (width//6, height//2), 
#                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)
                
#                 # Show frame
#                 cv2.imshow('Voice Command Camera', display_frame)
                
#                 # Key handling
#                 key = cv2.waitKey(1) & 0xFF
#                 if key == ord('q') or key == 27:  # 'q' or ESC to quit
#                     break
#                 elif key == ord('d'):  # 'd' to toggle debug info
#                     self.show_debug_info = not self.show_debug_info
#                     print(f"Debug info: {'On' if self.show_debug_info else 'Off'}")
        
#         finally:
#             print(f"Shutting down. Total photos taken: {self.photos_taken}")
#             self.stop_thread = True
#             self.voice_thread.join(timeout=1)
#             self.cap.release()
#             cv2.destroyAllWindows()

# if __name__ == "__main__":
#     print("Starting Voice Command Camera...")
#     print("Say one of these words while smiling to take a photo:")
#     print("  - cheese")
#     print("  - capture")
#     print("  - take a photo")
#     print("  - snapshot")
#     print("  - smile")
#     print("  - picture")
#     print("Press 'd' to toggle debug information")
#     print("Press 'q' or ESC to quit")
    
#     try:
#         camera = VoiceCommandCamera()
#         camera.run()
#     except Exception as e:
#         print(f"Error: {e}")
#         import traceback
#         traceback.print_exc()
        
#         # Keep terminal window open if there's an error
#         input("Press Enter to exit...")



import cv2
import numpy as np
import threading
import time
from datetime import datetime
import speech_recognition as sr
import os

class VoiceCommandCamera:
    def __init__(self):
        # Initialize laptop camera
        self.cap = cv2.VideoCapture(0)  # 0 is typically the built-in webcam
        
        # Set lower resolution for better performance on laptops
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        if not self.cap.isOpened():
            raise IOError("Cannot open laptop webcam")
        
        # Load face cascade and smile cascade
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        
        # Load age and gender models
        self.initialize_age_gender_models()
        
        # Speech recognition trigger words
        self.trigger_words = ["cheese", "capture", "take a photo", "snapshot", "smile", "picture"]
        
        # Detection variables
        self.command_detected = False
        self.command_detection_time = 0
        self.command_timeout = 3  # Command detection remains valid for 3 seconds
        self.smile_detected = False
        self.last_recognized_command = ""
        
        # Photo capture variables
        self.last_capture_time = 0
        self.capture_cooldown = 2  # Seconds between captures
        self.photos_taken = 0
        self.show_capture_message = False
        self.capture_message_time = 0
        self.capture_message_duration = 1.5  # How long to show the "Photo Taken!" message
        
        # Age and gender detection results
        self.age_gender_results = []
        
        # Display toggles
        self.show_debug_info = True  # Will be toggled with 'd' key
        
        # Speech recognition setup
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Calibrate the recognizer for ambient noise
        print("Calibrating microphone for ambient noise - please be quiet for a moment...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Microphone calibrated!")
        
        # Start voice recognition in a separate thread
        self.stop_thread = False
        self.voice_thread = threading.Thread(target=self.recognize_speech)
        self.voice_thread.daemon = True
        self.voice_thread.start()
    
    def initialize_age_gender_models(self):
        """Initialize and load the age and gender models"""
        print("Loading age and gender detection models...")
        
        # Create model directory if it doesn't exist
        if not os.path.exists("models"):
            os.makedirs("models")
        
        # Define model URLs and file paths
        model_urls = {
            "age_deploy": "https://github.com/opencv/opencv/raw/master/samples/dnn/face_detector/deploy.prototxt",
            "age_model": "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel",
            "age_net": "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20180205_fp16/res10_300x300_ssd_iter_140000_fp16.caffemodel",
            "gender_deploy": "https://github.com/tony4d/age-gender-estimation/raw/master/deploy_gender.prototxt",
            "gender_model": "https://github.com/eveningglow/age-and-gender-classification/raw/master/model/gender_net.caffemodel",
            "age_deploy_age": "https://github.com/tony4d/age-gender-estimation/raw/master/deploy_age.prototxt",
            "age_model_age": "https://github.com/eveningglow/age-and-gender-classification/raw/master/model/age_net.caffemodel"
        }
        
        model_files = {
            "face_detector_prototxt": "models/deploy.prototxt",
            "face_detector_model": "models/res10_300x300_ssd_iter_140000.caffemodel",
            "age_prototxt": "models/deploy_age.prototxt",
            "age_model": "models/age_net.caffemodel",
            "gender_prototxt": "models/deploy_gender.prototxt",
            "gender_model": "models/gender_net.caffemodel"
        }
        
        # Check if we need to download models
        models_exist = all(os.path.exists(file_path) for file_path in model_files.values())
        
        if not models_exist:
            print("Some model files are missing. You'll need to download them manually.")
            print("Please visit the OpenCV DNN face detection and age/gender classification GitHub repositories")
            print("and download the necessary model files into a 'models' directory.")
            
            # If models don't exist, we'll still initialize the DNN but it won't work correctly
            # This allows the program to run, but age/gender detection will be disabled
            self.use_age_gender = False
            print("Age and gender detection will be disabled.")
            return
        
        # Load models
        try:
            # Face detection model
            self.face_net = cv2.dnn.readNet(model_files["face_detector_model"], 
                                          model_files["face_detector_prototxt"])
            
            # Age detection model
            self.age_net = cv2.dnn.readNet(model_files["age_model"], 
                                         model_files["age_prototxt"])
            
            # Gender detection model
            self.gender_net = cv2.dnn.readNet(model_files["gender_model"], 
                                            model_files["gender_prototxt"])
            
            # Model parameters
            self.model_mean_values = (78.4263377603, 87.7689143744, 114.895847746)
            self.age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
            self.gender_list = ['Male', 'Female']
            
            self.use_age_gender = True
            print("Age and gender detection models loaded successfully!")
            
        except Exception as e:
            print(f"Error loading age and gender models: {e}")
            self.use_age_gender = False
            print("Age and gender detection will be disabled.")
    
    def recognize_speech(self):
        """Continuously listen for speech commands in background thread"""
        print("Voice command recognition started")
        print(f"Listening for trigger words: {', '.join(self.trigger_words)}")
        
        while not self.stop_thread:
            try:
                # Use the microphone as source
                with self.microphone as source:
                    print("Listening...")
                    # Set timeout to prevent blocking indefinitely
                    audio = self.recognizer.listen(source, timeout=10, phrase_time_limit=5)
                
                try:
                    # Use Google's speech recognition
                    text = self.recognizer.recognize_google(audio).lower()
                    print(f"Recognized: {text}")
                    
                    # Check if any trigger word is in the recognized text
                    for word in self.trigger_words:
                        if word.lower() in text:
                            print(f"Trigger word detected: {word}")
                            self.command_detected = True
                            self.command_detection_time = time.time()
                            self.last_recognized_command = word
                            break
                            
                except sr.UnknownValueError:
                    # Speech was unintelligible
                    pass
                except sr.RequestError as e:
                    print(f"Could not request results; {e}")
                    time.sleep(2)  # Wait before trying again
                    
            except Exception as e:
                print(f"Error in speech recognition: {e}")
                time.sleep(1)
            
            # Check if command has timed out
            if time.time() - self.command_detection_time > self.command_timeout:
                self.command_detected = False
    
    def detect_age_gender(self, frame, faces):
        """Detect age and gender for detected faces"""
        if not self.use_age_gender:
            return []
        
        self.age_gender_results = []
        
        for (x, y, w, h) in faces:
            # Extract face ROI for age and gender detection
            face_img = frame[y:y+h, x:x+w].copy()
            if face_img.size == 0:
                continue
                
            # Resize and preprocess for age and gender networks
            try:
                blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227), 
                                           self.model_mean_values, swapRB=False)
                
                # Gender prediction
                self.gender_net.setInput(blob)
                gender_preds = self.gender_net.forward()
                gender = self.gender_list[gender_preds[0].argmax()]
                
                # Age prediction
                self.age_net.setInput(blob)
                age_preds = self.age_net.forward()
                age = self.age_list[age_preds[0].argmax()]
                
                # Store result for this face
                self.age_gender_results.append({
                    "position": (x, y, w, h),
                    "age": age,
                    "gender": gender
                })
            except Exception as e:
                print(f"Error in age/gender detection: {e}")
                
        return self.age_gender_results
    
    def detect_smile(self, frame):
        """Detect smile in the current frame with age and gender detection"""
        # Make a clean copy of the frame before any annotations
        clean_frame = frame.copy()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Equalize histogram to improve detection in varying laptop lighting
        gray = cv2.equalizeHist(gray)
        
        # Detection flags
        faces_found = False
        smile_found = False
        
        # More suitable parameters for laptop cameras
        faces = self.face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(100, 100))
        
        self.smile_detected = False
        
        # Detect age and gender for all faces
        age_gender_results = []
        # FIX: Changed faces.size > 0 to len(faces) > 0
        if len(faces) > 0 and hasattr(self, 'use_age_gender') and self.use_age_gender:
            age_gender_results = self.detect_age_gender(frame, faces)
        
        # Only add visualization if debug info is enabled
        if self.show_debug_info:
            for i, (x, y, w, h) in enumerate(faces):
                faces_found = True
                
                # Draw face rectangle
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                # Check if we have age/gender for this face
                age_gender_text = ""
                if i < len(age_gender_results):
                    age = age_gender_results[i]["age"]
                    gender = age_gender_results[i]["gender"]
                    age_gender_text = f"{gender}, {age}"
                    # Put age/gender text above face rectangle
                    cv2.putText(frame, age_gender_text, (x, y-10),
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
                
                # Smile detection
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                
                # Laptop-optimized smile detection parameters
                smiles = self.smile_cascade.detectMultiScale(
                    roi_gray, 
                    scaleFactor=1.7, 
                    minNeighbors=22, 
                    minSize=(25, 25)
                )
                
                for (sx, sy, sw, sh) in smiles:
                    smile_found = True
                    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)
                    self.smile_detected = True
        else:
            # Still do the detection but without visualization
            for (x, y, w, h) in faces:
                faces_found = True
                roi_gray = gray[y:y+h, x:x+w]
                
                # Laptop-optimized smile detection parameters
                smiles = self.smile_cascade.detectMultiScale(
                    roi_gray, 
                    scaleFactor=1.7, 
                    minNeighbors=22, 
                    minSize=(25, 25)
                )
                
                if len(smiles) > 0:
                    smile_found = True
                    self.smile_detected = True
        
        return frame, clean_frame, faces_found, smile_found, age_gender_results
    
    def capture_photo(self, frame, clean_frame, age_gender_results):
        """Take a photo when a trigger word is spoken and smile is detected"""
        current_time = time.time()
        
        if (self.command_detected and self.smile_detected and 
                current_time - self.last_capture_time > self.capture_cooldown):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            # Create a basic filename
            filename = f"photo_{timestamp}.jpg"
            
            # If we have age and gender info, include it in the filename
            if len(age_gender_results) > 0:
                # Use the first face's age and gender for the filename
                age = age_gender_results[0]["age"].replace("(", "").replace(")", "")
                gender = age_gender_results[0]["gender"]
                filename = f"photo_{gender}_{age}_{timestamp}.jpg"
            
            # Save the clean frame without any overlays
            cv2.imwrite(filename, clean_frame)
            self.photos_taken += 1
            print(f"Photo captured: {filename} (Total: {self.photos_taken})")
            
            # If we have age/gender, print that too
            if len(age_gender_results) > 0:
                for i, result in enumerate(age_gender_results):
                    print(f"Person {i+1}: {result['gender']}, Age {result['age']}")
            
            self.last_capture_time = current_time
            
            # Set the capture message flag and time
            self.show_capture_message = True
            self.capture_message_time = current_time
            
            # Reset command detection after capturing
            self.command_detected = False
            
            return True
        return False
    
    def run(self):
        """Main method to run the camera"""
        try:
            print("Camera initialized. Preparing interface...")
            print("Press 'd' to toggle debug information")
            time.sleep(1)  # Give the camera a moment to warm up
            
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("Failed to grab frame - trying to reinitialize camera")
                    self.cap.release()
                    time.sleep(1)
                    self.cap = cv2.VideoCapture(0)
                    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
                    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
                    continue
                
                # Mirror the frame for more intuitive laptop usage
                frame = cv2.flip(frame, 1)
                
                # Process frame for face, smile, age and gender detection
                display_frame, clean_frame, faces_found, smile_found, age_gender_results = self.detect_smile(frame.copy())
                
                # Check if capture message should be cleared
                current_time = time.time()
                if self.show_capture_message and current_time - self.capture_message_time > self.capture_message_duration:
                    self.show_capture_message = False
                
                # Display debug information if enabled
                if self.show_debug_info:
                    # Display status
                    command_status = self.last_recognized_command if self.command_detected else "None"
                    status_text = f"Command: {command_status}, Smile: {'Yes' if self.smile_detected else 'No'}"
                    cv2.putText(display_frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                    
                    # Display photo count and instructions
                    cv2.putText(display_frame, f"Photos: {self.photos_taken}", (10, 60), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
                    
                    # Show if age/gender detection is active
                    age_gender_status = "A/G: On" if hasattr(self, 'use_age_gender') and self.use_age_gender else "A/G: Off"
                    cv2.putText(display_frame, age_gender_status, (display_frame.shape[1] - 100, 30),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
                    
                    # Display trigger word instructions
                    cv2.putText(display_frame, "Say: cheese, capture, take a photo, etc.", 
                               (10, display_frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    
                    # Display face/smile detection status
                    detection_status = f"Face: {'Yes' if faces_found else 'No'}, Smile detected: {'Yes' if smile_found else 'No'}"
                    cv2.putText(display_frame, detection_status, (10, 90), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                
                # Capture photo if conditions are met (using the clean frame)
                photo_taken = self.capture_photo(display_frame, clean_frame, age_gender_results)
                
                # Always show the "Photo Taken!" message if needed, even in non-debug mode
                if self.show_capture_message:
                    height, width = display_frame.shape[:2]
                    
                    # If we have age and gender info, include it in the message
                    message = f"Photo Taken! ({self.last_recognized_command})"
                    if len(age_gender_results) > 0:
                        age = age_gender_results[0]["age"]
                        gender = age_gender_results[0]["gender"]
                        message = f"Photo Taken! {gender}, Age {age}"
                    
                    cv2.putText(display_frame, message, (width//6, height//2), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)
                
                # Show frame
                cv2.imshow('Voice Command Camera', display_frame)
                
                # Key handling
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q') or key == 27:  # 'q' or ESC to quit
                    break
                elif key == ord('d'):  # 'd' to toggle debug info
                    self.show_debug_info = not self.show_debug_info
                    print(f"Debug info: {'On' if self.show_debug_info else 'Off'}")
        
        finally:
            print(f"Shutting down. Total photos taken: {self.photos_taken}")
            self.stop_thread = True
            self.voice_thread.join(timeout=1)
            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Starting Voice Command Camera with Age and Gender Detection...")
    print("Say one of these words while smiling to take a photo:")
    print("  - cheese")
    print("  - capture")
    print("  - take a photo")
    print("  - snapshot")
    print("  - smile")
    print("  - picture")
    print("Press 'd' to toggle debug information")
    print("Press 'q' or ESC to quit")
    
    try:
        camera = VoiceCommandCamera()
        camera.run()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        
        # Keep terminal window open if there's an error
        input("Press Enter to exit...")