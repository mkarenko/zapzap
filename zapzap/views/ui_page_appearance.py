# Form implementation generated from reading ui file './zapzap/ui/ui_page_appearance.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PageAppearance(object):
    def setupUi(self, PageAppearance):
        PageAppearance.setObjectName("PageAppearance")
        PageAppearance.resize(693, 620)
        PageAppearance.setWindowTitle("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(PageAppearance)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(parent=PageAppearance)
        self.frame.setMinimumSize(QtCore.QSize(550, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.style_groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.style_groupBox.setObjectName("style_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.style_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.theme_auto_radioButton = QtWidgets.QRadioButton(parent=self.style_groupBox)
        self.theme_auto_radioButton.setChecked(True)
        self.theme_auto_radioButton.setObjectName("theme_auto_radioButton")
        self.gridLayout.addWidget(self.theme_auto_radioButton, 0, 0, 1, 1)
        self.theme_light_radioButton = QtWidgets.QRadioButton(parent=self.style_groupBox)
        self.theme_light_radioButton.setObjectName("theme_light_radioButton")
        self.gridLayout.addWidget(self.theme_light_radioButton, 0, 1, 1, 1)
        self.theme_dark_radioButton = QtWidgets.QRadioButton(parent=self.style_groupBox)
        self.theme_dark_radioButton.setObjectName("theme_dark_radioButton")
        self.gridLayout.addWidget(self.theme_dark_radioButton, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.style_groupBox)
        self.tray_groupBox = QtWidgets.QGroupBox(parent=self.frame)
        self.tray_groupBox.setCheckable(True)
        self.tray_groupBox.setObjectName("tray_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tray_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tray_default_radioButton = QtWidgets.QRadioButton(parent=self.tray_groupBox)
        self.tray_default_radioButton.setChecked(True)
        self.tray_default_radioButton.setObjectName("tray_default_radioButton")
        self.gridLayout_2.addWidget(self.tray_default_radioButton, 0, 0, 1, 1)
        self.tray_slight_radioButton = QtWidgets.QRadioButton(parent=self.tray_groupBox)
        self.tray_slight_radioButton.setObjectName("tray_slight_radioButton")
        self.gridLayout_2.addWidget(self.tray_slight_radioButton, 0, 1, 1, 1)
        self.tray_sdark_radioButton = QtWidgets.QRadioButton(parent=self.tray_groupBox)
        self.tray_sdark_radioButton.setObjectName("tray_sdark_radioButton")
        self.gridLayout_2.addWidget(self.tray_sdark_radioButton, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.tray_groupBox)
        self.browser_sidebar = QtWidgets.QCheckBox(parent=self.frame)
        self.browser_sidebar.setChecked(True)
        self.browser_sidebar.setObjectName("browser_sidebar")
        self.verticalLayout_2.addWidget(self.browser_sidebar)
        self.mainwindow_menu = QtWidgets.QCheckBox(parent=self.frame)
        self.mainwindow_menu.setChecked(True)
        self.mainwindow_menu.setObjectName("mainwindow_menu")
        self.verticalLayout_2.addWidget(self.mainwindow_menu)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scaleLabel = QtWidgets.QLabel(parent=self.frame)
        self.scaleLabel.setObjectName("scaleLabel")
        self.gridLayout_3.addWidget(self.scaleLabel, 0, 0, 1, 1)
        self.scaleComboBox = QtWidgets.QComboBox(parent=self.frame)
        self.scaleComboBox.setObjectName("scaleComboBox")
        self.scaleComboBox.addItem("")
        self.scaleComboBox.addItem("")
        self.scaleComboBox.addItem("")
        self.scaleComboBox.addItem("")
        self.scaleComboBox.addItem("")
        self.gridLayout_3.addWidget(self.scaleComboBox, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 295, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)

        self.retranslateUi(PageAppearance)
        QtCore.QMetaObject.connectSlotsByName(PageAppearance)

    def retranslateUi(self, PageAppearance):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("PageAppearance", "Appearance"))
        self.style_groupBox.setTitle(_translate("PageAppearance", "Style"))
        self.theme_auto_radioButton.setText(_translate("PageAppearance", "Adaptive"))
        self.theme_light_radioButton.setText(_translate("PageAppearance", "Light"))
        self.theme_dark_radioButton.setText(_translate("PageAppearance", "Dark"))
        self.tray_groupBox.setTitle(_translate("PageAppearance", "Tray icon"))
        self.tray_default_radioButton.setText(_translate("PageAppearance", "Default"))
        self.tray_slight_radioButton.setText(_translate("PageAppearance", "Symbolic light"))
        self.tray_sdark_radioButton.setText(_translate("PageAppearance", "Symbolic dark"))
        self.browser_sidebar.setText(_translate("PageAppearance", "Show sidebar"))
        self.mainwindow_menu.setText(_translate("PageAppearance", "Show menu bar"))
        self.scaleLabel.setText(_translate("PageAppearance", "Scale"))
        self.scaleComboBox.setItemText(0, _translate("PageAppearance", "100 %"))
        self.scaleComboBox.setItemText(1, _translate("PageAppearance", "125 %"))
        self.scaleComboBox.setItemText(2, _translate("PageAppearance", "150 %"))
        self.scaleComboBox.setItemText(3, _translate("PageAppearance", "175 %"))
        self.scaleComboBox.setItemText(4, _translate("PageAppearance", "200 %"))
        self.label_2.setText(_translate("PageAppearance", "Note: The change of scale will only have effect until restarting."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PageAppearance = QtWidgets.QWidget()
    ui = Ui_PageAppearance()
    ui.setupUi(PageAppearance)
    PageAppearance.show()
    sys.exit(app.exec())
