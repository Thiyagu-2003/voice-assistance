# # google search,can be moved any where on the screen, always on top 
# import sys
# import webbrowser
# from PyQt6.QtWidgets import (QApplication, QWidget, QFrame, QPushButton, QLabel, 
#                             QTextBrowser, QCheckBox, QLineEdit, QTextEdit, QPlainTextEdit)
# from PyQt6.QtCore import Qt, QRect, QPoint
# from PyQt6.QtGui import QPixmap, QMovie

# class JarvisOverlayGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()
#         self.initDragFunctionality()
#         self.setup_gifs()

#     def setupUi(self):
#         # Main window setup
#         self.setObjectName("JarvisOverlayGUI")
#         self.setGeometry(0, 0, 575, 626)
#         self.setWindowTitle("JarvisOverlayGUI")
#         self.setStyleSheet("background-color: rgb(0, 0, 0);")
        
#         # Set window flags for frameless window and always on top
#         self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

#         # Full settings outer frame
#         self.full_setting_outer_frame = QFrame(self)
#         self.full_setting_outer_frame.setGeometry(QRect(190, 0, 381, 231))
#         self.full_setting_outer_frame.setStyleSheet("""
#             background-color: rgb(0, 0, 0);
#             border-color: rgb(255,255,255);
#             border-width: 2px;
#             border-style: solid;
#         """)
#         self.full_setting_outer_frame.setFrameShape(QFrame.Shape.StyledPanel)
#         self.full_setting_outer_frame.setFrameShadow(QFrame.Shadow.Raised)

#         # Voice Assistant Label
#         self.voise_assistant_label = QLabel(self.full_setting_outer_frame)
#         self.voise_assistant_label.setGeometry(QRect(0, 0, 291, 41))
#         self.voise_assistant_label.setPixmap(QPixmap("D:/Downloads/Frame 2.png"))
#         self.voise_assistant_label.setScaledContents(True)

#         # Exit Button
#         self.Exit_Button = QPushButton(self.full_setting_outer_frame)
#         self.Exit_Button.setGeometry(QRect(330, 0, 51, 41))
#         self.Exit_Button.setStyleSheet("font: 20pt \"Segoe UI\";")
#         self.Exit_Button.setText("X")
#         self.Exit_Button.clicked.connect(self.close)

#         # Minimize Button
#         self.Minimize_Button = QPushButton(self.full_setting_outer_frame)
#         self.Minimize_Button.setGeometry(QRect(290, 0, 41, 41))
#         self.Minimize_Button.setStyleSheet("font: 30pt \"Segoe UI\";")
#         self.Minimize_Button.setText("-")
#         self.Minimize_Button.clicked.connect(self.showMinimized)

#         # Settings Frame
#         self.settings_frame = QFrame(self.full_setting_outer_frame)
#         self.settings_frame.setGeometry(QRect(0, 40, 381, 191))
#         self.settings_frame.setFrameShape(QFrame.Shape.StyledPanel)
#         self.settings_frame.setFrameShadow(QFrame.Shadow.Raised)

#         # Settings Text Browser
#         self.only_settings_bar = QTextBrowser(self.settings_frame)
#         self.only_settings_bar.setGeometry(QRect(0, 0, 101, 31))
#         self.only_settings_bar.setStyleSheet("""
#             color: rgb(255,255,255);
#             background-color: transparent;
#             border-width: 0pt;
#         """)
#         self.only_settings_bar.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.only_settings_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.only_settings_bar.setHtml("""
#             <html><head><style>
#             p { margin: 0; }
#             </style></head><body>
#             <p style="font-size:16pt; font-weight:700;"> Settings</p>
#             </body></html>
#         """)

#         # Checkboxes
#         self.show_status = QCheckBox("Show Status Icon", self.settings_frame)
#         self.show_status.setGeometry(QRect(10, 40, 141, 22))
#         self.show_status.setStyleSheet("""
#             font: 11pt "Segoe UI";
#             color: rgb(255,255,255);
#             background-color: transparent;
#             border-width: 0pt;
#         """)

#         self.show_terminal = QCheckBox("Show Terminal", self.settings_frame)
#         self.show_terminal.setGeometry(QRect(200, 40, 131, 22))
#         self.show_terminal.setStyleSheet(self.show_status.styleSheet())
#         self.show_terminal.setChecked(True)  # Default to checked
#         self.show_terminal.stateChanged.connect(self.toggle_terminal_visibility)

