# import tkinter as tk
# from tkinter import ttk
# import webbrowser
# from datetime import datetime
# from PIL import Image, ImageTk
# import urllib.parse

# class InfoDialog:
#     def __init__(self, parent):
#         self.dialog = tk.Toplevel(parent)
#         self.dialog.title("How to Use JARVIS")
#         self.dialog.configure(bg='#1e1e1e')
        
#         dialog_width = 400
#         dialog_height = 500
#         screen_width = parent.winfo_screenwidth()
#         screen_height = parent.winfo_screenheight()
#         center_x = int(screen_width/2 - dialog_width/2)
#         center_y = int(screen_height/2 - dialog_height/2)
#         self.dialog.geometry(f'{dialog_width}x{dialog_height}+{center_x}+{center_y}')
        
#         self.dialog.transient(parent)
#         self.dialog.grab_set()

#         title_label = tk.Label(self.dialog, text="JARVIS User Guide", font=("Arial", 16, "bold"), bg='#1e1e1e', fg='white', pady=20)
#         title_label.pack()
        
#         instructions = """1. Getting Started:
#    • Click the green 'Start' button to activate JARVIS
#    • The system indicator will turn green when active
#    • Watch the center circle animate to confirm activation

# 2. Navigation:
#    • ⚙ (Settings): Configure system preferences
#    • ℹ (Info): View this help guide
#    • ✉ (Email): Open Gmail compose window

# 3. Status Indicators:
#    • Grey dot: System is inactive
#    • Green dot: System is active and running
#    • Time display: Shows current system time

# 4. Email Function:
#    • Click the email icon to open Gmail
#    • A new compose window will open
#    • The default recipient will be pre-filled

# 5. System States:
#    • Inactive: Default state on startup
#    • Active: System running with animations
#    • Processing: Shown by circle animation

# 6. Tips:
#    • Keep the window open to maintain activation
#    • Check the status indicator for system state
#    • Use the email function for quick communication
# """
        
#         text_frame = tk.Frame(self.dialog, bg='#1e1e1e')
#         text_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
#         scrollbar = tk.Scrollbar(text_frame)
#         scrollbar.pack(side='right', fill='y')
        
#         text_widget = tk.Text(text_frame, wrap=tk.WORD, bg='#2d2d2d', fg='white', font=("Arial", 11), padx=10, pady=10, yscrollcommand=scrollbar.set)
#         text_widget.pack(side='left', fill='both', expand=True)
#         scrollbar.config(command=text_widget.yview)
        
#         text_widget.insert('1.0', instructions)
#         text_widget.config(state='disabled')
        
#         close_btn = tk.Button(self.dialog, text="Close", font=("Arial", 12), bg='#28a745', fg='white', command=self.dialog.destroy, width=10, bd=0, highlightthickness=0)
#         close_btn.pack(pady=20)

# class JarvisGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("JARVIS ONLINE")
#         self.root.configure(bg='black')
        
#         window_width = 800
#         window_height = 600
#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()
#         center_x = int(screen_width/2 - window_width/2)
#         center_y = int(screen_height/2 - window_height/2)
#         self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        
#         self.recipient_email = "example@gmail.com"

#         self.main_frame = tk.Frame(root, bg='black')
#         self.main_frame.pack(expand=True, fill='both')

#         self.top_frame = tk.Frame(self.main_frame, bg='black')
#         self.top_frame.pack(fill='x', padx=20, pady=10)

#         self.time_label = tk.Label(self.top_frame, text="", font=("Arial", 14), bg='black', fg='white')
#         self.time_label.pack(side='left')

#         self.status_frame = tk.Frame(self.top_frame, bg='black')
#         self.status_frame.pack(side='left', padx=20)

#         self.status_indicator = tk.Canvas(self.status_frame, width=10, height=10, bg='black', highlightthickness=0)
#         self.status_indicator.pack(side='left')
#         self.status_indicator.create_oval(0, 0, 10, 10, fill='grey')

#         self.status_label = tk.Label(self.status_frame, text="System Inactive", font=("Arial", 12), bg='black', fg='white')
#         self.status_label.pack(side='left', padx=5)

#         self.icons_frame = tk.Frame(self.top_frame, bg='black')
#         self.icons_frame.pack(side='right')

#         self.settings_btn = tk.Button(self.icons_frame, text="⚙", font=("Arial", 12), bg='black', fg='white', bd=0, highlightthickness=0)
#         self.settings_btn.pack(side='left', padx=5)

#         self.info_btn = tk.Button(self.icons_frame, text="ℹ", font=("Arial", 12), bg='black', fg='white', bd=0, highlightthickness=0, command=self.show_info)
#         self.info_btn.pack(side='left', padx=5)

#         self.email_btn = tk.Button(self.icons_frame, text="✉", font=("Arial", 12), bg='black', fg='white', bd=0, highlightthickness=0, command=self.open_gmail_compose)
#         self.email_btn.pack(side='left', padx=5)

#         self.circle_canvas = tk.Label(self.main_frame, bg='black')
#         self.circle_canvas.pack(expand=True)

#         self.start_btn = tk.Button(self.main_frame, text="Start", font=("Arial", 14), bg='#28a745', fg='white', width=10, command=self.start_system, bd=0, highlightthickness=0)
#         self.start_btn.pack(pady=20)

#         self.gif_path = "D:\Material_gui_jarvis\logo.gif"
#         self.frames = []
#         self.load_gif()
#         self.current_frame = 0
#         self.animation_running = False

#         self.update_time()

