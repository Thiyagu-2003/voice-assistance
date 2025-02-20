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




#____________________________ WORKING OF SPEAK FUNCTION_____________________

import tkinter as tk
from tkinter import ttk
import webbrowser
from datetime import datetime
from PIL import Image, ImageTk
import urllib.parse
import pyttsx3  # Import the pyttsx3 library for text-to-speech
import threading  # Import threading for concurrent speech and animation
import os

class InfoDialog:
    def __init__(self, parent):
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("How to Use JARVIS")
        self.dialog.configure(bg='#1e1e1e')

        dialog_width = 400
        dialog_height = 500
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        center_x = int(screen_width/2 - dialog_width/2)
        center_y = int(screen_height/2 - dialog_height/2)
        self.dialog.geometry(f'{dialog_width}x{dialog_height}+{center_x}+{center_y}')

        title_label = tk.Label(self.dialog, text="JARVIS User Guide", font=("Arial", 16, "bold"), bg='#1e1e1e', fg='white', pady=20)
        title_label.pack()

        instructions = """1. Getting Started:
   • Click the green 'Start' button to activate JARVIS
   • The system indicator will turn green when active

2. Navigation:
   • ⚙ (Settings): Configure system preferences
   • ℹ (Info): View this help guide
   • ✉ (Email): Open Gmail compose window

3. System States:
   • Inactive: Default state on startup
   • Active: System running with animations

4. Tips:
   • Keep the window open to maintain activation
   • Check the status indicator for system state
"""
        text_frame = tk.Frame(self.dialog, bg='#1e1e1e')
        text_frame.pack(fill='both', expand=True, padx=20, pady=10)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side='right', fill='y')

        text_widget = tk.Text(text_frame, wrap=tk.WORD, bg='#2d2d2d', fg='white', font=("Arial", 11), padx=10, pady=10, yscrollcommand=scrollbar.set)
        text_widget.pack(side='left', fill='both', expand=True)
        scrollbar.config(command=text_widget.yview)

        text_widget.insert('1.0', instructions)
        text_widget.config(state='disabled')

        close_btn = tk.Button(self.dialog, text="Close", font=("Arial", 12), bg='#28a745', fg='white', command=self.dialog.destroy, width=10, bd=0)
        close_btn.pack(pady=20)

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS ONLINE")
        self.root.configure(bg='black')

        window_width = 800
        window_height = 600
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.recipient_email = "example@gmail.com"

        self.main_frame = tk.Frame(root, bg='black')
        self.main_frame.pack(expand=True, fill='both')

        self.top_frame = tk.Frame(self.main_frame, bg='black')
        self.top_frame.pack(fill='x', padx=20, pady=10)

        self.time_label = tk.Label(self.top_frame, text="", font=("Arial", 14), bg='black', fg='white')
        self.time_label.pack(side='left')

        self.status_frame = tk.Frame(self.top_frame, bg='black')
        self.status_frame.pack(side='left', padx=20)

        self.status_indicator = tk.Canvas(self.status_frame, width=10, height=10, bg='black', highlightthickness=0)
        self.status_indicator.pack(side='left')
        self.status_indicator.create_oval(0, 0, 10, 10, fill='grey')

        self.status_label = tk.Label(self.status_frame, text="System Inactive", font=("Arial", 12), bg='black', fg='white')
        self.status_label.pack(side='left', padx=5)

        self.icons_frame = tk.Frame(self.top_frame, bg='black')
        self.icons_frame.pack(side='right')

        self.info_btn = tk.Button(self.icons_frame, text="ℹ", font=("Arial", 12), bg='black', fg='white', bd=0, command=self.show_info)
        self.info_btn.pack(side='left', padx=5)

        self.email_btn = tk.Button(self.icons_frame, text="✉", font=("Arial", 12), bg='black', fg='white', bd=0, command=self.open_gmail_compose)
        self.email_btn.pack(side='left', padx=5)

        self.circle_canvas = tk.Label(self.main_frame, bg='black')
        self.circle_canvas.pack(expand=True)

        self.start_btn = tk.Button(self.main_frame, text="Start", font=("Arial", 14), bg='#28a745', fg='white', width=10, command=self.start_system, bd=0)
        self.start_btn.pack(pady=20)

        # GIF Animation
        self.gif_path = r"D:\Material_gui_jarvis\logo.gif"  # Ensure this path is correct
        self.frames = []
        self.load_gif()
        self.current_frame = 0
        self.animation_running = False

        self.update_time()

        # Initialize text-to-speech engine
        self.engine = pyttsx3.init()

    def load_gif(self):
        try:
            if not os.path.exists(self.gif_path):
                print(f"Error: GIF not found at {self.gif_path}")
                return
            gif = Image.open(self.gif_path)
            for frame in range(gif.n_frames):
                gif.seek(frame)
                resized_frame = gif.resize((150, 150))
                self.frames.append(ImageTk.PhotoImage(resized_frame))
            if not self.frames:
                print("Warning: No frames loaded in GIF.")
        except Exception as e:
            print(f"Error loading GIF: {e}")

    def show_info(self):
        InfoDialog(self.root)

    def update_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)

    def speak(self, text):
        """ Function to make the system speak a sentence """
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

        self.status_indicator.delete("all")
        self.status_indicator.create_oval(0, 0, 10, 10, fill='#28a745')
        self.status_label.config(text="System Activated")

        if not self.animation_running:
            self.animation_running = True
            self.play_gif()

    def play_gif(self):
        if self.animation_running and self.frames:
            self.circle_canvas.config(image=self.frames[self.current_frame])
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.root.after(50, self.play_gif)

    def open_gmail_compose(self):
        gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(self.recipient_email)}"
        webbrowser.open(gmail_url)

def main():
    print("Starting JARVIS GUI...")  # Debugging line
    root = tk.Tk()
    app = JarvisGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
