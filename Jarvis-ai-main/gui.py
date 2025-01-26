from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class JarvisUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jarvis UI")
        self.setFixedSize(984, 572)  # Maintain fixed size
        self.setStyleSheet("background-color: #1e1e1e;")  # Set black background for all widgets
        self.setup_ui()

    def setup_ui(self):
        # Central Widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Background Label
        self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
        self.backgroundLabel.setStyleSheet("background-color: black;")
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 984, 572))

        # Path Gif Label
        self.pathGifLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathGif = QtGui.QMovie(".\\Material/path.gif")
        self.pathGifLabel.setMovie(self.pathGif)
        self.pathGifLabel.setScaledContents(True)
        self.pathGifLabel.setGeometry(QtCore.QRect(290, 330, 391, 201))

        # Logo Gif Label
        self.logoGifLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoGif = QtGui.QMovie(".\\Material/logo.gif")
        self.logoGifLabel.setMovie(self.logoGif)
        self.logoGifLabel.setScaledContents(True)
        self.logoGifLabel.setGeometry(QtCore.QRect(720, 20, 261, 221))

        # New Gif Label
        self.newGifLabel = QtWidgets.QLabel(self.centralwidget)
        self.newGif = QtGui.QMovie(".\\Material/new.gif")
        self.newGifLabel.setMovie(self.newGif)
        self.newGifLabel.setScaledContents(True)
        self.newGifLabel.setGeometry(QtCore.QRect(10, 10, 411, 301))

        # Buttons
        self.startButton = QtWidgets.QPushButton("Start", self.centralwidget)
        self.startButton.setFont(QtGui.QFont("Segoe Print", 8))
        self.startButton.setStyleSheet("""
            QPushButton {
               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4CAF50, stop: 1 #388E3C);
               border-radius: 5px;
               color: white;
               padding: 8px;
            }
            QPushButton:hover {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #66BB6A, stop: 1 #43A047);
            }
            QPushButton:pressed {
              background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #388E3C, stop: 1 #2E7D32);
            }
        """)
        self.startButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
        self.startButton.clicked.connect(self.start_button_clicked)

        self.stopButton = QtWidgets.QPushButton("Stop", self.centralwidget)
        self.stopButton.setFont(QtGui.QFont("Verdana", 8))
        self.stopButton.setStyleSheet("""
            QPushButton {
              background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f44336, stop: 1 #d32f2f);
              border-radius: 5px;
              color: white;
              padding: 8px;
            }
            QPushButton:hover {
              background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ef5350, stop: 1 #c62828);
            }
            QPushButton:pressed {
              background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d32f2f, stop: 1 #b71c1c);
            }
        """)
        self.stopButton.setGeometry(QtCore.QRect(840, 510, 81, 31))
        self.stopButton.clicked.connect(self.stop_button_clicked)

    def start_button_clicked(self):
        """Start the main code and play GIFs."""
        self.pathGif.start()
        self.logoGif.start()
        self.newGif.start()
        print("Start button clicked - Main code is running...")

        # Add your main logic here
        # For example, start a thread to run background tasks if needed.

    def stop_button_clicked(self):
        """Exit the application."""
        print("Stop button clicked - Exiting...")
        QtWidgets.QApplication.quit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Set the style to dark
    app.setStyle("Fusion")
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
    palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
    palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
    palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
    palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
    palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
    app.setPalette(palette)

    jarvis_ui = JarvisUI()
    jarvis_ui.show()
    sys.exit(app.exec_())


# # from PyQt5 import QtCore, QtGui, QtWidgets
# # import sys

# # class JarvisUI(QtWidgets.QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Jarvis UI")
# #         self.setFixedSize(984, 572)  # Maintain fixed size
# #         self.setStyleSheet("background-color: rgb(0, 0, 0);")  # Set black background for all widgets
# #         self.setup_ui()

# #     def setup_ui(self):
# #         # Central Widget
# #         self.centralwidget = QtWidgets.QWidget(self)
# #         self.setCentralWidget(self.centralwidget)

# #         # Background Label
# #         self.backgroundLabel = QtWidgets.QLabel(self.centralwidget)
# #         self.backgroundLabel.setStyleSheet("background-color: rgb(0, 0, 0);")
# #         self.backgroundLabel.setScaledContents(True)
# #         self.backgroundLabel.setGeometry(QtCore.QRect(0, 0, 984, 572))

# #         # Path Gif Label
# #         self.pathGifLabel = QtWidgets.QLabel(self.centralwidget)
# #         self.pathGif = QtGui.QMovie(".\\Material/path.gif")
# #         self.pathGifLabel.setMovie(self.pathGif)
# #         self.pathGifLabel.setScaledContents(True)
# #         self.pathGifLabel.setGeometry(QtCore.QRect(290, 330, 391, 201))