#     def load_gif(self):
#         try:
#             gif = Image.open(self.gif_path)
#             for frame in range(gif.n_frames):
#                 gif.seek(frame)
#                 resized_frame = gif.resize((150, 150))
#                 self.frames.append(ImageTk.PhotoImage(resized_frame))
#         except Exception as e:
#             print("Error loading GIF:", e)

#     def show_info(self):
#         InfoDialog(self.root)

#     def update_time(self):
#         current_time = datetime.now().strftime("%I:%M %p")
#         self.time_label.config(text=current_time)
#         self.root.after(1000, self.update_time)

#     def start_system(self):
#         self.status_indicator.delete("all")
#         self.status_indicator.create_oval(0, 0, 10, 10, fill='#28a745')
#         self.status_label.config(text="System Activated")

#         if not self.animation_running:
#             self.animation_running = True
#             self.play_gif()

#     def play_gif(self):
#         if self.animation_running and self.frames:
#             self.circle_canvas.config(image=self.frames[self.current_frame])
#             self.current_frame = (self.current_frame + 1) % len(self.frames)
#             self.root.after(50, self.play_gif)

#     def open_gmail_compose(self):
#         gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(self.recipient_email)}"
#         webbrowser.open(gmail_url)

# def main():
#     root = tk.Tk()
#     app = JarvisGUI(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()




#____________________________ WORKING OF SPEAK FUNCTION & NAME CHANGED TO NOVA_____________________

# import tkinter as tk
# from tkinter import ttk
# import webbrowser
# from datetime import datetime
# from PIL import Image, ImageTk
# import urllib.parse
# import pyttsx3  # Import the pyttsx3 library for text-to-speech
# import threading  # Import threading for concurrent speech and animation
# import os

# class InfoDialog:
#     def __init__(self, parent):
#         self.dialog = tk.Toplevel(parent)
#         self.dialog.title("How to Use NOVA")
#         self.dialog.configure(bg='#1e1e1e')

#         dialog_width = 400
#         dialog_height = 500
#         screen_width = parent.winfo_screenwidth()
#         screen_height = parent.winfo_screenheight()
#         center_x = int(screen_width/2 - dialog_width/2)
#         center_y = int(screen_height/2 - dialog_height/2)
#         self.dialog.geometry(f'{dialog_width}x{dialog_height}+{center_x}+{center_y}')

#         title_label = tk.Label(self.dialog, text="NOVA User Guide", font=("Arial", 16, "bold"), bg='#1e1e1e', fg='white', pady=20)
#         title_label.pack()

#         instructions = """1. Getting Started:
#    • Click the green 'Start' button to activate NOVA
#    • The system indicator will turn green when active
#    • Watch the center circle animate to confirm activation

# 2. Navigation:
#    • ⚙ (Settings): Configure system preferences
#    • ℹ (Info): View this help guide
#    • ✉ (Email): Open Gmail compose window

# 3. Status Indicators:
#    • Grey dot: System is inactive
#    • Green dot: System is active and running
#    • Time display: Shows current system time

# 4. Email Function:
#    • Click the email icon to open Gmail
#    • A new compose window will open
#    • The default recipient will be pre-filled

# 5. System States:
#    • Inactive: Default state on startup
#    • Active: System running with animations
#    • Processing: Shown by circle animation

# 6. Tips:
#    • Keep the window open to maintain activation
#    • Check the status indicator for system state
#    • Use the email function for quick communication
# """
#         text_frame = tk.Frame(self.dialog, bg='#1e1e1e')
#         text_frame.pack(fill='both', expand=True, padx=20, pady=10)

#         scrollbar = tk.Scrollbar(text_frame)
#         scrollbar.pack(side='right', fill='y')

#         text_widget = tk.Text(text_frame, wrap=tk.WORD, bg='#2d2d2d', fg='white', font=("Arial", 11), padx=10, pady=10, yscrollcommand=scrollbar.set)
#         text_widget.pack(side='left', fill='both', expand=True)
#         scrollbar.config(command=text_widget.yview)

#         text_widget.insert('1.0', instructions)
#         text_widget.config(state='disabled')

#         close_btn = tk.Button(self.dialog, text="Close", font=("Arial", 12), bg='#28a745', fg='white', command=self.dialog.destroy, width=10, bd=0, highlightthickness=0)
#         close_btn.pack(pady=20)

# class JarvisGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("NOVA ONLINE")
#         self.root.configure(bg='black')

#         window_width = 800
#         window_height = 600
#         screen_width = root.winfo_screenwidth()
#         screen_height = root.winfo_screenheight()
#         center_x = int(screen_width/2 - window_width/2)
#         center_y = int(screen_height/2 - window_height/2)
#         self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#         self.recipient_email = "example@gmail.com"

#         self.main_frame = tk.Frame(root, bg='black')
#         self.main_frame.pack(expand=True, fill='both')

#         self.top_frame = tk.Frame(self.main_frame, bg='black')
#         self.top_frame.pack(fill='x', padx=20, pady=10)

#         self.time_label = tk.Label(self.top_frame, text="", font=("Arial", 14), bg='black', fg='white')
#         self.time_label.pack(side='left')

#         self.status_frame = tk.Frame(self.top_frame, bg='black')
#         self.status_frame.pack(side='left', padx=20)

#         self.status_indicator = tk.Canvas(self.status_frame, width=10, height=10, bg='black', highlightthickness=0)
#         self.status_indicator.pack(side='left')
#         self.status_indicator.create_oval(0, 0, 10, 10, fill='grey')

#         self.status_label = tk.Label(self.status_frame, text="System Inactive", font=("Arial", 12), bg='black', fg='white')
#         self.status_label.pack(side='left', padx=5)

#         self.icons_frame = tk.Frame(self.top_frame, bg='black')
#         self.icons_frame.pack(side='right')
        
