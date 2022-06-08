# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zia1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bgimg = QtWidgets.QLabel(self.centralwidget)
        self.bgimg.setGeometry(QtCore.QRect(0, -210, 1621, 1001))
        self.bgimg.setText("")
        self.bgimg.setPixmap(QtGui.QPixmap('UIassets\\bg3.jpg'))
        self.bgimg.setScaledContents(True)
        self.bgimg.setObjectName("bgimg")
        self.maingif = QtWidgets.QLabel(self.centralwidget)
        self.maingif.setGeometry(QtCore.QRect(140, 50, 611, 471))
        self.maingif.setText("")
        self.maingif.setPixmap(QtGui.QPixmap("UIassets\\wave-sound-unscreen.gif"))
        self.maingif.setScaledContents(True)
        self.maingif.setObjectName("maingif")
        self.zia = QtWidgets.QTextBrowser(self.centralwidget)
        self.zia.setGeometry(QtCore.QRect(350, 240, 181, 101))
        self.zia.setStyleSheet("background-color:transparent;\n"
"border-radius:none;")
        self.zia.setObjectName("zia")
        self.micgif = QtWidgets.QLabel(self.centralwidget)
        self.micgif.setGeometry(QtCore.QRect(290, 430, 321, 211))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        self.micgif.setFont(font)
        self.micgif.setText("")
        self.micgif.setPixmap(QtGui.QPixmap("UIassets\\mic1-unscreen.gif"))
        self.micgif.setScaledContents(True)
        self.micgif.setObjectName("micgif")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(692, 540, 181, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"border:3px solid rgb(79, 112, 237); \n"
"border-radius:10px;\n"
"color:rgb(159, 159, 159);\n"
"padding-left:40px;\n"
"padding-bottom:5px;\n"
"    background-color: rgb(0, 28, 49)\n"
"\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.start_push = QtWidgets.QPushButton(self.centralwidget)
        self.start_push.setGeometry(QtCore.QRect(420, 520, 61, 23))
        self.start_push.setStyleSheet("background-color:transparent;\n"
"border-radius:none;")
        self.start_push.setText("")
        self.start_push.setObjectName("start_push")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.zia.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">ZIA</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