# #         # Logo Gif Label
# #         self.logoGifLabel = QtWidgets.QLabel(self.centralwidget)
# #         self.logoGif = QtGui.QMovie(".\\Material/logo.gif")
# #         self.logoGifLabel.setMovie(self.logoGif)
# #         self.logoGifLabel.setScaledContents(True)
# #         self.logoGifLabel.setGeometry(QtCore.QRect(720, 20, 261, 221))

# #         # New Gif Label
# #         self.newGifLabel = QtWidgets.QLabel(self.centralwidget)
# #         self.newGif = QtGui.QMovie(".\\Material/new.gif")
# #         self.newGifLabel.setMovie(self.newGif)
# #         self.newGifLabel.setScaledContents(True)
# #         self.newGifLabel.setGeometry(QtCore.QRect(10, 10, 411, 301))

# #         # Text Browser for information
# #         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
# #         self.textBrowser.setGeometry(QtCore.QRect(0, 510, 191, 41))
# #         font = QtGui.QFont()
# #         font.setFamily("Sitka Subheading")
# #         font.setPointSize(16)
# #         self.textBrowser.setFont(font)
# #         self.textBrowser.setStyleSheet("background:transparent; border-radius:none;")
# #         self.textBrowser.setObjectName("textBrowser")

# #         self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
# #         self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
# #         font = QtGui.QFont()
# #         font.setPointSize(16)
# #         self.textBrowser_2.setFont(font)
# #         self.textBrowser_2.setStyleSheet("background:transparent; border-radius:none;")
# #         self.textBrowser_2.setObjectName("textBrowser_2")

# #         # Buttons
# #         self.startButton = QtWidgets.QPushButton("Start", self.centralwidget)
# #         self.startButton.setFont(QtGui.QFont("Segoe Print", 8))
# #         self.startButton.setStyleSheet("""
# #             QPushButton {
# #                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4CAF50, stop: 1 #388E3C);
# #                border-radius: 5px;
# #                color: white;
# #                padding: 8px;
# #             }
# #             QPushButton:hover {
# #                 background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #66BB6A, stop: 1 #43A047);
# #             }
# #             QPushButton:pressed {
# #               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #388E3C, stop: 1 #2E7D32);
# #             }
# #         """)
# #         self.startButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
# #         self.startButton.clicked.connect(self.start_button_clicked)

# #         self.stopButton = QtWidgets.QPushButton("Stop", self.centralwidget)
# #         self.stopButton.setFont(QtGui.QFont("Verdana", 8))
# #         self.stopButton.setStyleSheet("""
# #             QPushButton {
# #               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f44336, stop: 1 #d32f2f);
# #               border-radius: 5px;
# #               color: white;
# #               padding: 8px;
# #             }
# #             QPushButton:hover {
# #               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ef5350, stop: 1 #c62828);
# #             }
# #             QPushButton:pressed {
# #               background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d32f2f, stop: 1 #b71c1c);
# #             }
# #         """)
# #         self.stopButton.setGeometry(QtCore.QRect(840, 510, 81, 31))
# #         self.stopButton.clicked.connect(self.stop_button_clicked)

# #     def start_button_clicked(self):
# #         """Start the main code and play GIFs."""
# #         self.pathGif.start()
# #         self.logoGif.start()
# #         self.newGif.start()
# #         print("Start button clicked - Main code is running...")

# #         # Add your main logic here
# #         # For example, start a thread to run background tasks if needed.

# #     def stop_button_clicked(self):
# #         """Exit the application."""
# #         print("Stop button clicked - Exiting...")
# #         QtWidgets.QApplication.quit()


# # if __name__ == "__main__":
# #     app = QtWidgets.QApplication(sys.argv)
# #     # Set the style to dark
# #     app.setStyle("Fusion")
# #     palette = QtGui.QPalette()
# #     palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
# #     palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
# #     palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
# #     palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
# #     palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
# #     palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
# #     palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
# #     palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
# #     palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
# #     palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
# #     palette.setColor(QtGui.QPalette.Link, QtGui.QColor(42, 130, 218))
# #     palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(42, 130, 218))
# #     palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
# #     app.setPalette(palette)

# #     jarvis_ui = JarvisUI()
# #     jarvis_ui.show()
# #     sys.exit(app.exec_())


# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.clock import Clock
# from kivy.core.window import Window
# from kivy.properties import BooleanProperty, StringProperty, NumericProperty
# from kivy.graphics import Color, RoundedRectangle, Line
# from datetime import datetime
# import random

# class GlassPanel(BoxLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         with self.canvas.before:
#             Color(1, 1, 1, 0.1)
#             self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[16])
#         self.bind(pos=self._update_rect, size=self._update_rect)
    
#     def _update_rect(self, instance, value):
#         self.rect.pos = instance.pos
#         self.rect.size = instance.size