#         self.settings_btn = tk.Button(self.icons_frame, text="⚙", font=("Arial", 12), bg='black', fg='white', bd=0, highlightthickness=0)
#         self.settings_btn.pack(side='left', padx=5)

#         self.info_btn = tk.Button(self.icons_frame, text="ℹ", font=("Arial", 12), bg='black', fg='white', bd=0, command=self.show_info)
#         self.info_btn.pack(side='left', padx=5)

#         self.email_btn = tk.Button(self.icons_frame, text="✉", font=("Arial", 12), bg='black', fg='white', bd=0, command=self.open_gmail_compose)
#         self.email_btn.pack(side='left', padx=5)

#         self.circle_canvas = tk.Label(self.main_frame, bg='black')
#         self.circle_canvas.pack(expand=True)

#         self.start_btn = tk.Button(self.main_frame, text="Start", font=("Arial", 14), bg='#28a745', fg='white', width=10, command=self.start_system, bd=0)
#         self.start_btn.pack(pady=20)

#         # GIF Animation
#         self.gif_path = r"D:\Material_gui_jarvis\logo.gif"  # Ensure this path is correct
        
#         self.frames = []
#         self.load_gif()
#         self.current_frame = 0
#         self.animation_running = False

#         self.update_time()

#         # Initialize text-to-speech engine
#         self.engine = pyttsx3.init()

#     def load_gif(self):
#         try:
#             if not os.path.exists(self.gif_path):
#                 print(f"Error: GIF not found at {self.gif_path}")
#                 return
#             gif = Image.open(self.gif_path)
#             for frame in range(gif.n_frames):
#                 gif.seek(frame)
#                 resized_frame = gif.resize((150, 150))
#                 self.frames.append(ImageTk.PhotoImage(resized_frame))
#             if not self.frames:
#                 print("Warning: No frames loaded in GIF.")
#         except Exception as e:
#             print(f"Error loading GIF: {e}")

#     def show_info(self):
#         InfoDialog(self.root)

#     def update_time(self):
#         current_time = datetime.now().strftime("%I:%M %p")
#         self.time_label.config(text=current_time)
#         self.root.after(1000, self.update_time)

#     def speak(self, text):
#         """ Function to make the system speak a sentence """
#         self.engine.say(text)
#         self.engine.runAndWait()

#     def start_system(self):
#         sentences = [
#             "Initializing the cloud...",
#             "Starting all systems applications",
#             "Checking all drivers",
#             "Calibrating core processors",
#             "Checking the internet connection",
#             "Updating cloud configuration",
#             "All systems are now activated."
#         ]

#         def speak_thread():
#             for sentence in sentences:
#                 self.speak(sentence)

#         threading.Thread(target=speak_thread, daemon=True).start()

#         self.status_indicator.delete("all")
#         self.status_indicator.create_oval(0, 0, 10, 10, fill='#28a745')
#         self.status_label.config(text="System Activated")

#         if not self.animation_running:
#             self.animation_running = True
#             self.play_gif()

#     def play_gif(self):
#         if self.animation_running and self.frames:
#             self.circle_canvas.config(image=self.frames[self.current_frame])
#             self.current_frame = (self.current_frame + 1) % len(self.frames)
#             self.root.after(50, self.play_gif)

#     def open_gmail_compose(self):
#         gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(self.recipient_email)}"
#         webbrowser.open(gmail_url)

# def main():
#     print("Starting NOVA GUI...")  # Debugging line
#     root = tk.Tk()
#     app = JarvisGUI(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()




#____________________________ WORKING OF SPEAK FUNCTION & NAME CHANGED TO NOVA & CONVERTED TO PYQT6_____________________

    
# import sys
# import os
# import threading
# import urllib.parse
# import webbrowser
# from datetime import datetime
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QDialog,
#     QScrollArea, QFrame
# )
# from PyQt6.QtGui import QPixmap, QMovie, QFont
# from PyQt6.QtCore import Qt, QTimer
# import pyttsx3

# class InfoDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("How to Use NOVA")
#         self.setFixedSize(400, 500)
#         self.setStyleSheet("background-color: #1e1e1e; color: white;")

#         layout = QVBoxLayout()
#         title = QLabel("NOVA User Guide")
#         title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title)

#         instructions = QTextEdit()
#         instructions.setReadOnly(True)
#         instructions.setStyleSheet("background-color: #2d2d2d; color: white; padding: 10px;")
#         instructions.setText(
#             """1. Getting Started:\n   • Click the green 'Start' button to activate NOVA\n   • The system indicator will turn green when active\n   • Watch the center circle animate to confirm activation\n\n2. Navigation:\n   • ⚙ (Settings): Configure system preferences\n   • ℹ (Info): View this help guide\n   • ✉ (Email): Open Gmail compose window\n\n3. Status Indicators:\n   • Grey dot: System is inactive\n   • Green dot: System is active and running\n   • Time display: Shows current system time\n\n4. Email Function:\n   • Click the email icon to open Gmail\n   • A new compose window will open\n   • The default recipient will be pre-filled\n\n5. System States:\n   • Inactive: Default state on startup\n   • Active: System running with animations\n   • Processing: Shown by circle animation\n\n6. Tips:\n   • Keep the window open to maintain activation\n   • Check the status indicator for system state\n   • Use the email function for quick communication"""
#         )
#         layout.addWidget(instructions)

#         close_btn = QPushButton("Close")
#         close_btn.setStyleSheet("background-color: #28a745; color: white;")
#         close_btn.clicked.connect(self.close)
#         layout.addWidget(close_btn)

#         self.setLayout(layout)

# class JarvisGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("NOVA ONLINE")
#         self.setFixedSize(800, 600)
#         self.setStyleSheet("background-color: black; color: white;")

