# # from PyQt5 import QtCore, QtGui, QtWidgets
# # from PyQt5.QtGui import QPixmap
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# # import sys


# # class Ui_jarvisUi(object):
# #     def setupUi(self, jarvisUi):
# #         jarvisUi.setObjectName("jarvisUi")
# #         jarvisUi.resize(984, 572)
# #         self.is_dark_mode = True  # Initialize with a dark theme
# #         self.centralwidget = QtWidgets.QWidget(jarvisUi)
# #         self.centralwidget.setObjectName("centralwidget")
# #         self.label = QtWidgets.QLabel(self.centralwidget)
# #         self.label.setGeometry(QtCore.QRect(-10, -10, 1021, 601))
# #         self.label.setText("")
# #         self.label.setScaledContents(True)
# #         self.label.setObjectName("label")
# #         self.label_3 = QtWidgets.QLabel(self.centralwidget)
# #         self.label_3.setGeometry(QtCore.QRect(290, 330, 391, 201))
# #         self.label_3.setText("")
# #         self.label_3.setPixmap(QtGui.QPixmap(".\\Material/path.gif"))
# #         self.label_3.setScaledContents(True)
# #         self.label_3.setObjectName("label_3")
# #         self.label_5 = QtWidgets.QLabel(self.centralwidget)
# #         self.label_5.setGeometry(QtCore.QRect(720, 20, 261, 221))
# #         self.label_5.setText("")
# #         self.label_5.setPixmap(QtGui.QPixmap(".\\Material/logo.gif"))
# #         self.label_5.setScaledContents(True)
# #         self.label_5.setObjectName("label_5")
# #         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
# #         self.textBrowser.setGeometry(QtCore.QRect(0, 510, 191, 41))
# #         font = QtGui.QFont()
# #         font.setFamily("Sitka Subheading")
# #         font.setPointSize(16)
# #         self.textBrowser.setFont(font)
# #         self.textBrowser.setObjectName("textBrowser")
# #         self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
# #         self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
# #         font = QtGui.QFont()
# #         font.setPointSize(16)
# #         self.textBrowser_2.setFont(font)
# #         self.textBrowser_2.setObjectName("textBrowser_2")
# #         self.label_2 = QtWidgets.QLabel(self.centralwidget)
# #         self.label_2.setGeometry(QtCore.QRect(10, 10, 411, 301))
# #         self.label_2.setText("")
# #         self.label_2.setPixmap(QtGui.QPixmap(".\\Material/new.gif"))
# #         self.label_2.setScaledContents(True)
# #         self.label_2.setObjectName("label_2")
# #         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
# #         self.pushButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
# #         self.pushButton.setObjectName("pushButton")
# #         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
# #         self.pushButton_2.setGeometry(QtCore.QRect(840, 510, 81, 31))
# #         self.pushButton_2.setObjectName("pushButton_2")

# #         # New theme toggle button
# #         self.toggle_button = QPushButton(self.centralwidget)
# #         self.toggle_button.setGeometry(QtCore.QRect(450, 10, 100, 30))
# #         self.toggle_button.setText("Dark Mode")
# #         self.toggle_button.clicked.connect(self.toggle_theme)

# #         jarvisUi.setCentralWidget(self.centralwidget)

# #         self.retranslateUi(jarvisUi)
# #         self.update_theme(self.is_dark_mode) #initial theme applied
# #         QtCore.QMetaObject.connectSlotsByName(jarvisUi)

# #     def retranslateUi(self, jarvisUi):
# #         _translate = QtCore.QCoreApplication.translate
# #         jarvisUi.setWindowTitle(_translate("jarvisUi", "MainWindow"))
# #         self.pushButton.setText(_translate("jarvisUi", "Start"))
# #         self.pushButton_2.setText(_translate("jarvisUi", "Stop"))

# #     def toggle_theme(self):
# #         self.is_dark_mode = not self.is_dark_mode
# #         if self.is_dark_mode:
# #             self.toggle_button.setText("Dark Mode")
# #         else:
# #             self.toggle_button.setText("Light Mode")
# #         self.update_theme(self.is_dark_mode)
    
# #     def update_theme(self, is_dark):

# #         if is_dark:
# #            self.theme = {
# #             "bg_color": "rgb(0, 0, 0)",
# #             "text_color": "white",
# #             "button_color": "qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))",
# #             "button_alt_color":"qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0))",
# #             "button_alt_text":"rgb(255, 0, 0)"
# #         }
# #         else:
# #            self.theme = {
# #             "bg_color": "white",
# #             "text_color": "black",
# #             "button_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #f6f6f6, stop:1 #e7e7e7)",
# #             "button_alt_color":"qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #f6f6f6, stop:1 #e7e7e7)",
# #              "button_alt_text":"black"
# #            }


