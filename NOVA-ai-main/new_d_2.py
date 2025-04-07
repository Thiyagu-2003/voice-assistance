import sys
import webbrowser
from PyQt5.QtWidgets import (QApplication, QWidget, QFrame, QPushButton, QLabel,
                             QTextBrowser, QCheckBox, QLineEdit, QTextEdit, QPlainTextEdit)
from PyQt5.QtCore import Qt, QRect, QEvent, QPoint
from PyQt5.QtGui import QPixmap, QMovie, QIcon

class JarvisOverlayGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.is_expanded = False
        self.setupUi()
        self.initDragFunctionality()
        self.setup_gifs()

    def setupUi(self):
        self.setObjectName("JarvisOverlayGUI")
        self.setGeometry(0, 0, 575, 626)
        self.setWindowTitle("JarvisOverlayGUI")
        self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

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
        self.NOVA_ONLINE.clicked.connect(self.toggle_gui)

        self.main_container = QFrame(self)
        self.main_container.setGeometry(QRect(0, 0, 575, 626))

        self.full_setting_outer_frame = QFrame(self.main_container)
        self.full_setting_outer_frame.setGeometry(QRect(190, 0, 381, 231))
        self.full_setting_outer_frame.setStyleSheet("""
            background-color: rgb(0, 0, 0);
            border: 2px solid rgb(255,255,255);
        """)
        self.full_setting_outer_frame.setFrameShape(QFrame.StyledPanel)
        self.full_setting_outer_frame.setFrameShadow(QFrame.Raised)

        self.voise_assistant_label = QLabel(self.full_setting_outer_frame)
        self.voise_assistant_label.setGeometry(QRect(0, 0, 291, 41))
        self.voise_assistant_label.setPixmap(QPixmap("D:/Downloads/Frame 2.png"))
        self.voise_assistant_label.setScaledContents(True)

        self.Exit_Button = QPushButton("X", self.full_setting_outer_frame)
        self.Exit_Button.setGeometry(QRect(330, 0, 51, 41))
        self.Exit_Button.setStyleSheet("""
            font: 20pt "Segoe UI";
            color: rgb(255, 255, 255);
        """)
        self.Exit_Button.clicked.connect(self.close)

        self.Minimize_Button = QPushButton("-", self.full_setting_outer_frame)
        self.Minimize_Button.setGeometry(QRect(290, 0, 41, 41))
        self.Minimize_Button.setStyleSheet("""
            font: 30pt "Segoe UI";
            color: rgb(255, 255, 255);
        """)
        self.Minimize_Button.clicked.connect(self.minimize_gui)

        self.settings_frame = QFrame(self.full_setting_outer_frame)
        self.settings_frame.setGeometry(QRect(0, 40, 381, 191))
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)

        self.only_settings_bar = QTextBrowser(self.settings_frame)
        self.only_settings_bar.setGeometry(QRect(0, 0, 101, 31))
        self.only_settings_bar.setStyleSheet("""
            color: white;
            background-color: transparent;
            border: none;
        """)
        self.only_settings_bar.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.only_settings_bar.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.only_settings_bar.setHtml("""
            <html><body><p style="font-size:16pt; font-weight:700;"> Settings</p></body></html>
        """)

        # Checkboxes
        self.show_status = QCheckBox("Show Status Icon", self.settings_frame)
        self.show_status.setGeometry(QRect(10, 40, 141, 22))
        self.show_status.setStyleSheet("font: 11pt 'Segoe UI'; color: white; background: transparent;")
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

        self.listening_gif = QLabel(self.main_container)
        self.listening_gif.setGeometry(QRect(0, 100, 181, 171))

        self.loading_gif = QLabel(self.main_container)
        self.loading_gif.setGeometry(QRect(0, 100, 181, 181))

        self.speaking_gif = QLabel(self.main_container)
        self.speaking_gif.setGeometry(QRect(0, 90, 181, 171))

        self.sleeping_gif = QLabel(self.main_container)
        self.sleeping_gif.setGeometry(QRect(0, 90, 181, 181))

        self.search = QFrame(self.main_container)
        self.search.setGeometry(QRect(190, 230, 381, 51))
        self.search.setStyleSheet("""
            background-color: black;
            border: 1px solid white;
        """)
        self.search.setFrameShape(QFrame.StyledPanel)
        self.search.setFrameShadow(QFrame.Raised)

        self.search_box = QLineEdit(self.search)
        self.search_box.setGeometry(QRect(0, 0, 291, 51))
        self.search_box.setPlaceholderText(" Enter your query to search")
        self.search_box.setStyleSheet("color: white; background: transparent; border: none;")

        self.send_button = QPushButton("Send", self.search)
        self.send_button.setGeometry(QRect(300, 10, 71, 31))
        self.send_button.setStyleSheet("font: 20pt 'Segoe UI'; color: white; background: transparent;")
        self.send_button.clicked.connect(self.perform_search)

        self.nova_terminal_outerframe = QFrame(self.main_container)
        self.nova_terminal_outerframe.setGeometry(QRect(0, 290, 571, 331))
        self.nova_terminal_outerframe.setStyleSheet("""
            background-color: black;
            border: 2px solid white;
        """)
        self.nova_terminal_outerframe.setFrameShape(QFrame.StyledPanel)
        self.nova_terminal_outerframe.setFrameShadow(QFrame.Raised)

        self.nova_terminal_heading = QTextEdit(self.nova_terminal_outerframe)
        self.nova_terminal_heading.setGeometry(QRect(0, 0, 571, 41))
        self.nova_terminal_heading.setStyleSheet("color: white; background: transparent;")
        self.nova_terminal_heading.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.nova_terminal_heading.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.nova_terminal_heading.setHtml("""
            <html><body><p align="center" style="font-size:16pt;">NOVA TERMINAL</p></body></html>
        """)
        self.nova_terminal_heading.setReadOnly(True)

        self.TerminalText = QPlainTextEdit(self.nova_terminal_outerframe)
        self.TerminalText.setGeometry(QRect(0, 40, 571, 291))
        self.TerminalText.setStyleSheet("color: white; background: transparent;")
        self.TerminalText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.TerminalText.setReadOnly(True)

        self.main_container.hide()
        self.resize(181, 100)

    def toggle_gui(self):
        if self.is_expanded:
            self.main_container.hide()
            self.resize(181, 100)
        else:
            self.main_container.show()
            self.resize(575, 626 if self.show_terminal.isChecked() else 291)
            self.NOVA_ONLINE.raise_()
        self.is_expanded = not self.is_expanded

    def toggle_terminal_visibility(self, state):
        if state == Qt.Unchecked:
            self.nova_terminal_outerframe.hide()
            self.resize(571, 291)
        else:
            self.nova_terminal_outerframe.show()
            self.resize(575, 626)

    def append_to_terminal(self, text):
        self.TerminalText.appendPlainText(text)

    def setup_gifs(self):
        gifs = [
            ("D:/Material_gui_jarvis/logo.gif", self.listening_gif),
            ("D:/Material_gui_jarvis/path.gif", self.loading_gif),
            ("D:/Material_gui_jarvis/new.gif", self.speaking_gif),
            ("D:/Downloads/voice assistant.gif.gif", self.sleeping_gif)
        ]
        for gif_path, label in gifs:
            movie = QMovie(gif_path)
            label.setMovie(movie)
            movie.start()

    def initDragFunctionality(self):
        self.oldPos = self.pos()
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = event.globalPos() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def perform_search(self):
        query = self.search_box.text()
        if query:
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            self.TerminalText.appendPlainText(f"Searching Google for: {query}")
            self.search_box.clear()

    def minimize_gui(self):
        self.main_container.hide()
        self.is_expanded = False

        if self.show_status.isChecked():
            self.sleeping_gif.show()
            self.resize(191, 291)
        else:
            self.sleeping_gif.hide()
            self.resize(181, 100)
        self.NOVA_ONLINE.raise_()

    def changeEvent(self, event):
        if event and event.type() == QEvent.WindowStateChange:
            if self.is_expanded and self.isVisible():
                self.main_container.show()
                self.full_setting_outer_frame.show()
                self.search.show()
                if self.show_terminal.isChecked():
                    self.nova_terminal_outerframe.show()
                self.resize(575, 626 if self.show_terminal.isChecked() else 291)
        super().changeEvent(event)

    def update_gif_state(self, state):
        self.speaking_gif.hide()
        self.listening_gif.hide()
        self.loading_gif.hide()
        self.sleeping_gif.hide()

        if state == "speaking":
            self.speaking_gif.show()
            self.append_to_terminal("NOVA is speaking...")
        elif state == "listening":
            self.listening_gif.show()
            self.append_to_terminal("NOVA is listening...")
        elif state == "loading":
            self.loading_gif.show()
            self.append_to_terminal("NOVA is processing...")
        elif state == "sleeping":
            self.sleeping_gif.show()
            self.append_to_terminal("NOVA is in sleep mode...")
        else:
            self.sleeping_gif.show()
            self.append_to_terminal(f"Unknown state: {state}. Defaulting to sleep mode...")

def main():
    app = QApplication(sys.argv)
    window = JarvisOverlayGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