#         self.recipient_email = "example@gmail.com"
#         self.engine = pyttsx3.init()
#         self.animation_running = False

#         self.setup_ui()
#         self.update_time()

#     def setup_ui(self):
#         main_layout = QVBoxLayout()

#         # Time and Status Bar
#         top_layout = QHBoxLayout()
#         self.time_label = QLabel()
#         self.time_label.setFont(QFont("Arial", 14))
#         top_layout.addWidget(self.time_label)

#         self.status_indicator = QLabel()
#         self.status_indicator.setFixedSize(10, 10)
#         self.update_status_indicator("grey")
#         top_layout.addWidget(self.status_indicator)

#         self.status_label = QLabel("System Inactive")
#         top_layout.addWidget(self.status_label)

#         # Icons
#         icons_layout = QHBoxLayout()
#         self.info_btn = QPushButton("ℹ")
#         self.info_btn.clicked.connect(self.show_info)
#         icons_layout.addWidget(self.info_btn)

#         self.email_btn = QPushButton("✉")
#         self.email_btn.clicked.connect(self.open_gmail_compose)
#         icons_layout.addWidget(self.email_btn)

#         top_layout.addLayout(icons_layout)
#         main_layout.addLayout(top_layout)

#         # Animation
#         self.animation_label = QLabel()
#         self.gif_path = r"D:\Material_gui_jarvis\logo.gif"
#         if os.path.exists(self.gif_path):
#             self.movie = QMovie(self.gif_path)
#             self.animation_label.setMovie(self.movie)
#         main_layout.addWidget(self.animation_label, alignment=Qt.AlignmentFlag.AlignCenter)

#         # Start Button
#         self.start_btn = QPushButton("Start")
#         self.start_btn.setFont(QFont("Arial", 14))
#         self.start_btn.setStyleSheet("background-color: #28a745; color: white;")
#         self.start_btn.clicked.connect(self.start_system)
#         main_layout.addWidget(self.start_btn)

#         self.setLayout(main_layout)

#     def update_status_indicator(self, color):
#         self.status_indicator.setStyleSheet(f"background-color: {color}; border-radius: 5px;")

#     def update_time(self):
#         current_time = datetime.now().strftime("%I:%M %p")
#         self.time_label.setText(current_time)
#         QTimer.singleShot(1000, self.update_time)

#     def show_info(self):
#         dialog = InfoDialog(self)
#         dialog.exec()

#     def speak(self, text):
#         self.engine.say(text)
#         self.engine.runAndWait()

#     def start_system(self):
#         sentences = [
#             "Initializing the cloud...",
#             "Starting all systems applications",
#             "Checking all drivers",
#             "Calibrating core processors",
#             "Checking the internet connection",
#             "Updating cloud configuration",
#             "All systems are now activated."
#         ]

#         def speak_thread():
#             for sentence in sentences:
#                 self.speak(sentence)

#         threading.Thread(target=speak_thread, daemon=True).start()
#         self.update_status_indicator("#28a745")
#         self.status_label.setText("System Activated")

#         if not self.animation_running and hasattr(self, 'movie'):
#             self.animation_running = True
#             self.movie.start()

#     def open_gmail_compose(self):
#         gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(self.recipient_email)}"
#         webbrowser.open(gmail_url)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = JarvisGUI()
#     window.show()
#     sys.exit(app.exec())


#____________________________ WORKING OF SPEAK FUNCTION & NAME CHANGED TO NOVA & CONVERTED TO PYQT6 AND DIFFERENT INFO AND MAIL BUTTON _____________________

# import sys
# import os
# import threading
# import urllib.parse
# import webbrowser
# from datetime import datetime
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QDialog,
#     QScrollArea, QFrame
# )
# from PyQt6.QtGui import QPixmap, QMovie, QFont, QIcon
# from PyQt6.QtCore import Qt, QTimer
# import pyttsx3

# class InfoDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("How to Use NOVA")
#         self.setFixedSize(400, 500)
#         self.setStyleSheet("background-color: #1e1e1e; color: white;")

#         layout = QVBoxLayout()
#         title = QLabel("NOVA User Guide")
#         title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title)

#         instructions = QTextEdit()
#         instructions.setReadOnly(True)
#         instructions.setStyleSheet("background-color: #2d2d2d; color: white; padding: 10px;")
#         instructions.setText(
#             """1. Getting Started:\n   • Click the green 'Start' button to activate NOVA\n   • The system indicator will turn green when active\n   • Watch the center circle animate to confirm activation\n\n2. Navigation:\n   • ⚙ (Settings): Configure system preferences\n   • ℹ (Info): View this help guide\n   • ✉ (Email): Open Gmail compose window\n\n3. Status Indicators:\n   • Grey dot: System is inactive\n   • Green dot: System is active and running\n   • Time display: Shows current system time\n\n4. Email Function:\n   • Click the email icon to open Gmail\n   • A new compose window will open\n   • The default recipient will be pre-filled\n\n5. System States:\n   • Inactive: Default state on startup\n   • Active: System running with animations\n   • Processing: Shown by circle animation\n\n6. Tips:\n   • Keep the window open to maintain activation\n   • Check the status indicator for system state\n   • Use the email function for quick communication"""
#         )
#         layout.addWidget(instructions)

#         close_btn = QPushButton("Close")
#         close_btn.setStyleSheet("background-color: #28a745; color: white;")
#         close_btn.clicked.connect(self.close)
#         layout.addWidget(close_btn)

#         self.setLayout(layout)

# class JarvisGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("NOVA ONLINE")
#         self.setFixedSize(800, 600)
#         self.setStyleSheet("background-color: black; color: white;")

