# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tugas_latihan.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 900)
        MainWindow.setMinimumSize(QtCore.QSize(800, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 780, 850))
        self.frame.setMinimumSize(QtCore.QSize(780, 850))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(249, 136, 102);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setMinimumSize(QtCore.QSize(700, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.frame_5.setFont(font)
        self.frame_5.setStyleSheet("background-color: rgb(249, 136, 102);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMinimumSize(QtCore.QSize(250, 50))
        self.label.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 66, 14);")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_8 = QtWidgets.QFrame(self.frame_2)
        self.frame_8.setMinimumSize(QtCore.QSize(700, 60))
        self.frame_8.setStyleSheet("background-color: rgb(249, 136, 102);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        self.label_8.setMinimumSize(QtCore.QSize(250, 50))
        self.label_8.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 66, 14);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addWidget(self.frame_8)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(700, 60))
        self.frame_6.setStyleSheet("background-color: rgb(249, 136, 102);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.frame_6)
        self.label_9.setMinimumSize(QtCore.QSize(250, 50))
        self.label_9.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 66, 14);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_9 = QtWidgets.QFrame(self.frame_2)
        self.frame_9.setMinimumSize(QtCore.QSize(700, 60))
        self.frame_9.setStyleSheet("background-color: rgb(249, 136, 102);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        self.label_10.setMinimumSize(QtCore.QSize(250, 50))
        self.label_10.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 66, 14);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setMinimumSize(QtCore.QSize(700, 60))
        self.frame_7.setStyleSheet("background-color: rgb(249, 136, 102);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.frame_7)
        self.label_11.setMinimumSize(QtCore.QSize(250, 50))
        self.label_11.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 66, 14);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_10 = QtWidgets.QFrame(self.frame_2)
        self.frame_10.setMinimumSize(QtCore.QSize(700, 60))
        self.frame_10.setStyleSheet("background-color: rgb(249, 136, 102);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_13 = QtWidgets.QLabel(self.frame_10)
        self.label_13.setMinimumSize(QtCore.QSize(250, 50))
        self.label_13.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 66, 14);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setMaxLength(100)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_2)
        self.frame_11.setMinimumSize(QtCore.QSize(700, 60))
        self.frame_11.setStyleSheet("background-color: rgb(249, 136, 102);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        self.label_12.setMinimumSize(QtCore.QSize(250, 50))
        self.label_12.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(400, 50))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 66, 14);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_8.addWidget(self.lineEdit_7)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(700, 70))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color: rgb(89, 130, 52);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(174, 189, 56);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(174, 189, 56);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(174, 189, 56);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(174, 189, 56);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NIM"))
        self.label_8.setText(_translate("MainWindow", "Nama"))
        self.label_9.setText(_translate("MainWindow", "Kelas"))
        self.label_10.setText(_translate("MainWindow", "Tempat Lahir"))
        self.label_11.setText(_translate("MainWindow", "Tanggal Lahir"))
        self.label_13.setText(_translate("MainWindow", "Alamat"))
        self.label_12.setText(_translate("MainWindow", "Telepon"))
        self.pushButton.setText(_translate("MainWindow", "SIMPAN"))
        self.pushButton_2.setText(_translate("MainWindow", "EDIT"))
        self.pushButton_3.setText(_translate("MainWindow", "HAPUS"))
        self.pushButton_4.setText(_translate("MainWindow", "BATAL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())