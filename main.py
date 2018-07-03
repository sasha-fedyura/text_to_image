# -*- coding: utf-8 -*-

import os
import socket
import time
import crypt_text
import decrypt_text
import list_creator
QT_DEBUG_PLUGINS=1
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
QT_QPA_PLATFORM_PLUGIN_PATH="\platforms"

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 219)
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Ukraine))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setEnabled(False)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.ip_key = QtWidgets.QCheckBox(Form)
        self.ip_key.setEnabled(False)
        self.ip_key.setObjectName("ip_key")
        self.gridLayout.addWidget(self.ip_key, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(False)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.radio_decrypt = QtWidgets.QRadioButton(Form)
        self.radio_decrypt.setObjectName("radio_decrypt")
        self.gridLayout.addWidget(self.radio_decrypt, 0, 2, 1, 1)
        self.inp_list_numb = QtWidgets.QSpinBox(Form)
        self.inp_list_numb.setEnabled(False)
        self.inp_list_numb.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inp_list_numb.setMaximum(255)
        self.inp_list_numb.setObjectName("inp_list_numb")
        self.gridLayout.addWidget(self.inp_list_numb, 3, 1, 1, 2)
        self.auto_ip = QtWidgets.QCheckBox(Form)
        self.auto_ip.setEnabled(False)
        self.auto_ip.setCheckable(True)
        self.auto_ip.setObjectName("auto_ip")
        self.gridLayout.addWidget(self.auto_ip, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setEnabled(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.key = QtWidgets.QLineEdit(Form)
        self.key.setEnabled(False)
        self.key.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.key.setObjectName("key")
        self.gridLayout.addWidget(self.key, 2, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setEnabled(False)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.color_step = QtWidgets.QSpinBox(Form)
        self.color_step.setEnabled(False)
        self.color_step.setMaximum(16)
        self.color_step.setObjectName("color_step")
        self.gridLayout.addWidget(self.color_step, 6, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setEnabled(False)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 10, 0, 1, 1)
        self.path = QtWidgets.QLineEdit(Form)
        self.path.setEnabled(False)
        self.path.setObjectName("path")
        self.gridLayout.addWidget(self.path, 1, 1, 1, 6)
        self.run = QtWidgets.QPushButton(Form)
        self.run.setEnabled(False)
        self.run.setObjectName("run")
        self.gridLayout.addWidget(self.run, 10, 7, 1, 1)
        self.ip = QtWidgets.QLineEdit(Form)
        self.ip.setEnabled(False)
        self.ip.setObjectName("ip")
        self.gridLayout.addWidget(self.ip, 3, 5, 1, 3)
        self.dict_step = QtWidgets.QSpinBox(Form)
        self.dict_step.setEnabled(False)
        self.dict_step.setMaximum(65535)
        self.dict_step.setObjectName("dict_step")
        self.gridLayout.addWidget(self.dict_step, 10, 1, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setEnabled(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 10, 3, 1, 4)
        self.open_file = QtWidgets.QPushButton(Form)
        self.open_file.setEnabled(False)
        self.open_file.setObjectName("open_file")
        self.gridLayout.addWidget(self.open_file, 1, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setEnabled(False)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 4, 1, 1)
        self.radio_crypt = QtWidgets.QRadioButton(Form)
        self.radio_crypt.setObjectName("radio_crypt")
        self.gridLayout.addWidget(self.radio_crypt, 0, 0, 1, 2)
        self.label.setBuddy(self.path)
        self.label_2.setBuddy(self.key)
        self.label_3.setBuddy(self.inp_list_numb)
        self.label_4.setBuddy(self.ip)

        self.retranslateUi(Form)
        self.run.clicked.connect(self.run_but)
        self.open_file.clicked.connect(self.open_file_but)
        self.radio_crypt.clicked['bool'].connect(self.path.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.key.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.inp_list_numb.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.ip.setDisabled)
        self.radio_crypt.clicked['bool'].connect(self.ip_key.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.run.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.open_file.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.auto_ip.setDisabled)
        self.radio_crypt.clicked['bool'].connect(self.label_4.setDisabled)
        self.radio_decrypt.clicked['bool'].connect(self.path.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.open_file.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.path.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.key.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.inp_list_numb.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.ip_key.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.auto_ip.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.ip.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.run.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.label_4.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.label.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.label_2.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.label_3.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.label.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.label_2.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.label_3.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.label_6.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.color_step.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.color_step.setDisabled)
        self.radio_crypt.clicked['bool'].connect(self.label_6.setDisabled)
        self.radio_crypt.clicked['bool'].connect(self.label_6.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.color_step.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.color_step.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.label_6.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.progressBar.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.progressBar.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.label_5.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.dict_step.setEnabled)
        self.radio_crypt.clicked['bool'].connect(self.label_5.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.label_5.setEnabled)
        self.radio_decrypt.clicked['bool'].connect(self.dict_step.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.radio_crypt, self.radio_decrypt)
        Form.setTabOrder(self.radio_decrypt, self.path)
        Form.setTabOrder(self.path, self.key)
        Form.setTabOrder(self.key, self.inp_list_numb)
        Form.setTabOrder(self.inp_list_numb, self.ip_key)
        Form.setTabOrder(self.ip_key, self.auto_ip)
        Form.setTabOrder(self.auto_ip, self.open_file)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crypt"))
        self.label_6.setText(_translate("Form", "CStep:"))
        self.ip_key.setText(_translate("Form", "Binding with IP?"))
        self.label.setText(_translate("Form", "&File path:"))
        self.radio_decrypt.setText(_translate("Form", "&Decrypt"))
        self.auto_ip.setText(_translate("Form", "Auto IP"))
        self.label_2.setText(_translate("Form", "&Key:"))
        self.key.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "&CPS:"))
        self.label_5.setText(_translate("Form", "DStep"))
        self.run.setText(_translate("Form", "Run"))
        self.open_file.setText(_translate("Form", "Open"))
        self.label_4.setText(_translate("Form", "&IP:"))
        self.radio_crypt.setText(_translate("Form", "&Crypt"))

    def open_file_but(self):
        self.fname = QFileDialog.getOpenFileName()
        self.path.setText(self.fname[0])

    def run_but(self):
        self.progressBar.setValue(0)
        def del_list():
            with open("unicode_list.py", 'w'):
                pass

        if self.radio_crypt.isChecked():
            ip_key = self.ip_key.checkState()
            if ip_key:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("gmail.com", 80))
                ip = s.getsockname()[0]
                s.close()
            else:
                ip = ""

            key = self.key.text() + ip or "0" + ip
            step = self.color_step.value() if 0 < self.color_step.value() < 17 else 2
            inp_list_numb = self.inp_list_numb.value()
            list_cr = inp_list_numb if 0 < inp_list_numb < 25 else 5
            list_creator.list_creator(list_cr, self.dict_step.value(), 1)

            path = self.path.text()
            file_open = open(path, "r")
            text = file_open.read()
            self.progressBar.setValue(25)
            crypt_text.crypt_text(text, key, list_cr, step)
            self.progressBar.setValue(85)
            del_list()
            self.progressBar.setValue(100)
            

        elif self.radio_decrypt.isChecked():
            ip_key = self.ip_key.checkState()
            ip_type = self.auto_ip.isChecked()
            if ip_key:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("gmail.com", 80))
                ip = s.getsockname()[0] if type_ip else self.ip.text()
                s.close()
            else:
                ip = ""

            key = self.key.text() + ip or "0" + ip
            step = self.color_step.value() if 0 < self.color_step.value() < 17 else 2
            inp_list_numb = self.inp_list_numb.value()
            list_cr = int(inp_list_numb) if 0 < int(inp_list_numb) < 256 else 5
            list_creator.list_creator(list_cr, self.dict_step.value(), 0)

            path = self.path.text()
            self.progressBar.setValue(25)
            decrypt_text.decrypt_text(path, key, step)
            self.progressBar.setValue(85)
            del_list()
            self.progressBar.setValue(100)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())