#         self.recipient_email = "example@gmail.com"
#         self.engine = pyttsx3.init()
#         self.animation_running = False

#         self.setup_ui()
#         self.update_time()

#     def setup_ui(self):
#         main_layout = QVBoxLayout()

#         # Time and Status Bar
#         top_layout = QHBoxLayout()
#         self.time_label = QLabel()
#         self.time_label.setFont(QFont("Arial", 14))
#         self.time_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
#         top_layout.addWidget(self.time_label)

#         self.status_indicator = QLabel()
#         self.status_indicator.setFixedSize(15, 15)  # Match Tkinter size
#         self.update_status_indicator("grey")
#         top_layout.addWidget(self.status_indicator)

#         self.status_label = QLabel("System Inactive")
#         top_layout.addWidget(self.status_label)

#         # Icons
#         icons_layout = QHBoxLayout()
#         icon_size = 40  # Match Tkinter size
#         self.info_btn = QPushButton()
#         self.info_btn.setIcon(QIcon.fromTheme("dialog-information"))
#         self.info_btn.setIconSize(QPixmap(40, 40).size())
#         self.info_btn.setFixedSize(icon_size, icon_size)
#         self.info_btn.clicked.connect(self.show_info)
#         icons_layout.addWidget(self.info_btn)

#         self.email_btn = QPushButton()
#         self.email_btn.setIcon(QIcon.fromTheme("mail-send"))
#         self.email_btn.setIconSize(QPixmap(40, 40).size())
#         self.email_btn.setFixedSize(icon_size, icon_size)
#         self.email_btn.clicked.connect(self.open_gmail_compose)
#         icons_layout.addWidget(self.email_btn)

#         top_layout.addLayout(icons_layout)
#         main_layout.addLayout(top_layout)

#         # Animation
#         self.animation_label = QLabel()
#         self.gif_path = r"D:\Material_gui_jarvis\logo.gif"
#         if os.path.exists(self.gif_path):
#             self.movie = QMovie(self.gif_path)
#             self.animation_label.setMovie(self.movie)
#         main_layout.addWidget(self.animation_label, alignment=Qt.AlignmentFlag.AlignCenter)

#         # Start Button
#         self.start_btn = QPushButton("Start")
#         self.start_btn.setFont(QFont("Arial", 14))
#         self.start_btn.setFixedSize(120, 50)
#         self.start_btn.setStyleSheet("background-color: #28a745; color: white;")
#         self.start_btn.clicked.connect(self.start_system)
#         main_layout.addWidget(self.start_btn, alignment=Qt.AlignmentFlag.AlignCenter)

#         self.setLayout(main_layout)

#     def update_status_indicator(self, color):
#         self.status_indicator.setStyleSheet(f"background-color: {color}; border-radius: 7px;")

#     def update_time(self):
#         current_time = datetime.now().strftime("%I:%M %p")
#         self.time_label.setText(current_time)
#         QTimer.singleShot(1000, self.update_time)

#     def show_info(self):
#         dialog = InfoDialog(self)
#         dialog.exec()

#     def speak(self, text):
#         self.engine.say(text)
#         self.engine.runAndWait()

#     def start_system(self):
#         sentences = [
#             "Initializing the cloud...",
#             "Starting all systems applications",
#             "Checking all drivers",
#             "Calibrating core processors",
#             "Checking the internet connection",
#             "Updating cloud configuration",
#             "All systems are now activated."
#         ]

#         def speak_thread():
#             for sentence in sentences:
#                 self.speak(sentence)

#         threading.Thread(target=speak_thread, daemon=True).start()
#         self.update_status_indicator("#28a745")
#         self.status_label.setText("System Activated")

#         if not self.animation_running and hasattr(self, 'movie'):
#             self.animation_running = True
#             self.movie.start()

#     def open_gmail_compose(self):
#         gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(self.recipient_email)}"
#         webbrowser.open(gmail_url)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = JarvisGUI()
#     window.show()
#     sys.exit(app.exec())


#____________________________ WORKING OF SPEAK FUNCTION & NAME CHANGED TO NOVA & CONVERTED TO PYQT6 DIFFERENT BUTTON AND GLOW EFFECT AND BLACK GREEN COLOR_____________________


# import sys
# import os
# import threading
# import urllib.parse
# import webbrowser
# from datetime import datetime
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QDialog,
#     QScrollArea, QFrame
# )
# from PyQt6.QtGui import QPixmap, QMovie, QFont
# from PyQt6.QtCore import Qt, QTimer
# import pyttsx3

# class InfoDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("How to Use NOVA")
#         self.setFixedSize(400, 500)
#         self.setStyleSheet("background-color: #1e1e1e; color: white;")

#         layout = QVBoxLayout()
#         title = QLabel("NOVA User Guide")
#         title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title)

#         instructions = QTextEdit()
#         instructions.setReadOnly(True)
#         instructions.setStyleSheet("background-color: #2d2d2d; color: white; padding: 10px;")
#         instructions.setText(
#             """1. Getting Started:\n   • Click the green 'Start' button to activate NOVA\n   • The system indicator will turn green when active\n   • Watch the center circle animate to confirm activation\n\n2. Navigation:\n   • ⚙ (Settings): Configure system preferences\n   • ℹ (Info): View this help guide\n   • ✉ (Email): Open Gmail compose window\n\n3. Status Indicators:\n   • Grey dot: System is inactive\n   • Green dot: System is active and running\n   • Time display: Shows current system time\n\n4. Email Function:\n   • Click the email icon to open Gmail\n   • A new compose window will open\n   • The default recipient will be pre-filled\n\n5. System States:\n   • Inactive: Default state on startup\n   • Active: System running with animations\n   • Processing: Shown by circle animation\n\n6. Tips:\n   • Keep the window open to maintain activation\n   • Check the status indicator for system state\n   • Use the email function for quick communication"""
#         )
#         layout.addWidget(instructions)

