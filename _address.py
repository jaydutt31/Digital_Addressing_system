# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'address.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(793, 586)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(220, 110, 561, 451))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(40, 130, 491, 251))
        self.frame_2.setStyleSheet("\n"
"background-color: rgb(224, 255, 249);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.splitter_5 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_5.setGeometry(QtCore.QRect(10, 10, 5, 231))
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(120, 30, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.address = QtWidgets.QLineEdit(self.frame_2)
        self.address.setEnabled(False)
        self.address.setGeometry(QtCore.QRect(110, 120, 281, 41))
        self.address.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.address.setObjectName("address")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(20, 250, 191, 201))
        self.splitter.setAutoFillBackground(True)
        self.splitter.setFrameShape(QtWidgets.QFrame.Box)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pincode = QtWidgets.QPushButton(self.splitter)
        self.pincode.setObjectName("pincode")
        self.city = QtWidgets.QPushButton(self.splitter)
        self.city.setObjectName("city")
        self.state = QtWidgets.QPushButton(self.splitter)
        self.state.setObjectName("state")
        self.postoffice = QtWidgets.QPushButton(self.splitter)
        self.postoffice.setObjectName("postoffice")
        self.splitter_2 = QtWidgets.QSplitter(Dialog)
        self.splitter_2.setGeometry(QtCore.QRect(220, 40, 551, 51))
        self.splitter_2.setAutoFillBackground(True)
        self.splitter_2.setFrameShape(QtWidgets.QFrame.Box)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.home = QtWidgets.QPushButton(self.splitter_2)
        self.home.setObjectName("home")
        self.database = QtWidgets.QPushButton(self.splitter_2)
        self.database.setObjectName("database")
        self.about = QtWidgets.QPushButton(self.splitter_2)
        self.about.setObjectName("about")
        self.help = QtWidgets.QPushButton(self.splitter_2)
        self.help.setObjectName("help")
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(10, 10, 201, 181))
        self.logo.setAutoFillBackground(False)
        self.logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignJustify)
        self.logo.setWordWrap(True)
        self.logo.setIndent(0)
        self.logo.setObjectName("logo")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "DIGITAL ADDRESSEE SYSTEM"))
        self.label.setText(_translate("Dialog", "YOUR E-PIN IS:"))
        self.pincode.setText(_translate("Dialog", "PINCODE"))
        self.city.setText(_translate("Dialog", "CITY "))
        self.state.setText(_translate("Dialog", "STATE"))
        self.postoffice.setText(_translate("Dialog", "POST-OFFICE"))
        self.home.setText(_translate("Dialog", "HOME"))
        self.database.setText(_translate("Dialog", "DATABASE"))
        self.about.setText(_translate("Dialog", "ABOUT"))
        self.help.setText(_translate("Dialog", "HELP"))
        self.logo.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/newPrefix/LOG.png\"/></p></body></html>"))
import img_rc