#         self.custom_search = QCheckBox("Custom Search", self.settings_frame)
#         self.custom_search.setGeometry(QRect(10, 90, 131, 22))
#         self.custom_search.setStyleSheet(self.show_status.styleSheet())

#         self.mute_nova = QCheckBox("Mute Nova", self.settings_frame)
#         self.mute_nova.setGeometry(QRect(200, 90, 111, 22))
#         self.mute_nova.setStyleSheet(self.show_status.styleSheet())

#         # NOVA Online Label
#         self.NOVA_ONLINE = QLabel(self)
#         self.NOVA_ONLINE.setGeometry(QRect(0, 10, 181, 81))
#         self.NOVA_ONLINE.setPixmap(QPixmap("D:/Material_gui_jarvis/NOVA.png"))
#         self.NOVA_ONLINE.setScaledContents(True)

#         # All GIF Labels
#         self.starting_gif = QLabel(self)
#         self.starting_gif.setGeometry(QRect(0, 100, 181, 171))
#         self.starting_gif.setPixmap(QPixmap("D:/Material_gui_jarvis/logo.gif"))
#         self.starting_gif.setScaledContents(True)

#         self.starting_gif_2 = QLabel(self)
#         self.starting_gif_2.setGeometry(QRect(0, 100, 181, 181))
#         self.starting_gif_2.setPixmap(QPixmap("D:/Material_gui_jarvis/path.gif"))
#         self.starting_gif_2.setScaledContents(True)

#         self.starting_gif_3 = QLabel(self)
#         self.starting_gif_3.setGeometry(QRect(0, 90, 181, 171))
#         self.starting_gif_3.setPixmap(QPixmap("D:/Material_gui_jarvis/new.gif"))
#         self.starting_gif_3.setScaledContents(True)

#         self.voice_assistant_gif = QLabel(self)
#         self.voice_assistant_gif.setGeometry(QRect(0, 90, 181, 181))
#         self.voice_assistant_gif.setPixmap(QPixmap("D:/Downloads/voice assistant.gif.gif"))
#         self.voice_assistant_gif.setScaledContents(True)

#         # Search Frame
#         self.search = QFrame(self)
#         self.search.setGeometry(QRect(190, 230, 381, 51))
#         self.search.setStyleSheet("""
#             background-color: rgb(0,0,0);
#             border-color: rgb(255, 255, 255);
#             border-width: 1px;
#             border-style: solid;
#         """)
#         self.search.setFrameShape(QFrame.Shape.StyledPanel)
#         self.search.setFrameShadow(QFrame.Shadow.Raised)

#         # Search Box
#         self.search_box = QLineEdit(self.search)
#         self.search_box.setGeometry(QRect(0, 0, 291, 51))
#         self.search_box.setPlaceholderText(" Enter your query to search")

#         # Send Button
#         self.send_button = QPushButton("Send", self.search)
#         self.send_button.setGeometry(QRect(300, 10, 71, 31))
#         self.send_button.setStyleSheet("font: 20pt \"Segoe UI\";")
#         self.send_button.clicked.connect(self.perform_search)

#         # Nova Terminal Frame
#         self.nova_terminal_outerframe = QFrame(self)
#         self.nova_terminal_outerframe.setGeometry(QRect(0, 290, 571, 331))
#         self.nova_terminal_outerframe.setFrameShape(QFrame.Shape.StyledPanel)
#         self.nova_terminal_outerframe.setFrameShadow(QFrame.Shadow.Raised)

#         # Terminal Heading
#         self.nova_terminal_heading = QTextEdit(self.nova_terminal_outerframe)
#         self.nova_terminal_heading.setGeometry(QRect(0, 0, 571, 41))
#         self.nova_terminal_heading.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.nova_terminal_heading.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.nova_terminal_heading.setHtml("""
#             <html><head><style>
#             p { margin: 0; }
#             </style></head><body>
#             <p align="center" style="font-size:16pt;">NOVA TERMINAL</p>
#             </body></html>
#         """)
#         self.nova_terminal_heading.setReadOnly(True)

#         # Terminal Output
#         self.interaction_print_terminal = QPlainTextEdit(self.nova_terminal_outerframe)
#         self.interaction_print_terminal.setGeometry(QRect(0, 40, 571, 291))
#         self.interaction_print_terminal.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
#         self.interaction_print_terminal.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.interaction_print_terminal.setReadOnly(True)