#         close_btn = QPushButton("Close")
#         close_btn.setStyleSheet("background-color: #28a745; color: white;")
#         close_btn.clicked.connect(self.close)
#         layout.addWidget(close_btn)

#         self.setLayout(layout)

# class JarvisGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("NOVA ONLINE")
#         self.setFixedSize(800, 600)
#         self.setStyleSheet("background-color: black; color: white;")

#         self.recipient_email = "example@gmail.com"
#         self.engine = pyttsx3.init()
#         self.animation_running = False

#         self.setup_ui()
#         self.update_time()

#     def setup_ui(self):
#         main_layout = QVBoxLayout()

#         # Time and Status Bar
#         top_layout = QHBoxLayout()
#         self.time_label = QLabel()
#         self.time_label.setFont(QFont("Arial", 14))
#         top_layout.addWidget(self.time_label)

#         self.status_indicator = QLabel()
#         self.status_indicator.setFixedSize(10, 10)
#         self.update_status_indicator("grey")
#         top_layout.addWidget(self.status_indicator)

#         self.status_label = QLabel("System Inactive")
#         top_layout.addWidget(self.status_label)

#         # Icons
#         icons_layout = QHBoxLayout()
#         button_style = "background-color: #28a745; color: white; font-size: 16px; padding: 10px; border-radius: 5px;"
#         self.info_btn = QPushButton("ℹ")
#         self.info_btn.setFixedSize(40, 40)
#         self.info_btn.setStyleSheet(button_style)
#         self.info_btn.clicked.connect(self.show_info)
#         icons_layout.addWidget(self.info_btn)

#         self.email_btn = QPushButton("✉")
#         self.email_btn.setFixedSize(40, 40)
#         self.email_btn.setStyleSheet(button_style)
#         self.email_btn.clicked.connect(self.open_gmail_compose)
#         icons_layout.addWidget(self.email_btn)

#         top_layout.addLayout(icons_layout)
#         main_layout.addLayout(top_layout)

#         # Animation
#         self.animation_label = QLabel()
#         self.gif_path = r"D:\Material_gui_jarvis\logo.gif"
#         if os.path.exists(self.gif_path):
#             self.movie = QMovie(self.gif_path)
#             self.animation_label.setMovie(self.movie)
#         main_layout.addWidget(self.animation_label, alignment=Qt.AlignmentFlag.AlignCenter)

#         # Start Button
#         self.start_btn = QPushButton("Start")
#         self.start_btn.setFont(QFont("Arial", 14))
#         self.start_btn.setStyleSheet("background-color: #28a745; color: white;")
#         self.start_btn.clicked.connect(self.start_system)
#         main_layout.addWidget(self.start_btn)

#         self.setLayout(main_layout)

#     def update_status_indicator(self, color):
#         self.status_indicator.setStyleSheet(f"background-color: {color}; border-radius: 5px;")

#     def update_time(self):
#         current_time = datetime.now().strftime("%I:%M %p")
#         self.time_label.setText(current_time)
#         QTimer.singleShot(1000, self.update_time)

#     def show_info(self):
#         dialog = InfoDialog(self)
#         dialog.exec()

#     def speak(self, text):
#         self.engine.say(text)
#         self.engine.runAndWait()

#     def start_system(self):
#         sentences = [
#             "Initializing the cloud...",
#             "Starting all systems applications",
#             "Checking all drivers",
#             "Calibrating core processors",
#             "Checking the internet connection",
#             "Updating cloud configuration",
#             "All systems are now activated."
#         ]

#         def speak_thread():
#             for sentence in sentences:
#                 self.speak(sentence)

#         threading.Thread(target=speak_thread, daemon=True).start()
#         self.update_status_indicator("#28a745")
#         self.status_label.setText("System Activated")

#         if not self.animation_running and hasattr(self, 'movie'):
#             self.animation_running = True
#             self.movie.start()

#     def open_gmail_compose(self):
#         gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(self.recipient_email)}"
#         webbrowser.open(gmail_url)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = JarvisGUI()
#     window.show()
#     sys.exit(app.exec())



# import sys
# import os                           # full screen with setting button
# import threading
# import urllib.parse
# import webbrowser
# from datetime import datetime
# from PyQt6.QtWidgets import (
#     QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QDialog,
#     QScrollArea, QFrame
# )
# from PyQt6.QtGui import QPixmap, QMovie, QFont
# from PyQt6.QtCore import Qt, QTimer
# import pyttsx3

# class InfoDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("How to Use NOVA")
#         self.setFixedSize(400, 500)
#         self.setStyleSheet("background-color: #1e1e1e; color: white;")

#         layout = QVBoxLayout()
#         title = QLabel("NOVA User Guide")
#         title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
#         title.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(title)

#         instructions = QTextEdit()
#         instructions.setReadOnly(True)
#         instructions.setStyleSheet("background-color: #2d2d2d; color: white; padding: 10px;")
#         instructions.setText(
#             """1. Getting Started:\n   • Click the green 'Start' button to activate NOVA\n   • The system indicator will turn green when active\n   • Watch the center circle animate to confirm activation\n\n2. Navigation:\n   • ⚙ (Settings): Configure system preferences\n   • ℹ (Info): View this help guide\n   • ✉ (Email): Open Gmail compose window\n\n3. Status Indicators:\n   • Grey dot: System is inactive\n   • Green dot: System is active and running\n   • Time display: Shows current system time\n\n4. Email Function:\n   • Click the email icon to open Gmail\n   • A new compose window will open\n   • The default recipient will be pre-filled\n\n5. System States:\n   • Inactive: Default state on startup\n   • Active: System running with animations\n   • Processing: Shown by circle animation\n\n6. Tips:\n   • Keep the window open to maintain activation\n   • Check the status indicator for system state\n   • Use the email function for quick communication"""
#         )
#         layout.addWidget(instructions)