# #         self.label.setStyleSheet(f"background-color: {self.theme['bg_color']};")
# #         self.textBrowser.setStyleSheet(f"background:transparent; border-radius:none; color: {self.theme['text_color']};")
# #         self.textBrowser_2.setStyleSheet(f"background:transparent; border-radius:none; color: {self.theme['text_color']};")
# #         self.pushButton.setStyleSheet(f"font: 8pt 'Segoe Print'; color: {self.theme['button_color']}")
# #         self.pushButton_2.setStyleSheet(f"font: 8pt 'Verdana';alternate-background-color: {self.theme['button_alt_color']};color: {self.theme['button_alt_text']}")

# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     jarvisUi = QMainWindow()
# #     ui = Ui_jarvisUi()
# #     ui.setupUi(jarvisUi)
# #     jarvisUi.show()
# #     sys.exit(app.exec_())


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys


# class Ui_jarvisUi(object):
#     def setupUi(self, jarvisUi):
#         jarvisUi.setObjectName("jarvisUi")
#         jarvisUi.resize(984, 572)
#         self.is_dark_mode = True  # Initialize with a dark theme
#         self.centralwidget = QtWidgets.QWidget(jarvisUi)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(-10, -10, 1021, 601))
#         self.label.setText("")
#         self.label.setScaledContents(True)
#         self.label.setObjectName("label")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(290, 330, 391, 201))
#         self.label_3.setText("")
#         self.label_3.setPixmap(QtGui.QPixmap(".\\Material/path.gif"))
#         self.label_3.setScaledContents(True)
#         self.label_3.setObjectName("label_3")
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(720, 20, 261, 221))
#         self.label_5.setText("")
#         self.label_5.setPixmap(QtGui.QPixmap(".\\Material/logo.gif"))
#         self.label_5.setScaledContents(True)
#         self.label_5.setObjectName("label_5")
#         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser.setGeometry(QtCore.QRect(0, 510, 191, 41))
#         font = QtGui.QFont()
#         font.setFamily("Sitka Subheading")
#         font.setPointSize(16)
#         self.textBrowser.setFont(font)
#         self.textBrowser.setObjectName("textBrowser")
#         self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         self.textBrowser_2.setFont(font)
#         self.textBrowser_2.setObjectName("textBrowser_2")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(10, 10, 411, 301))
#         self.label_2.setText("")
#         self.label_2.setPixmap(QtGui.QPixmap(".\\Material/new.gif"))
#         self.label_2.setScaledContents(True)
#         self.label_2.setObjectName("label_2")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(840, 510, 81, 31))
#         self.pushButton_2.setObjectName("pushButton_2")

#         # New theme toggle button
#         self.toggle_button = QPushButton(self.centralwidget)
#         self.toggle_button.setGeometry(QtCore.QRect(450, 10, 100, 30))
#         self.toggle_button.setText("Dark Mode")
#         self.toggle_button.clicked.connect(self.toggle_theme)

#         jarvisUi.setCentralWidget(self.centralwidget)

#         self.retranslateUi(jarvisUi)
#         self.update_theme(self.is_dark_mode)  # initial theme applied
#         QtCore.QMetaObject.connectSlotsByName(jarvisUi)

#     def retranslateUi(self, jarvisUi):
#         _translate = QtCore.QCoreApplication.translate
#         jarvisUi.setWindowTitle(_translate("jarvisUi", "MainWindow"))
#         self.pushButton.setText(_translate("jarvisUi", "Start"))
#         self.pushButton_2.setText(_translate("jarvisUi", "Stop"))

#     def toggle_theme(self):
#         self.is_dark_mode = not self.is_dark_mode
#         if self.is_dark_mode:
#             self.toggle_button.setText("Dark Mode")
#         else:
#             self.toggle_button.setText("Light Mode")
#         self.update_theme(self.is_dark_mode)

#     def update_theme(self, is_dark):
#         if is_dark:
#             self.theme = {
#                 "bg_color": "rgb(0, 0, 0)",  # Black for the background
#                 "text_color": "lime",  # Neon green for text
#                 "button_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 lime, stop:1 yellow)",  # Neon green-yellow button
#                 "button_alt_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 cyan, stop:1 magenta)",  # Neon cyan-magenta button
#                 "button_alt_text":"white"
#             }
#         else:
#             self.theme = {
#                 "bg_color": "white",  # White background
#                 "text_color": "navy",  # Navy blue text
#                 "button_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightblue, stop:1 white)", #light blue to white button gradient
#                 "button_alt_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightblue, stop:1 white)", #light blue to white alt button gradient
#                 "button_alt_text":"black" # alt button text
#             }