#     def toggle_terminal_visibility(self, state):
#         if state == Qt.CheckState.Unchecked:
#             # Hide terminal when unchecked
#             self.nova_terminal_outerframe.setGeometry(QRect(0, 290, 0, 0))
#             # Resize the main window
#             self.setGeometry(0, 0, 575, 290)
#         else:
#             # Show terminal when checked
#             self.nova_terminal_outerframe.setGeometry(QRect(0, 290, 571, 331))
#             # Restore full window size
#             self.setGeometry(0, 0, 575, 626)

#     def setup_gifs(self):
#         # Setup actual GIF animations
#         gifs = [
#             ("D:/Material_gui_jarvis/logo.gif", self.starting_gif),
#             ("D:/Material_gui_jarvis/path.gif", self.starting_gif_2),
#             ("D:/Material_gui_jarvis/new.gif", self.starting_gif_3),
#             ("D:/Downloads/voice assistant.gif.gif", self.voice_assistant_gif)
#         ]
        
#         for gif_path, label in gifs:
#             movie = QMovie(gif_path)
#             label.setMovie(movie)
#             movie.start()

#     def initDragFunctionality(self):
#         # Enable moving the window by clicking and dragging
#         self.oldPos = self.pos()
#         self.setMouseTracking(True)

#     def mousePressEvent(self, event):
#         # Capture the initial mouse position when pressed
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.oldPos = event.globalPosition().toPoint()

#     def mouseMoveEvent(self, event):
#         # Move the window when mouse is dragged
#         if event.buttons() == Qt.MouseButton.LeftButton:
#             delta = event.globalPosition().toPoint() - self.oldPos
#             self.move(self.x() + delta.x(), self.y() + delta.y())
#             self.oldPos = event.globalPosition().toPoint()

#     def perform_search(self):
#         # Get search query from search box
#         query = self.search_box.text()
#         if query:
#             # Perform Google search
#             search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
#             webbrowser.open(search_url)
            
#             # Log search in terminal
#             self.interaction_print_terminal.appendPlainText(f"Searching Google for: {query}")
            
#             # Clear search box after search
#             self.search_box.clear()

# def main():
#     app = QApplication(sys.argv)
#     window = JarvisOverlayGUI()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()

#++++++++++++++++++++++++++++++++++++++++++++_____________________________________________________________________

# import sys              #3 checkbox will be ticked automatically
# import webbrowser
# from PyQt6.QtWidgets import (QApplication, QWidget, QFrame, QPushButton, QLabel, 
#                             QTextBrowser, QCheckBox, QLineEdit, QTextEdit, QPlainTextEdit)
# from PyQt6.QtCore import Qt, QRect, QPoint
# from PyQt6.QtGui import QPixmap, QMovie

# class JarvisOverlayGUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()
#         self.initDragFunctionality()
#         self.setup_gifs()

#     def setupUi(self):
#         # Main window setup
#         self.setObjectName("JarvisOverlayGUI")
#         self.setGeometry(0, 0, 575, 626)
#         self.setWindowTitle("JarvisOverlayGUI")
#         self.setStyleSheet("background-color: rgb(0, 0, 0);")
        
#         # Set window flags for frameless window and always on top
#         self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

#         # Full settings outer frame
#         self.full_setting_outer_frame = QFrame(self)
#         self.full_setting_outer_frame.setGeometry(QRect(190, 0, 381, 231))
#         self.full_setting_outer_frame.setStyleSheet("""
#             background-color: rgb(0, 0, 0);
#             border-color: rgb(255,255,255);
#             border-width: 2px;
#             border-style: solid;
#         """)
#         self.full_setting_outer_frame.setFrameShape(QFrame.Shape.StyledPanel)
#         self.full_setting_outer_frame.setFrameShadow(QFrame.Shadow.Raised)

#         # Voice Assistant Label
#         self.voise_assistant_label = QLabel(self.full_setting_outer_frame)
#         self.voise_assistant_label.setGeometry(QRect(0, 0, 291, 41))
#         self.voise_assistant_label.setPixmap(QPixmap("D:/Downloads/Frame 2.png"))
#         self.voise_assistant_label.setScaledContents(True)

#         # Exit Button
#         self.Exit_Button = QPushButton(self.full_setting_outer_frame)
#         self.Exit_Button.setGeometry(QRect(330, 0, 51, 41))
#         self.Exit_Button.setStyleSheet("font: 20pt \"Segoe UI\";")
#         self.Exit_Button.setText("X")
#         self.Exit_Button.clicked.connect(self.close)