#         close_btn = QPushButton("Close")
#         close_btn.setStyleSheet("background-color: #28a745; color: white;")
#         close_btn.clicked.connect(self.close)
#         layout.addWidget(close_btn)

#         self.setLayout(layout)

# class JarvisGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("NOVA ONLINE")
#         self.showFullScreen()
#         self.setStyleSheet("background-color: black; color: white;")

#         self.recipient_email = "example@gmail.com"
#         self.engine = pyttsx3.init()
#         self.animation_running = False

#         self.setup_ui()
#         self.update_time()

#     def setup_ui(self):
#         main_layout = QVBoxLayout()

#         # Time and Status Bar
#         top_layout = QHBoxLayout()
#         self.time_label = QLabel()
#         self.time_label.setFont(QFont("Arial", 14))
#         top_layout.addWidget(self.time_label)

#         self.status_indicator = QLabel()
#         self.status_indicator.setFixedSize(10, 10)
#         self.update_status_indicator("grey")
#         top_layout.addWidget(self.status_indicator)

#         self.status_label = QLabel("System Inactive")
#         top_layout.addWidget(self.status_label)

#         # Icons
#         icons_layout = QHBoxLayout()
#         button_style = "background-color: #28a745; color: white; font-size: 16px; padding: 10px; border-radius: 5px;"
#         self.info_btn = QPushButton("ℹ")
#         self.info_btn.setFixedSize(40, 40)
#         self.info_btn.setStyleSheet(button_style)
#         self.info_btn.clicked.connect(self.show_info)
#         icons_layout.addWidget(self.info_btn)

#         self.settings_btn = QPushButton("⚙")
#         self.settings_btn.setFixedSize(40, 40)
#         self.settings_btn.setStyleSheet(button_style)
#         self.settings_btn.clicked.connect(self.show_settings)
#         icons_layout.addWidget(self.settings_btn)

#         self.email_btn = QPushButton("✉")
#         self.email_btn.setFixedSize(40, 40)
#         self.email_btn.setStyleSheet(button_style)
#         self.email_btn.clicked.connect(self.open_gmail_compose)
#         icons_layout.addWidget(self.email_btn)

#         top_layout.addLayout(icons_layout)
#         main_layout.addLayout(top_layout)

#         # Animation
#         self.animation_label = QLabel()
#         self.gif_path = r"D:\\Material_gui_jarvis\\logo.gif"
#         if os.path.exists(self.gif_path):
#             self.movie = QMovie(self.gif_path)
#             self.animation_label.setMovie(self.movie)
#         main_layout.addWidget(self.animation_label, alignment=Qt.AlignmentFlag.AlignCenter)

#         # Start Button
#         self.start_btn = QPushButton("Start")
#         self.start_btn.setFont(QFont("Arial", 14))
#         self.start_btn.setStyleSheet("background-color: #28a745; color: white;")
#         self.start_btn.clicked.connect(self.start_system)
#         main_layout.addWidget(self.start_btn)

#         self.setLayout(main_layout)

#     def update_status_indicator(self, color):
#         self.status_indicator.setStyleSheet(f"background-color: {color}; border-radius: 5px;")

#     def update_time(self):
#         current_time = datetime.now().strftime("%I:%M %p")
#         self.time_label.setText(current_time)
#         QTimer.singleShot(1000, self.update_time)

#     def show_info(self):
#         dialog = InfoDialog(self)
#         dialog.exec()
    
#     def show_settings(self):
#         settings_dialog = QDialog(self)
#         settings_dialog.setWindowTitle("Settings")
#         settings_dialog.setFixedSize(300, 200)
#         settings_dialog.setStyleSheet("background-color: #1e1e1e; color: white;")
#         layout = QVBoxLayout()
#         label = QLabel("Settings Menu (Placeholder)")
#         label.setFont(QFont("Arial", 12))
#         label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(label)
#         close_btn = QPushButton("Close")
#         close_btn.setStyleSheet("background-color: #28a745; color: white;")
#         close_btn.clicked.connect(settings_dialog.close)
#         layout.addWidget(close_btn)
#         settings_dialog.setLayout(layout)
#         settings_dialog.exec()

#     def speak(self, text):
#         self.engine.say(text)
#         self.engine.runAndWait()

#     def start_system(self):
#         sentences = [
#             "Initializing the cloud...",
#             "Starting all systems applications",
#             "Checking all drivers",
#             "Calibrating core processors",
#             "Checking the internet connection",
#             "Updating cloud configuration",
#             "All systems are now activated."
#         ]

#         def speak_thread():
#             for sentence in sentences:
#                 self.speak(sentence)

#         threading.Thread(target=speak_thread, daemon=True).start()
#         self.update_status_indicator("#28a745")
#         self.status_label.setText("System Activated")

#         if not self.animation_running and hasattr(self, 'movie'):
#             self.animation_running = True
#             self.movie.start()

#     def open_gmail_compose(self):
#         gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(self.recipient_email)}"
#         webbrowser.open(gmail_url)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = JarvisGUI()
#     window.show()
#     sys.exit(app.exec())


#______________________ final ____________________________________________

