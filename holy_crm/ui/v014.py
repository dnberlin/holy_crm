# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v013.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 536)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.console_out = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.console_out.setGeometry(QtCore.QRect(10, 10, 381, 101))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(9)
        self.console_out.setFont(font)
        self.console_out.setReadOnly(True)
        self.console_out.setObjectName("console_out")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(280, 460, 88, 34))
        self.start.setObjectName("start")
        self.sub_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sub_edit.setGeometry(QtCore.QRect(10, 170, 351, 51))
        self.sub_edit.setObjectName("sub_edit")
        self.sub = QtWidgets.QLabel(self.centralwidget)
        self.sub.setGeometry(QtCore.QRect(10, 150, 58, 18))
        self.sub.setObjectName("sub")
        self.mail_to = QtWidgets.QLabel(self.centralwidget)
        self.mail_to.setGeometry(QtCore.QRect(10, 120, 58, 18))
        self.mail_to.setObjectName("mail_to")
        self.recipient = QtWidgets.QLabel(self.centralwidget)
        self.recipient.setGeometry(QtCore.QRect(70, 120, 291, 18))
        self.recipient.setAutoFillBackground(True)
        self.recipient.setText("")
        self.recipient.setObjectName("recipient")
        self.cont = QtWidgets.QLabel(self.centralwidget)
        self.cont.setGeometry(QtCore.QRect(10, 230, 91, 18))
        self.cont.setObjectName("cont")
        self.cont_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cont_edit.setGeometry(QtCore.QRect(10, 260, 571, 191))
        self.cont_edit.setObjectName("cont_edit")
        self.send_but = QtWidgets.QPushButton(self.centralwidget)
        self.send_but.setGeometry(QtCore.QRect(380, 460, 88, 34))
        self.send_but.setObjectName("send_but")
        self.no_send_but = QtWidgets.QPushButton(self.centralwidget)
        self.no_send_but.setGeometry(QtCore.QRect(490, 460, 88, 34))
        self.no_send_but.setObjectName("no_send_but")
        self.l_cont = QtWidgets.QLabel(self.centralwidget)
        self.l_cont.setGeometry(QtCore.QRect(400, 10, 81, 18))
        self.l_cont.setObjectName("l_cont")
        self.last_contact = QtWidgets.QLabel(self.centralwidget)
        self.last_contact.setGeometry(QtCore.QRect(400, 30, 171, 201))
        self.last_contact.setText("")
        self.last_contact.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.last_contact.setWordWrap(True)
        self.last_contact.setObjectName("last_contact")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 30))
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
        self.console_out.setPlainText(_translate("MainWindow", "| |__   ___ | |_   _        ___ _ __ _ __ ___  \n"
"| \'_ \\ / _ \\| | | | |_____ / __| \'__| \'_ ` _ \\ \n"
"| | | | (_) | | |_| |_____| (__| |  | | | | | |\n"
"|_| |_|\\___/|_|\\__, |      \\___|_|  |_| |_| |_|\n"
"               |___/                      alpha"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.sub.setText(_translate("MainWindow", "Subject:"))
        self.mail_to.setText(_translate("MainWindow", "Email to:"))
        self.cont.setText(_translate("MainWindow", "Mail Content"))
        self.send_but.setText(_translate("MainWindow", "Send Mail"))
        self.no_send_but.setText(_translate("MainWindow", "Do not Send"))
        self.l_cont.setText(_translate("MainWindow", "Last Contact:"))
