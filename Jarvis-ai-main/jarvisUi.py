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



# # new design for buttons and frames not working

# from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_jarvisUi(object):
#     def setupUi(self, jarvisUi):
#         jarvisUi.setObjectName("jarvisUi")
#         jarvisUi.resize(984, 572)
#         self.centralwidget = QtWidgets.QWidget(jarvisUi)
#         self.centralwidget.setObjectName("centralwidget")

#         # Main background label
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(0, 0, 984, 572))
#         self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
#         self.label.setText("")
#         self.label.setObjectName("label")

#         # Top-left frame
#         self.top_left_frame = QtWidgets.QFrame(self.centralwidget)
#         self.top_left_frame.setGeometry(QtCore.QRect(50, 50, 300, 200))
#         self.top_left_frame.setStyleSheet("background-color: rgb(30, 30, 30);")
#         self.top_left_frame.setObjectName("top_left_frame")

#         # Top-right frame
#         self.top_right_frame = QtWidgets.QFrame(self.centralwidget)
#         self.top_right_frame.setGeometry(QtCore.QRect(600, 50, 300, 200))
#         self.top_right_frame.setStyleSheet("background-color: rgb(30, 30, 30);")
#         self.top_right_frame.setObjectName("top_right_frame")

#         # Bottom frame
#         self.bottom_frame = QtWidgets.QFrame(self.centralwidget)
#         self.bottom_frame.setGeometry(QtCore.QRect(200, 300, 600, 200))
#         self.bottom_frame.setStyleSheet("background-color: rgb(30, 30, 30);")
#         self.bottom_frame.setObjectName("bottom_frame")

#         # Start Button
#         self.start_button = QtWidgets.QPushButton(self.centralwidget)
#         self.start_button.setGeometry(QtCore.QRect(750, 520, 100, 40))
#         self.start_button.setStyleSheet("background-color: rgb(0, 200, 0); color: white; font-size: 16px; border-radius: 10px;")
#         self.start_button.setText("Start")
#         self.start_button.setObjectName("start_button")

#         # Stop Button
#         self.stop_button = QtWidgets.QPushButton(self.centralwidget)
#         self.stop_button.setGeometry(QtCore.QRect(870, 520, 100, 40))
#         self.stop_button.setStyleSheet("background-color: rgb(200, 0, 0); color: white; font-size: 16px; border-radius: 10px;")
#         self.stop_button.setText("Stop")
#         self.stop_button.setObjectName("stop_button")

#         jarvisUi.setCentralWidget(self.centralwidget)
#         self.retranslateUi(jarvisUi)
#         QtCore.QMetaObject.connectSlotsByName(jarvisUi)

#     def retranslateUi(self, jarvisUi):
#         _translate = QtCore.QCoreApplication.translate
#         jarvisUi.setWindowTitle(_translate("jarvisUi", "Jarvis UI"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     jarvisUi = QtWidgets.QMainWindow()
#     ui = Ui_jarvisUi()
#     ui.setupUi(jarvisUi)
#     jarvisUi.show()
#     sys.exit(app.exec_())
