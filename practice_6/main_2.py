from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 640)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(140, 200, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(140, 300, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(140, 410, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 90, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 500, 91, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 540, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "Файл"))
        self.radioButton_2.setText(_translate("Form", "Интернет"))
        self.radioButton_3.setText(_translate("Form", "Камера"))
        self.label.setText(_translate("Form", "Тип источника видео"))
        self.label_2.setText(_translate("Form", "Путь к видео"))
        self.pushButton.setText(_translate("Form", "Выбрать"))