#         self.label.setStyleSheet(f"background-color: {self.theme['bg_color']};")
#         self.textBrowser.setStyleSheet(
#             f"background:transparent; border-radius:none; color: {self.theme['text_color']};"
#         )
#         self.textBrowser_2.setStyleSheet(
#             f"background:transparent; border-radius:none; color: {self.theme['text_color']};"
#         )
#         self.pushButton.setStyleSheet(
#             f"font: 8pt 'Segoe Print'; color: {self.theme['text_color']}; background-color: {self.theme['button_color']}"
#         )
#         self.pushButton_2.setStyleSheet(
#             f"font: 8pt 'Verdana';alternate-background-color: {self.theme['button_alt_color']};color: {self.theme['button_alt_text']};"
#         )


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     jarvisUi = QMainWindow()
#     ui = Ui_jarvisUi()
#     ui.setupUi(jarvisUi)
#     jarvisUi.show()
#     sys.exit(app.exec_())



# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys


# class Ui_jarvisUi(object):
#     def setupUi(self, jarvisUi):
#         jarvisUi.setObjectName("jarvisUi")
#         jarvisUi.resize(984, 572)
#         self.is_dark_mode = True  # Initialize with a dark theme
#         self.centralwidget = QtWidgets.QWidget(jarvisUi)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(-10, -10, 1021, 601))
#         self.label.setText("")
#         self.label.setScaledContents(True)
#         self.label.setObjectName("label")
#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(290, 330, 391, 201))
#         self.label_3.setText("")
#         self.label_3.setPixmap(QtGui.QPixmap(".\\Material/path.gif"))
#         self.label_3.setScaledContents(True)
#         self.label_3.setObjectName("label_3")
#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(720, 20, 261, 221))
#         self.label_5.setText("")
#         self.label_5.setPixmap(QtGui.QPixmap(".\\Material/logo.gif"))
#         self.label_5.setScaledContents(True)
#         self.label_5.setObjectName("label_5")
#         self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser.setGeometry(QtCore.QRect(0, 510, 191, 41))
#         font = QtGui.QFont()
#         font.setFamily("Sitka Subheading")
#         font.setPointSize(16)
#         self.textBrowser.setFont(font)
#         self.textBrowser.setObjectName("textBrowser")
#         self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
#         self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
#         font = QtGui.QFont()
#         font.setPointSize(16)
#         self.textBrowser_2.setFont(font)
#         self.textBrowser_2.setObjectName("textBrowser_2")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(10, 10, 411, 301))
#         self.label_2.setText("")
#         self.label_2.setPixmap(QtGui.QPixmap(".\\Material/new.gif"))
#         self.label_2.setScaledContents(True)
#         self.label_2.setObjectName("label_2")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(840, 510, 81, 31))
#         self.pushButton_2.setObjectName("pushButton_2")

#         # New theme toggle button
#         self.toggle_button = QPushButton(self.centralwidget)
#         self.toggle_button.setGeometry(QtCore.QRect(450, 10, 100, 30))
#         self.toggle_button.setText("Dark Mode")
#         self.toggle_button.clicked.connect(self.toggle_theme)

#         jarvisUi.setCentralWidget(self.centralwidget)

#         self.retranslateUi(jarvisUi)
#         self.update_theme(self.is_dark_mode)  # initial theme applied
#         QtCore.QMetaObject.connectSlotsByName(jarvisUi)

#     def retranslateUi(self, jarvisUi):
#         _translate = QtCore.QCoreApplication.translate
#         jarvisUi.setWindowTitle(_translate("jarvisUi", "MainWindow"))
#         self.pushButton.setText(_translate("jarvisUi", "Start"))
#         self.pushButton_2.setText(_translate("jarvisUi", "Stop"))

#     def toggle_theme(self):
#         self.is_dark_mode = not self.is_dark_mode
#         if self.is_dark_mode:
#             self.toggle_button.setText("Dark Mode")
#         else:
#             self.toggle_button.setText("Light Mode")
#         self.update_theme(self.is_dark_mode)

#     def update_theme(self, is_dark):
#         if is_dark:
#             self.theme = {
#                 "bg_color": "rgb(0, 0, 0)",  # Black for the background
#                 "text_color": "lime",  # Neon green for text
#                 "button_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 lime, stop:1 yellow)",  # Neon green-yellow button
#                 "button_alt_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 cyan, stop:1 magenta)",  # Neon cyan-magenta button
#                 "button_alt_text":"white",
#                 "start_button_color": "green", # Start button color
#                 "stop_button_color":"red" # Stop button color
#             }
#         else:
#             self.theme = {
#                 "bg_color": "white",  # White background
#                 "text_color": "navy",  # Navy blue text
#                 "button_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightblue, stop:1 white)", #light blue to white button gradient
#                 "button_alt_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightblue, stop:1 white)", #light blue to white alt button gradient
#                 "button_alt_text":"black", # alt button text
#                 "start_button_color": "darkgreen",
#                 "stop_button_color":"darkred"
#             }

