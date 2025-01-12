# import sys
# from PyQt5.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QWidget,
#     QLabel,
#     QPushButton,
#     QHBoxLayout,
#     QVBoxLayout,
#     QFrame,
#     QSizePolicy,
# )
# from PyQt5.QtCore import Qt, QTimer, QTime
# from PyQt5.QtGui import QFont, QIcon, QPixmap, QColor, QPainter, QPen


# class AudioWaveform(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.waveform_data = [
#             (50, 20, 100),
#             (50, 20, 120),
#             (50, 20, 140),
#             (50, 20, 120),
#             (50, 20, 100),
#         ]
#         self.bar_color = QColor(0, 255, 255)

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         pen = QPen(self.bar_color)
#         pen.setWidth(3)
#         painter.setPen(pen)
#         x_spacing = self.width() / (len(self.waveform_data) * 2 + 1)
#         start_x = x_spacing
#         for i, (offset, amplitude, bar_height) in enumerate(self.waveform_data):
#             x_pos = start_x + i * x_spacing * 2
#             y_pos = self.height() / 2 - bar_height / 2
#             painter.drawLine(x_pos, self.height() / 2, x_pos, y_pos+bar_height )


# class MainApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Voice Control Interface")
#         self.setGeometry(100, 100, 600, 400)
#         self.setStyleSheet("background-color: black;")

#         self.main_widget = QWidget(self)
#         self.setCentralWidget(self.main_widget)
#         self.setup_ui()

#     def setup_ui(self):
#         main_layout = QVBoxLayout(self.main_widget)

#         # Header container
#         header_container = QFrame()
#         header_container.setObjectName("headerContainer")
#         header_container.setStyleSheet(
#             "#headerContainer { background-color: rgba(0, 0, 0, 0.7); border-radius: 10px; padding: 10px; }"
#         )
#         header_layout = QHBoxLayout(header_container)
#         header_layout.setAlignment(Qt.AlignHCenter)
#         header_container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

#         # Brain icon
#         brain_icon_label = QLabel()
#         brain_icon_label.setPixmap(
#             QPixmap("brain_icon.png").scaled(30, 30, Qt.KeepAspectRatio)
#         )
#         header_layout.addWidget(brain_icon_label)
#         #Spacer item
#         header_layout.addStretch(1)


#         # Time Label
#         self.time_label = QLabel("12:43:03 PM")
#         self.time_label.setStyleSheet("color: white; font-size: 14px; margin-right: 10px")
#         self.time_label.setAlignment(Qt.AlignRight)
#         header_layout.addWidget(self.time_label)


#         # Status Label
#         status_label = QLabel("SYSTEM ACTIVE")
#         status_label.setStyleSheet("color: white; font-size: 12px; margin-right: 10px")
#         header_layout.addWidget(status_label)

#         # Control Buttons
#         settings_icon = QIcon("settings_icon.png")
#         power_icon = QIcon("power_icon.png")
#         add_icon = QIcon("add_icon.png")

#         settings_button = QPushButton()
#         settings_button.setIcon(settings_icon)
#         settings_button.setFixedSize(24,24)
#         settings_button.setStyleSheet("QPushButton {border: none; padding: 2px; background-color: transparent}")
#         header_layout.addWidget(settings_button)

#         power_button = QPushButton()
#         power_button.setIcon(power_icon)
#         power_button.setFixedSize(24, 24)
#         power_button.setStyleSheet("QPushButton {border: none; padding: 2px; background-color: transparent}")
#         header_layout.addWidget(power_button)
        
#         add_button = QPushButton()
#         add_button.setIcon(add_icon)
#         add_button.setFixedSize(24, 24)
#         add_button.setStyleSheet("QPushButton {border: none; padding: 2px; background-color: transparent}")
#         header_layout.addWidget(add_button)

#         main_layout.addWidget(header_container)
        
#         # Waveform Widget
#         self.audio_waveform = AudioWaveform()
#         main_layout.addWidget(self.audio_waveform)

#         # Voice Recognition Status
#         voice_status = QLabel("VOICE RECOGNITION ACTIVE")
#         voice_status.setAlignment(Qt.AlignCenter)
#         voice_status.setStyleSheet("color: white; font-size: 12px; margin-top: 10px")
#         main_layout.addWidget(voice_status)

#         # Activation Button
#         self.activation_button = QPushButton()
#         self.activation_button.setFixedSize(80, 80)
#         self.activation_button.setStyleSheet(
#             "QPushButton {background-color: rgba(0, 255, 255, 0.7); border-radius: 40px;}"
#         )
#         self.activation_button.clicked.connect(self.toggle_activation)

#         activation_layout = QVBoxLayout()
#         activation_layout.addWidget(self.activation_button)
#         activation_layout.setAlignment(Qt.AlignCenter)
#         main_layout.addLayout(activation_layout)

#         # Timer for updating time
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_time)
#         self.timer.start(1000)

#     def update_time(self):
#       current_time = QTime.currentTime()
#       formatted_time = current_time.toString("hh:mm:ss AP")
#       self.time_label.setText(formatted_time)

#     def toggle_activation(self):
#         if self.activation_button.styleSheet() == "QPushButton {background-color: rgba(0, 255, 255, 0.7); border-radius: 40px;}":
#            self.activation_button.setStyleSheet(
#                "QPushButton {background-color: rgba(255, 0, 0, 0.7); border-radius: 40px;}"
#            )
#         else:
#            self.activation_button.setStyleSheet(
#               "QPushButton {background-color: rgba(0, 255, 255, 0.7); border-radius: 40px;}"
#            )


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainApp()
#     window.show()
#     sys.exit(app.exec_())





from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(984, 572)
        self.centralwidget = QtWidgets.QWidget(jarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1021, 601))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 330, 391, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(".\\Material/path.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(720, 20, 261, 221))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(".\\Material/logo.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 510, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border -radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border -radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 411, 301))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\Material/new.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
        self.pushButton.setStyleSheet("font: 8pt \"Segoe Print\";\n"
"color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 510, 81, 31))
        self.pushButton_2.setStyleSheet("font: 8pt \"Verdana\";\n"
"alternate-background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        jarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUi)
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)

    def retranslateUi(self, jarvisUi):
        _translate = QtCore.QCoreApplication.translate
        jarvisUi.setWindowTitle(_translate("jarvisUi", "MainWindow"))
        self.pushButton.setText(_translate("jarvisUi", "Start"))
        self.pushButton_2.setText(_translate("jarvisUi", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisUi = QtWidgets.QMainWindow()
    ui = Ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())