#         # Minimize Button
#         self.Minimize_Button = QPushButton(self.full_setting_outer_frame)
#         self.Minimize_Button.setGeometry(QRect(290, 0, 41, 41))
#         self.Minimize_Button.setStyleSheet("font: 30pt \"Segoe UI\";")
#         self.Minimize_Button.setText("-")
#         self.Minimize_Button.clicked.connect(self.showMinimized)

#         # Settings Frame
#         self.settings_frame = QFrame(self.full_setting_outer_frame)
#         self.settings_frame.setGeometry(QRect(0, 40, 381, 191))
#         self.settings_frame.setFrameShape(QFrame.Shape.StyledPanel)
#         self.settings_frame.setFrameShadow(QFrame.Shadow.Raised)

#         # Settings Text Browser
#         self.only_settings_bar = QTextBrowser(self.settings_frame)
#         self.only_settings_bar.setGeometry(QRect(0, 0, 101, 31))
#         self.only_settings_bar.setStyleSheet("""
#             color: rgb(255,255,255);
#             background-color: transparent;
#             border-width: 0pt;
#         """)
#         self.only_settings_bar.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.only_settings_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.only_settings_bar.setHtml("""
#             <html><head><style>
#             p { margin: 0; }
#             </style></head><body>
#             <p style="font-size:16pt; font-weight:700;"> Settings</p>
#             </body></html>
#         """)

#         # Checkboxes
#         self.show_status = QCheckBox("Show Status Icon", self.settings_frame)
#         self.show_status.setGeometry(QRect(10, 40, 141, 22))
#         self.show_status.setStyleSheet("""
#             font: 11pt "Segoe UI";
#             color: rgb(255,255,255);
#             background-color: transparent;
#             border-width: 0pt;
#         """)
#         self.show_status.setChecked(True)

#         self.show_terminal = QCheckBox("Show Terminal", self.settings_frame)
#         self.show_terminal.setGeometry(QRect(200, 40, 131, 22))
#         self.show_terminal.setStyleSheet(self.show_status.styleSheet())
#         self.show_terminal.setChecked(True)
#         self.show_terminal.stateChanged.connect(self.toggle_terminal_visibility)

#         self.custom_search = QCheckBox("Custom Search", self.settings_frame)
#         self.custom_search.setGeometry(QRect(10, 90, 131, 22))
#         self.custom_search.setStyleSheet(self.show_status.styleSheet())
#         self.custom_search.setChecked(True)

#         self.mute_nova = QCheckBox("Mute Nova", self.settings_frame)
#         self.mute_nova.setGeometry(QRect(200, 90, 111, 22))
#         self.mute_nova.setStyleSheet(self.show_status.styleSheet())

#         # NOVA Online Label
#         self.NOVA_ONLINE = QLabel(self)
#         self.NOVA_ONLINE.setGeometry(QRect(0, 10, 181, 81))
#         self.NOVA_ONLINE.setPixmap(QPixmap("D:/Material_gui_jarvis/NOVA.png"))
#         self.NOVA_ONLINE.setScaledContents(True)

#         # All GIF Labels
#         self.starting_gif = QLabel(self)
#         self.starting_gif.setGeometry(QRect(0, 100, 181, 171))
#         self.starting_gif.setPixmap(QPixmap("D:/Material_gui_jarvis/logo.gif"))
#         self.starting_gif.setScaledContents(True)

#         self.starting_gif_2 = QLabel(self)
#         self.starting_gif_2.setGeometry(QRect(0, 100, 181, 181))
#         self.starting_gif_2.setPixmap(QPixmap("D:/Material_gui_jarvis/path.gif"))
#         self.starting_gif_2.setScaledContents(True)

#         self.starting_gif_3 = QLabel(self)
#         self.starting_gif_3.setGeometry(QRect(0, 90, 181, 171))
#         self.starting_gif_3.setPixmap(QPixmap("D:/Material_gui_jarvis/new.gif"))
#         self.starting_gif_3.setScaledContents(True)

#         self.voice_assistant_gif = QLabel(self)
#         self.voice_assistant_gif.setGeometry(QRect(0, 90, 181, 181))
#         self.voice_assistant_gif.setPixmap(QPixmap("D:/Downloads/voice assistant.gif.gif"))
#         self.voice_assistant_gif.setScaledContents(True)