#         self.label.setStyleSheet(f"background-color: {self.theme['bg_color']};")
#         self.textBrowser.setStyleSheet(
#             f"background:transparent; border-radius:none; color: {self.theme['text_color']};"
#         )
#         self.textBrowser_2.setStyleSheet(
#             f"background:transparent; border-radius:none; color: {self.theme['text_color']};"
#         )
#         self.pushButton.setStyleSheet(
#             f"font: 8pt 'Segoe Print'; color: {self.theme['text_color']}; background-color: {self.theme['button_color']}"
#         )
#         self.pushButton_2.setStyleSheet(
#             f"font: 8pt 'Verdana';alternate-background-color: {self.theme['button_alt_color']};color: {self.theme['button_alt_text']};"
#         )
#         self.pushButton.setStyleSheet(f"background-color: {self.theme['start_button_color']}; font: 8pt 'Segoe Print';color:{self.theme['text_color']}")
#         self.pushButton_2.setStyleSheet(f"background-color: {self.theme['stop_button_color']}; font: 8pt 'Verdana'; color:white")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     jarvisUi = QMainWindow()
#     ui = Ui_jarvisUi()
#     ui.setupUi(jarvisUi)
#     jarvisUi.show()
#     sys.exit(app.exec_())




from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class Ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(984, 572)
        self.is_dark_mode = True  # Initialize with a dark theme
        self.centralwidget = QtWidgets.QWidget(jarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1021, 601))
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
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 411, 301))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\Material/new.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 510, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        # New theme toggle button
        self.toggle_button = QPushButton(self.centralwidget)
        self.toggle_button.setGeometry(QtCore.QRect(450, 10, 100, 30))
        self.toggle_button.setText("Dark Mode")
        self.toggle_button.clicked.connect(self.toggle_theme)

        jarvisUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisUi)
        self.update_theme(self.is_dark_mode)  # initial theme applied
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)

    def retranslateUi(self, jarvisUi):
        _translate = QtCore.QCoreApplication.translate
        jarvisUi.setWindowTitle(_translate("jarvisUi", "MainWindow"))
        self.pushButton.setText(_translate("jarvisUi", "Start"))
        self.pushButton_2.setText(_translate("jarvisUi", "Stop"))

    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        if self.is_dark_mode:
            self.toggle_button.setText("Dark Mode")
        else:
            self.toggle_button.setText("Light Mode")
        self.update_theme(self.is_dark_mode)

    def update_theme(self, is_dark):
        if is_dark:
             self.theme = {
                "bg_color": "qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 #1e002a, stop:0.5 #0d0015,stop:1 #19002b)", # dark purple to dark to light purple
                "text_color": "lime",  # Neon green for text
                "button_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 cyan, stop:1 lime)",  # Neon green-yellow button
                "button_alt_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 magenta, stop:1 yellow)",  # Neon cyan-magenta button
                "button_alt_text":"white",
                "start_button_color": "green", # Start button color
                "stop_button_color":"red" # Stop button color
            }
        else:
            self.theme = {
                "bg_color": "white",  # White background
                "text_color": "navy",  # Navy blue text
                "button_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightblue, stop:1 white)", #light blue to white button gradient
                "button_alt_color": "qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightblue, stop:1 white)", #light blue to white alt button gradient
                "button_alt_text":"black", # alt button text
                "start_button_color": "darkgreen",
                "stop_button_color":"darkred"
            }

        self.label.setStyleSheet(f"background-color: {self.theme['bg_color']};")
        self.textBrowser.setStyleSheet(
            f"background:transparent; border-radius:none; color: {self.theme['text_color']};"
        )
        self.textBrowser_2.setStyleSheet(
            f"background:transparent; border-radius:none; color: {self.theme['text_color']};"
        )
        self.pushButton.setStyleSheet(
            f"font: 8pt 'Segoe Print'; color: {self.theme['text_color']}; background-color: {self.theme['button_color']}"
        )
        self.pushButton_2.setStyleSheet(
            f"font: 8pt 'Verdana';alternate-background-color: {self.theme['button_alt_color']};color: {self.theme['button_alt_text']};"
        )
        self.pushButton.setStyleSheet(f"background-color: {self.theme['start_button_color']}; font: 8pt 'Segoe Print';color:{self.theme['text_color']}")
        self.pushButton_2.setStyleSheet(f"background-color: {self.theme['stop_button_color']}; font: 8pt 'Verdana'; color:white")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvisUi = QMainWindow()
    ui = Ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())