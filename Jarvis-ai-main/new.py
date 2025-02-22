import sys
import os
import threading
import urllib.parse
import webbrowser
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QDialog
)
from PyQt6.QtGui import QMovie, QFont
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
            "1. Getting Started:\n   • Click the green 'Start' button to activate NOVA\n   • The system indicator will turn green when active\n   • Watch the center circle animate to confirm activation\n\n2. Navigation:\n   • ⚙ (Settings): Configure system preferences\n   • ℹ (Info): View this help guide\n   • ✉ (Email): Open Gmail compose window\n\n3. Status Indicators:\n   • Grey dot: System is inactive\n   • Green dot: System is active and running\n   • Time display: Shows current system time\n\n4. Email Function:\n   • Click the email icon to open Gmail\n   • A new compose window will open\n   • The default recipient will be pre-filled\n\n5. System States:\n   • Inactive: Default state on startup\n   • Active: System running with animations\n   • Processing: Shown by circle animation\n\n6. Tips:\n   • Keep the window open to maintain activation\n   • Check the status indicator for system state\n   • Use the email function for quick communication"
        )
        layout.addWidget(instructions)

        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("background-color: #28a745; color: white;")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)

        self.setLayout(layout)

class Desktop1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NOVA ONLINE")
        self.setFixedSize(800, 600)
        self.setStyleSheet("background-color: black; color: white;")

        self.recipient_email = "example@gmail.com"
        self.engine = pyttsx3.init()
        self.animation_running = False

        self.setup_ui()
        self.update_time()

    def setup_ui(self):
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        self.time_label = QLabel()
        self.time_label.setFont(QFont("Arial", 14))
        top_layout.addWidget(self.time_label)

        self.status_label = QLabel("System Inactive")
        top_layout.addWidget(self.status_label)

        self.animation_label = QLabel()
        self.gif_path = r"D:/Material_gui_jarvis/logo.gif"
        if os.path.exists(self.gif_path):
            self.movie = QMovie(self.gif_path)
            self.animation_label.setMovie(self.movie)
        layout.addWidget(self.animation_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.start_btn = QPushButton("Start")
        self.start_btn.setFont(QFont("Arial", 14))
        self.start_btn.setStyleSheet("background-color: #28a745; color: white;")
        self.start_btn.clicked.connect(self.start_system)
        layout.addWidget(self.start_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def update_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        self.time_label.setText(current_time)
        QTimer.singleShot(1000, self.update_time)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def start_system(self):
        sentences = [
            "Initializing the cloud...",
            "Starting all systems applications...",
            "Checking all drivers...",
            "Calibrating core processors...",
            "Checking the internet connection...",
            "Updating cloud configuration...",
            "All systems are now activated."
        ]

        def speak_thread():
            for sentence in sentences:
                self.speak(sentence)
            self.launch_desktop_2()

        threading.Thread(target=speak_thread, daemon=True).start()
        self.status_label.setText("System Activated")
        if not self.animation_running and hasattr(self, 'movie'):
            self.animation_running = True
            self.movie.start()

    # def launch_desktop_2(self):
    #     desktop_2_path = os.path.abspath(r"D:\FINAL_YEAR_PROJECT\voice-assistance\Jarvis-ai-main\desktop_2.py")  # Replace with the actual file path
    #     os.system(f'python "{desktop_2_path}"')  # Launch using file path
    #     self.close()

    

    def launch_desktop_2(self):
        import subprocess
        desktop_2_path = os.path.abspath(r"D:\FINAL_YEAR_PROJECT\voice-assistance\Jarvis-ai-main\desktop_2.py")  # Replace with the actual file path
        subprocess.Popen([sys.executable, desktop_2_path])  # Launch using subprocess
        self.close()  # Close desktop_1.py immediately


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Desktop1()
    window.show()
    sys.exit(app.exec())