#         # Search Frame
#         self.search = QFrame(self)
#         self.search.setGeometry(QRect(190, 230, 381, 51))
#         self.search.setStyleSheet("""
#             background-color: rgb(0,0,0);
#             border-color: rgb(255, 255, 255);
#             border-width: 1px;
#             border-style: solid;
#         """)
#         self.search.setFrameShape(QFrame.Shape.StyledPanel)
#         self.search.setFrameShadow(QFrame.Shadow.Raised)

#         # Search Box
#         self.search_box = QLineEdit(self.search)
#         self.search_box.setGeometry(QRect(0, 0, 291, 51))
#         self.search_box.setPlaceholderText(" Enter your query to search")

#         # Send Button
#         self.send_button = QPushButton("Send", self.search)
#         self.send_button.setGeometry(QRect(300, 10, 71, 31))
#         self.send_button.setStyleSheet("font: 20pt \"Segoe UI\";")
#         self.send_button.clicked.connect(self.perform_search)

#         # Nova Terminal Frame
#         self.nova_terminal_outerframe = QFrame(self)
#         self.nova_terminal_outerframe.setGeometry(QRect(0, 290, 571, 331))
#         self.nova_terminal_outerframe.setFrameShape(QFrame.Shape.StyledPanel)
#         self.nova_terminal_outerframe.setFrameShadow(QFrame.Shadow.Raised)

#         # Terminal Heading
#         self.nova_terminal_heading = QTextEdit(self.nova_terminal_outerframe)
#         self.nova_terminal_heading.setGeometry(QRect(0, 0, 571, 41))
#         self.nova_terminal_heading.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.nova_terminal_heading.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.nova_terminal_heading.setHtml("""
#             <html><head><style>
#             p { margin: 0; }
#             </style></head><body>
#             <p align="center" style="font-size:16pt;">NOVA TERMINAL</p>
#             </body></html>
#         """)
#         self.nova_terminal_heading.setReadOnly(True)

#         # Terminal Output
#         self.interaction_print_terminal = QPlainTextEdit(self.nova_terminal_outerframe)
#         self.interaction_print_terminal.setGeometry(QRect(0, 40, 571, 291))
#         self.interaction_print_terminal.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
#         self.interaction_print_terminal.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.interaction_print_terminal.setReadOnly(True)

#     def toggle_terminal_visibility(self, state):
#         if state == Qt.CheckState.Unchecked:
#             # Hide terminal when unchecked
#             self.nova_terminal_outerframe.hide()
#             # Resize the main window precisely
#             self.resize(571, 291)
#         else:
#             # Show terminal when checked
#             self.nova_terminal_outerframe.show()
#             # Restore full window size
#             self.resize(575, 626)
   
#     def setup_gifs(self):
#         # Setup actual GIF animations
#         gifs = [
#             ("D:/Material_gui_jarvis/logo.gif", self.starting_gif),
#             ("D:/Material_gui_jarvis/path.gif", self.starting_gif_2),
#             ("D:/Material_gui_jarvis/new.gif", self.starting_gif_3),
#             ("D:/Downloads/voice assistant.gif.gif", self.voice_assistant_gif)
#         ]
        
#         for gif_path, label in gifs:
#             movie = QMovie(gif_path)
#             label.setMovie(movie)
#             movie.start()

#     def initDragFunctionality(self):
#         # Enable moving the window by clicking and dragging
#         self.oldPos = self.pos()
#         self.setMouseTracking(True)

#     def mousePressEvent(self, event):
#         # Capture the initial mouse position when pressed
#         if event.button() == Qt.MouseButton.LeftButton:
#             self.oldPos = event.globalPosition().toPoint()

#     def mouseMoveEvent(self, event):
#         # Move the window when mouse is dragged
#         if event.buttons() == Qt.MouseButton.LeftButton:
#             delta = event.globalPosition().toPoint() - self.oldPos
#             self.move(self.x() + delta.x(), self.y() + delta.y())
#             self.oldPos = event.globalPosition().toPoint()

#     def perform_search(self):
#         # Get search query from search box
#         query = self.search_box.text()
#         if query:
#             # Perform Google search
#             search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
#             webbrowser.open(search_url)
            
#             # Log search in terminal
#             self.interaction_print_terminal.appendPlainText(f"Searching Google for: {query}")
            
