# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsubscriptiondialog.ui'
#
# Created: Sat Nov 02 04:23:29 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NewSubscriptionDialog(object):
    def setupUi(self, NewSubscriptionDialog):
        NewSubscriptionDialog.setObjectName(_fromUtf8("NewSubscriptionDialog"))
        NewSubscriptionDialog.resize(482, 186)
        self.formLayout = QtGui.QFormLayout(NewSubscriptionDialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(NewSubscriptionDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.label_2)
        self.newsubscriptionlabel = QtGui.QLineEdit(NewSubscriptionDialog)
        self.newsubscriptionlabel.setObjectName(_fromUtf8("newsubscriptionlabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.newsubscriptionlabel)
        self.label = QtGui.QLabel(NewSubscriptionDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label)
        spacerItem = QtGui.QSpacerItem(302, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.FieldRole, spacerItem)
        self.lineEditSubscriptionAddress = QtGui.QLineEdit(NewSubscriptionDialog)
        self.lineEditSubscriptionAddress.setObjectName(_fromUtf8("lineEditSubscriptionAddress"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.lineEditSubscriptionAddress)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtGui.QFormLayout.FieldRole, spacerItem1)
        self.labelSubscriptionAddressCheck = QtGui.QLabel(NewSubscriptionDialog)
        self.labelSubscriptionAddressCheck.setText(_fromUtf8(""))
        self.labelSubscriptionAddressCheck.setWordWrap(True)
        self.labelSubscriptionAddressCheck.setObjectName(_fromUtf8("labelSubscriptionAddressCheck"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.SpanningRole, self.labelSubscriptionAddressCheck)
        self.buttonBox = QtGui.QDialogButtonBox(NewSubscriptionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.buttonBox)

        self.retranslateUi(NewSubscriptionDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), NewSubscriptionDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), NewSubscriptionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewSubscriptionDialog)

    def retranslateUi(self, NewSubscriptionDialog):
        NewSubscriptionDialog.setWindowTitle(_translate("NewSubscriptionDialog", "Add new entry", None))
        self.label_2.setText(_translate("NewSubscriptionDialog", "Label", None))
        self.label.setText(_translate("NewSubscriptionDialog", "Address", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    NewSubscriptionDialog = QtGui.QDialog()
    ui = Ui_NewSubscriptionDialog()
    ui.setupUi(NewSubscriptionDialog)
    NewSubscriptionDialog.show()
    sys.exit(app.exec_())

