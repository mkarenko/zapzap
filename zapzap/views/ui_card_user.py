from gettext import gettext as _
# Form implementation generated from reading ui file './zapzap/ui/ui_card_user.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CardUser(object):
    def setupUi(self, CardUser):
        CardUser.setObjectName("CardUser")
        CardUser.resize(385, 98)
        CardUser.setWindowTitle("")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(CardUser)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_carduser = QtWidgets.QFrame(parent=CardUser)
        self.frame_carduser.setStyleSheet("")
        self.frame_carduser.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_carduser.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_carduser.setObjectName("frame_carduser")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_carduser)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QPushButton(parent=self.frame_carduser)
        self.icon.setMinimumSize(QtCore.QSize(46, 46))
        self.icon.setMaximumSize(QtCore.QSize(46, 46))
        self.icon.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"                border: none;\n"
"                border-radius: none;\n"
"                qproperty-flat: true;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"                border: 1px solid #D0D4D8;\n"
"                border-radius: 6px;\n"
"                \n"
"                \n"
"            }")
        self.icon.setText("")
        self.icon.setIconSize(QtCore.QSize(46, 46))
        self.icon.setFlat(True)
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.disable = QtWidgets.QPushButton(parent=self.frame_carduser)
        self.disable.setStyleSheet("")
        self.disable.setCheckable(True)
        self.disable.setObjectName("disable")
        self.gridLayout.addWidget(self.disable, 1, 1, 1, 1)
        self.silence = QtWidgets.QPushButton(parent=self.frame_carduser)
        self.silence.setStyleSheet("")
        self.silence.setCheckable(True)
        self.silence.setObjectName("silence")
        self.gridLayout.addWidget(self.silence, 1, 0, 1, 1)
        self.delete = QtWidgets.QPushButton(parent=self.frame_carduser)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete.sizePolicy().hasHeightForWidth())
        self.delete.setSizePolicy(sizePolicy)
        self.delete.setStyleSheet("")
        self.delete.setObjectName("delete")
        self.gridLayout.addWidget(self.delete, 1, 2, 1, 1)
        self.name = QtWidgets.QLineEdit(parent=self.frame_carduser)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.frame_carduser)

        self.retranslateUi(CardUser)
        QtCore.QMetaObject.connectSlotsByName(CardUser)

    def retranslateUi(self, CardUser):
        
        self.icon.setToolTip(_("Click to generate new colors for the icon"))
        self.disable.setToolTip(_("Temporarily disable"))
        self.disable.setText(_("Disable"))
        self.silence.setToolTip(_("Silences the notifications"))
        self.silence.setText(_("Do not disturb"))
        self.delete.setToolTip(_("Delete permanently"))
        self.delete.setText(_("Delete"))
        self.name.setPlaceholderText(_("Enter the user name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardUser = QtWidgets.QWidget()
    ui = Ui_CardUser()
    ui.setupUi(CardUser)
    CardUser.show()
    sys.exit(app.exec())