#             # Clear search box after search
#             self.search_box.clear()

# def main():
#     app = QApplication(sys.argv)
#     window = JarvisOverlayGUI()
#     window.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                            # with nova button
import sys
import webbrowser
from PyQt6.QtWidgets import (QApplication, QWidget, QFrame, QPushButton, QLabel, 
                             QTextBrowser, QCheckBox, QLineEdit, QTextEdit, QPlainTextEdit)
from PyQt6.QtCore import Qt, QRect, QEvent, QPoint
from PyQt6.QtGui import QPixmap, QMovie, QIcon

class JarvisOverlayGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.is_expanded = False
        self.setupUi()
        self.initDragFunctionality()
        self.setup_gifs()
        
    def setupUi(self):
        # Main window setup
        self.setObjectName("JarvisOverlayGUI")
        self.setGeometry(0, 0, 575, 626)
        self.setWindowTitle("JarvisOverlayGUI")
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        # Set window flags for frameless window and always on top
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        
        # NOVA Online Button (acts as the launcher for the full GUI)
        self.NOVA_ONLINE = QPushButton(self)
        self.NOVA_ONLINE.setGeometry(QRect(0, 10, 181, 81))
        self.NOVA_ONLINE.setStyleSheet("""
            QPushButton {
                border: none;
                background-color: transparent;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
        """)
        pixmap = QPixmap("D:/Material_gui_jarvis/NOVA.png")
        icon = QIcon(pixmap)
        self.NOVA_ONLINE.setIcon(icon)
        self.NOVA_ONLINE.setIconSize(pixmap.size())
        # Clicking the NOVA Online button toggles the full GUI
        self.NOVA_ONLINE.clicked.connect(self.toggle_gui)
        
        # Create a container for all other widgets (full GUI)
        self.main_container = QFrame(self)
        self.main_container.setGeometry(QRect(0, 0, 575, 626))
        
        # Full settings outer frame
        self.full_setting_outer_frame = QFrame(self.main_container)
        self.full_setting_outer_frame.setGeometry(QRect(190, 0, 381, 231))
        self.full_setting_outer_frame.setStyleSheet("""
            background-color: rgb(0, 0, 0);
            border-color: rgb(255,255,255);
            border-width: 2px;
            border-style: solid;
        """)
        self.full_setting_outer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.full_setting_outer_frame.setFrameShadow(QFrame.Shadow.Raised)
        
        # Voice Assistant Label
        self.voise_assistant_label = QLabel(self.full_setting_outer_frame)
        self.voise_assistant_label.setGeometry(QRect(0, 0, 291, 41))
        self.voise_assistant_label.setPixmap(QPixmap("D:/Downloads/Frame 2.png"))
        self.voise_assistant_label.setScaledContents(True)
        
        # Exit Button
        self.Exit_Button = QPushButton(self.full_setting_outer_frame)
        self.Exit_Button.setGeometry(QRect(330, 0, 51, 41))
        self.Exit_Button.setStyleSheet("""
            font: 20pt "Segoe UI";
            color: rgb(255, 255, 255);
        """)
        self.Exit_Button.setText("X")
        self.Exit_Button.clicked.connect(self.close)
        
        # Minimize Button (uses our custom minimize behavior)
        self.Minimize_Button = QPushButton(self.full_setting_outer_frame)
        self.Minimize_Button.setGeometry(QRect(290, 0, 41, 41))
        self.Minimize_Button.setStyleSheet("""
            font: 30pt "Segoe UI";
            color: rgb(255, 255, 255);
        """)
        self.Minimize_Button.setText("-")
        self.Minimize_Button.clicked.connect(self.minimize_gui)
        
        # Settings Frame
        self.settings_frame = QFrame(self.full_setting_outer_frame)
        self.settings_frame.setGeometry(QRect(0, 40, 381, 191))
        self.settings_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Shadow.Raised)
        
        # Settings Text Browser
        self.only_settings_bar = QTextBrowser(self.settings_frame)
        self.only_settings_bar.setGeometry(QRect(0, 0, 101, 31))
        self.only_settings_bar.setStyleSheet("""
            color: rgb(255,255,255);
            background-color: transparent;
            border-width: 0pt;
        """)
        self.only_settings_bar.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.only_settings_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.only_settings_bar.setHtml("""
            <html><head><style>
            p { margin: 0; }
            </style></head><body>
            <p style="font-size:16pt; font-weight:700;"> Settings</p>
            </body></html>
        """)
        
        # Checkboxes
        self.show_status = QCheckBox("Show Status Icon", self.settings_frame)
        self.show_status.setGeometry(QRect(10, 40, 141, 22))
        self.show_status.setStyleSheet("""
            font: 11pt "Segoe UI";
            color: rgb(255,255,255);
            background-color: transparent;
            border-width: 0pt;
        """)
        self.show_status.setChecked(True)
        
        self.show_terminal = QCheckBox("Show Terminal", self.settings_frame)
        self.show_terminal.setGeometry(QRect(200, 40, 131, 22))
        self.show_terminal.setStyleSheet(self.show_status.styleSheet())
        self.show_terminal.setChecked(True)
        self.show_terminal.stateChanged.connect(self.toggle_terminal_visibility)
        
        self.custom_search = QCheckBox("Custom Search", self.settings_frame)
        self.custom_search.setGeometry(QRect(10, 90, 131, 22))
        self.custom_search.setStyleSheet(self.show_status.styleSheet())
        self.custom_search.setChecked(True)
        
        self.mute_nova = QCheckBox("Mute Nova", self.settings_frame)
        self.mute_nova.setGeometry(QRect(200, 90, 111, 22))
        self.mute_nova.setStyleSheet(self.show_status.styleSheet())
        
        # All GIF Labels
        self.starting_gif = QLabel(self.main_container)
        self.starting_gif.setGeometry(QRect(0, 100, 181, 171))
        self.starting_gif.setPixmap(QPixmap("D:/Material_gui_jarvis/logo.gif"))
        self.starting_gif.setScaledContents(True)
        
        self.starting_gif_2 = QLabel(self.main_container)
        self.starting_gif_2.setGeometry(QRect(0, 100, 181, 181))
        self.starting_gif_2.setPixmap(QPixmap("D:/Material_gui_jarvis/path.gif"))
        self.starting_gif_2.setScaledContents(True)
        
        self.starting_gif_3 = QLabel(self.main_container)
        self.starting_gif_3.setGeometry(QRect(0, 90, 181, 171))
        self.starting_gif_3.setPixmap(QPixmap("D:/Material_gui_jarvis/new.gif"))
        self.starting_gif_3.setScaledContents(True)
        
        self.voice_assistant_gif = QLabel(self.main_container)
        self.voice_assistant_gif.setGeometry(QRect(0, 90, 181, 181))
        self.voice_assistant_gif.setPixmap(QPixmap("D:/Downloads/voice assistant.gif.gif"))
        self.voice_assistant_gif.setScaledContents(True)
        
        # Search Frame
        self.search = QFrame(self.main_container)
        self.search.setGeometry(QRect(190, 230, 381, 51))
        self.search.setStyleSheet("""
            background-color: rgb(0,0,0);
            border-color: rgb(255, 255, 255);
            border-width: 1px;
            border-style: solid;
        """)
        self.search.setFrameShape(QFrame.Shape.StyledPanel)
        self.search.setFrameShadow(QFrame.Shadow.Raised)
        
        # Search Box
        self.search_box = QLineEdit(self.search)
        self.search_box.setGeometry(QRect(0, 0, 291, 51))
        self.search_box.setPlaceholderText(" Enter your query to search")
        self.search_box.setStyleSheet("""
            color: rgb(255, 255, 255);
            background-color: transparent;
            border: none;
        """)
        
        # Send Button
        self.send_button = QPushButton("Send", self.search)
        self.send_button.setGeometry(QRect(300, 10, 71, 31))
        self.send_button.setStyleSheet("""
            font: 20pt "Segoe UI";
            color: rgb(255, 255, 255);
            background-color: transparent;
        """)
        self.send_button.clicked.connect(self.perform_search)
        
        # Nova Terminal Frame
        self.nova_terminal_outerframe = QFrame(self.main_container)
        self.nova_terminal_outerframe.setGeometry(QRect(0, 290, 571, 331))
        self.nova_terminal_outerframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.nova_terminal_outerframe.setFrameShadow(QFrame.Shadow.Raised)
        
        # Terminal Heading
        self.nova_terminal_heading = QTextEdit(self.nova_terminal_outerframe)
        self.nova_terminal_heading.setGeometry(QRect(0, 0, 571, 41))
        self.nova_terminal_heading.setStyleSheet("""
            color: rgb(255, 255, 255);
            background-color: transparent;
        """)
        self.nova_terminal_heading.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.nova_terminal_heading.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.nova_terminal_heading.setHtml("""
            <html><head><style>
            p { margin: 0; }
            </style></head><body>
            <p align="center" style="font-size:16pt;">NOVA TERMINAL</p>
            </body></html>
        """)
        self.nova_terminal_heading.setReadOnly(True)
        
        # Terminal Output
        self.interaction_print_terminal = QPlainTextEdit(self.nova_terminal_outerframe)
        self.interaction_print_terminal.setGeometry(QRect(0, 40, 571, 291))
        self.interaction_print_terminal.setStyleSheet("""
            color: rgb(255, 255, 255);
            background-color: transparent;
        """)
        self.interaction_print_terminal.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.interaction_print_terminal.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.interaction_print_terminal.setReadOnly(True)
        
        # Initially hide all widgets except NOVA_ONLINE button
        self.main_container.hide()
        # Set initial window size to just show the NOVA button
        self.resize(181, 100)
    
    def toggle_gui(self):
        if self.is_expanded:
            # Collapse GUI back to the minimal view
            self.main_container.hide()
            self.resize(181, 100)
        else:
            # Expand GUI and ensure NOVA_ONLINE remains visible on top
            self.main_container.show()
            if self.show_terminal.isChecked():
                self.resize(575, 626)
            else:
                self.resize(575, 291)
            self.NOVA_ONLINE.raise_()  # Bring the NOVA Online button to the front
        self.is_expanded = not self.is_expanded

    def toggle_terminal_visibility(self, state):
        if state == Qt.CheckState.Unchecked:
            self.nova_terminal_outerframe.hide()
            self.resize(571, 291)
        else:
            self.nova_terminal_outerframe.show()
            self.resize(575, 626)
    

    def setup_gifs(self):
        # Setup actual GIF animations
        gifs = [
            ("D:/Material_gui_jarvis/logo.gif", self.starting_gif),
            ("D:/Material_gui_jarvis/path.gif", self.starting_gif_2),
            ("D:/Material_gui_jarvis/new.gif", self.starting_gif_3),
            ("D:/Downloads/voice assistant.gif.gif", self.voice_assistant_gif)
        ]
        for gif_path, label in gifs:
            movie = QMovie(gif_path)
            label.setMovie(movie)
            movie.start()
    
    def initDragFunctionality(self):
        self.oldPos = self.pos()
        self.setMouseTracking(True)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPosition().toPoint()
    
    def perform_search(self):
        query = self.search_box.text()
        if query:
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            self.interaction_print_terminal.appendPlainText(f"Searching Google for: {query}")
            self.search_box.clear()
    
    def minimize_gui(self):
        """
        Custom minimize behavior:
          - If "Show Status Icon" is checked, display the NOVA Online button plus the GIF.
          - If unchecked, display only the NOVA Online button.
        In both cases, the full GUI is collapsed.
        """
        # Collapse the full GUI view:
        self.main_container.hide()
        self.is_expanded = False

        if self.show_status.isChecked():
            # Show the status icon (using the voice assistant GIF as an example)
            self.voice_assistant_gif.show()
            # Hide other parts of the full GUI
            #self.full_setting_outer_frame.hide()
            #self.search.hide()
            #self.nova_terminal_outerframe.hide()
            # Resize the window to show NOVA Online and the GIF
            self.resize(191, 291)

        else:
            # Hide the GIF altogether
            self.voice_assistant_gif.hide()
            self.resize(181, 100)
        
        # Ensure NOVA_ONLINE is visible in minimized view
        self.NOVA_ONLINE.raise_()
    
    def changeEvent(self, event):
        """
        Override changeEvent to catch window state changes.
        For example, if the window is restored from a minimized state,
        we can re-show the full GUI if it was expanded.
        """
        if event and event.type() == QEvent.Type.WindowStateChange:
            # If the window was minimized (by OS action) and then restored:
            if event.oldState() & Qt.WindowState.WindowMinimized:
                if self.is_expanded:
                    self.main_container.show()
                    self.full_setting_outer_frame.show()
                    self.search.show()
                    if self.show_terminal.isChecked():
                        self.nova_terminal_outerframe.show()
                    self.resize(575, 626 if self.show_terminal.isChecked() else 291)
        super().changeEvent(event)

def main():
    app = QApplication(sys.argv)
    window = JarvisOverlayGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
