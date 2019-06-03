# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1236, 669)
        MainWindow.setStyleSheet("background-color: rgb(135, 135, 135);")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(5, 0))
        self.frame_4.setStyleSheet("background-color: rgb(135, 135, 135)\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout.addWidget(self.frame_4, 1, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setStyleSheet("background-color: rgb(135, 135, 135);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doButt = QtWidgets.QPushButton(self.frame)
        self.doButt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31);\n"
"font: bold 16px;")
        self.doButt.setObjectName("doButt")
        self.gridLayout_3.addWidget(self.doButt, 3, 0, 1, 1)
        self.lockButt = QtWidgets.QPushButton(self.frame)
        self.lockButt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31);\n"
"font: bold 16px;")
        self.lockButt.setObjectName("lockButt")
        self.gridLayout_3.addWidget(self.lockButt, 3, 1, 1, 1)
        self.clearButt = QtWidgets.QPushButton(self.frame)
        self.clearButt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31);\n"
"font: bold 16px;")
        self.clearButt.setObjectName("clearButt")
        self.gridLayout_3.addWidget(self.clearButt, 3, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet("background-color: rgb(135, 135, 135);\n"
"font: bold 14px;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setContentsMargins(10, -1, 10, -1)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setStyleSheet("font: bold 14px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.delayCHB = QtWidgets.QCheckBox(self.groupBox_3)
        self.delayCHB.setStyleSheet("font: bold 14px;")
        self.delayCHB.setObjectName("delayCHB")
        self.gridLayout_2.addWidget(self.delayCHB, 7, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.xcrd = QtWidgets.QSpinBox(self.frame_2)
        self.xcrd.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 4px;")
        self.xcrd.setMinimum(-1000)
        self.xcrd.setMaximum(1000)
        self.xcrd.setObjectName("xcrd")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.xcrd)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.ycrd = QtWidgets.QSpinBox(self.frame_2)
        self.ycrd.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 4px;")
        self.ycrd.setMinimum(-1000)
        self.ycrd.setMaximum(1000)
        self.ycrd.setObjectName("ycrd")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ycrd)
        self.gridLayout_2.addWidget(self.frame_2, 4, 0, 1, 1)
        self.pointBox = QtWidgets.QListWidget(self.groupBox_3)
        self.pointBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: bold 16px;\n"
"border-color: black;")
        self.pointBox.setObjectName("pointBox")
        self.gridLayout_2.addWidget(self.pointBox, 2, 0, 1, 1)
        self.addPointButt = QtWidgets.QPushButton(self.groupBox_3)
        self.addPointButt.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(31, 31, 31);\n"
"font: bold 16px;")
        self.addPointButt.setObjectName("addPointButt")
        self.gridLayout_2.addWidget(self.addPointButt, 5, 0, 1, 1)
        self.colorCB = QtWidgets.QComboBox(self.groupBox_3)
        self.colorCB.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border-style: outset;\n"
"border-width: 1px;\n"
"border-color: white;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 4px;")
        self.colorCB.setObjectName("colorCB")
        self.colorCB.addItem("")
        self.colorCB.addItem("")
        self.colorCB.addItem("")
        self.gridLayout_2.addWidget(self.colorCB, 3, 0, 1, 1)
        self.drawBorderCHB = QtWidgets.QCheckBox(self.groupBox_3)
        self.drawBorderCHB.setStyleSheet("font: bold 14px;")
        self.drawBorderCHB.setObjectName("drawBorderCHB")
        self.gridLayout_2.addWidget(self.drawBorderCHB, 6, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)
        self.fillFR = QtWidgets.QFrame(self.centralwidget)
        self.fillFR.setAutoFillBackground(False)
        self.fillFR.setStyleSheet("background-color: rgb(29, 29, 29)")
        self.fillFR.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fillFR.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fillFR.setObjectName("fillFR")
        self.gridLayout.addWidget(self.fillFR, 0, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.doButt.setText(_translate("MainWindow", "Выполнить"))
        self.lockButt.setText(_translate("MainWindow", "Замкнуть"))
        self.clearButt.setText(_translate("MainWindow", "Очистить"))
        self.label.setText(_translate("MainWindow", "Введенные точки "))
        self.delayCHB.setText(_translate("MainWindow", "Выполнить задержку"))
        self.label_2.setText(_translate("MainWindow", "x"))
        self.label_3.setText(_translate("MainWindow", "y"))
        self.addPointButt.setText(_translate("MainWindow", "Добавить точку"))
        self.colorCB.setItemText(0, _translate("MainWindow", "Белый"))
        self.colorCB.setItemText(1, _translate("MainWindow", "Красный"))
        self.colorCB.setItemText(2, _translate("MainWindow", "Синий"))
        self.drawBorderCHB.setText(_translate("MainWindow", "Отрисовать границы"))