import sys
import os
import threading
import urllib.parse
import webbrowser
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QDialog,
    QScrollArea, QFrame
)
from PyQt6.QtGui import QPixmap, QMovie, QFont
from PyQt6.QtCore import Qt, QTimer
import pyttsx3

class InfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("How to Use NOVA")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        layout = QVBoxLayout()
        title = QLabel("NOVA User Guide")
        title.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)

        instructions = QTextEdit()
        instructions.setReadOnly(True)
        instructions.setStyleSheet("background-color: #2d2d2d; color: white; padding: 10px;")
        instructions.setText(
            """1. Getting Started:\n   • Click the green 'Start' button to activate NOVA\n   • The system indicator will turn green when active\n   • Watch the center circle animate to confirm activation\n\n2. Navigation:\n   • ⚙ (Settings): Configure system preferences\n   • ℹ (Info): View this help guide\n   • ✉ (Email): Open Gmail compose window\n\n3. Status Indicators:\n   • Grey dot: System is inactive\n   • Green dot: System is active and running\n   • Time display: Shows current system time\n\n4. Email Function:\n   • Click the email icon to open Gmail\n   • A new compose window will open\n   • The default recipient will be pre-filled\n\n5. System States:\n   • Inactive: Default state on startup\n   • Active: System running with animations\n   • Processing: Shown by circle animation\n\n6. Tips:\n   • Keep the window open to maintain activation\n   • Check the status indicator for system state\n   • Use the email function for quick communication"""
        )
        layout.addWidget(instructions)

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("background-color: #28a745; color: white;")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)

class JarvisGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NOVA ONLINE")
        self.resize(1000, 700)
        self.setStyleSheet("background-color: black; color: white;")

        self.recipient_email = "example@gmail.com"
        self.engine = pyttsx3.init()
        self.animation_running = False

        self.setup_ui()
        self.update_time()

    def setup_ui(self):
        main_layout = QVBoxLayout()

        # Time and Status Bar
        top_layout = QHBoxLayout()
        self.time_label = QLabel()
        self.time_label.setFont(QFont("Arial", 14))
        top_layout.addWidget(self.time_label)

        self.status_indicator = QLabel()
        self.status_indicator.setFixedSize(10, 10)
        self.update_status_indicator("grey")
        top_layout.addWidget(self.status_indicator)

        self.status_label = QLabel("System Inactive")
        top_layout.addWidget(self.status_label)

        # Icons
        icons_layout = QHBoxLayout()
        button_style = "background-color: #28a745; color: white; font-size: 16px; padding: 10px; border-radius: 5px;"
        self.info_btn = QPushButton("ℹ")
        self.info_btn.setFixedSize(40, 40)
        self.info_btn.setStyleSheet(button_style)
        self.info_btn.clicked.connect(self.show_info)
        icons_layout.addWidget(self.info_btn)

        self.settings_btn = QPushButton("⚙")
        self.settings_btn.setFixedSize(40, 40)
        self.settings_btn.setStyleSheet(button_style)
        self.settings_btn.clicked.connect(self.show_settings)
        icons_layout.addWidget(self.settings_btn)

        self.email_btn = QPushButton("✉")
        self.email_btn.setFixedSize(40, 40)
        self.email_btn.setStyleSheet(button_style)
        self.email_btn.clicked.connect(self.open_gmail_compose)
        icons_layout.addWidget(self.email_btn)

        top_layout.addLayout(icons_layout)
        main_layout.addLayout(top_layout)

        # Animation
        self.animation_label = QLabel()
        self.gif_path = r"D:\\Material_gui_jarvis\\logo.gif"
        if os.path.exists(self.gif_path):
            self.movie = QMovie(self.gif_path)
            self.animation_label.setMovie(self.movie)
        main_layout.addWidget(self.animation_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Start Button
        self.start_btn = QPushButton("Start")
        self.start_btn.setFont(QFont("Arial", 14))
        self.start_btn.setStyleSheet("background-color: #28a745; color: white;")
        self.start_btn.clicked.connect(self.start_system)
        main_layout.addWidget(self.start_btn)

        self.setLayout(main_layout)

    def update_status_indicator(self, color):
        self.status_indicator.setStyleSheet(f"background-color: {color}; border-radius: 5px;")

    def update_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        self.time_label.setText(current_time)
        QTimer.singleShot(1000, self.update_time)

    def show_info(self):
        dialog = InfoDialog(self)
        dialog.exec()
    
    def show_settings(self):
        settings_dialog = QDialog(self)
        settings_dialog.setWindowTitle("Settings")
        settings_dialog.setFixedSize(300, 200)
        settings_dialog.setStyleSheet("background-color: #1e1e1e; color: white;")
        layout = QVBoxLayout()
        label = QLabel("Settings Menu (Placeholder)")
        label.setFont(QFont("Arial", 12))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("background-color: #28a745; color: white;")
        close_btn.clicked.connect(settings_dialog.close)
        layout.addWidget(close_btn)
        settings_dialog.setLayout(layout)
        settings_dialog.exec()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def start_system(self):
        sentences = [
            "Initializing the cloud...",
            "Starting all systems applications",
            "Checking all drivers",
            "Calibrating core processors",
            "Checking the internet connection",
            "Updating cloud configuration",
            "All systems are now activated."
        ]

        def speak_thread():
            for sentence in sentences:
                self.speak(sentence)

        threading.Thread(target=speak_thread, daemon=True).start()
        self.update_status_indicator("#28a745")
        self.status_label.setText("System Activated")

        if not self.animation_running and hasattr(self, 'movie'):
            self.animation_running = True
            self.movie.start()

    def open_gmail_compose(self):
        gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(self.recipient_email)}"
        webbrowser.open(gmail_url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisGUI()
    window.show()
    sys.exit(app.exec())