# class NeonButton(Button):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.background_normal = ''
#         self.background_color = (0, 0, 0, 0)
#         with self.canvas.before:
#             Color(*kwargs.get('bg_color', (0, 0.8, 0, 1)))
#             self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[30])
#         self.bind(pos=self._update_rect, size=self._update_rect)
    
#     def _update_rect(self, instance, value):
#         self.rect.pos = instance.pos
#         self.rect.size = instance.size

# class JarvisAssistant(BoxLayout):
#     is_dark_theme = BooleanProperty(True)
#     system_status = StringProperty('System Active')
#     cpu_usage = NumericProperty(0)
#     gpu_usage = NumericProperty(0)
#     current_time = StringProperty('')
    
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.orientation = 'vertical'
#         self.padding = 20
#         self.spacing = 10
#         Clock.schedule_interval(self.update_stats, 2)
#         Clock.schedule_interval(self.update_time, 1)
#         self._build_ui()
        
#     def _build_ui(self):
#         # Header
#         header = BoxLayout(size_hint_y=None, height=50, spacing=10)
#         header.add_widget(Widget(size_hint_x=0.3))
        
#         time_label = Label(
#             text=self.current_time,
#             font_size='24sp',
#             color=(0, 1, 1, 1),
#             size_hint_x=0.4
#         )
#         self.bind(current_time=lambda _, v: setattr(time_label, 'text', v))
#         header.add_widget(time_label)
        
#         controls = BoxLayout(size_hint_x=0.3, spacing=10)
#         theme_btn = Button(
#             text='🌙',
#             size_hint=(None, None),
#             size=(40, 40),
#             on_press=self.toggle_theme
#         )
#         settings_btn = Button(
#             text='⚙️',
#             size_hint=(None, None),
#             size=(40, 40)
#         )
#         controls.add_widget(theme_btn)
#         controls.add_widget(settings_btn)
#         header.add_widget(controls)
#         self.add_widget(header)
        
#         # Status Panel
#         status_panel = GlassPanel(size_hint_y=None, height=80, padding=10)
#         status_left = BoxLayout(orientation='vertical')
#         status_left.add_widget(Label(text='System Status', color=(0.7, 0.7, 0.7, 1)))
#         status_label = Label(text=self.system_status, color=(0, 1, 0, 1))
#         self.bind(system_status=lambda _, v: setattr(status_label, 'text', v))
#         status_left.add_widget(status_label)
#         status_panel.add_widget(status_left)
        
#         status_right = BoxLayout(orientation='vertical')
#         cpu_label = Label(text=f'CPU: {self.cpu_usage}%', color=(0.7, 0.7, 0.7, 1))
#         gpu_label = Label(text=f'GPU: {self.gpu_usage}%', color=(0.7, 0.7, 0.7, 1))
#         self.bind(
#             cpu_usage=lambda _, v: setattr(cpu_label, 'text', f'CPU: {v}%'),
#             gpu_usage=lambda _, v: setattr(gpu_label, 'text', f'GPU: {v}%')
#         )
#         status_right.add_widget(cpu_label)
#         status_right.add_widget(gpu_label)
#         status_panel.add_widget(status_right)
#         self.add_widget(status_panel)
        
#         # Waveform
#         waveform = GlassPanel()
#         with waveform.canvas:
#             Color(0, 1, 1, 0.3)
#             Line(points=[waveform.x, waveform.center_y, waveform.right, waveform.center_y],
#                  width=2, dash_length=10, dash_offset=5)
#         self.add_widget(waveform)
        
#         # Controls
#         controls = BoxLayout(size_hint_y=None, height=80, spacing=20)
#         start_btn = NeonButton(
#             text='🎤',
#             bg_color=(0, 0.8, 0, 1),
#             on_press=self.start_listening
#         )
#         stop_btn = NeonButton(
#             text='⏹',
#             bg_color=(0.8, 0, 0, 1),
#             on_press=self.stop_listening
#         )
#         controls.add_widget(start_btn)
#         controls.add_widget(stop_btn)
#         self.add_widget(controls)
        
#     def update_stats(self, dt):
#         self.cpu_usage = random.randint(0, 100)
#         self.gpu_usage = random.randint(0, 100)
        
#     def update_time(self, dt):
#         self.current_time = datetime.now().strftime('%H:%M:%S')
        
#     def toggle_theme(self, *args):
#         self.is_dark_theme = not self.is_dark_theme
#         Window.clearcolor = (0.07, 0.07, 0.07, 1) if self.is_dark_theme else (0.96, 0.96, 0.96, 1)
        
#     def start_listening(self, *args):
#         self.system_status = 'Listening...'
        
#     def stop_listening(self, *args):
#         self.system_status = 'System Active'

# class JarvisApp(App):
#     def build(self):
#         Window.clearcolor = (0.07, 0.07, 0.07, 1)
#         return JarvisAssistant()

# if __name__ == '__main__':
#     JarvisApp().run()
