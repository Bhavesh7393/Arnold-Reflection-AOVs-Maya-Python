# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arnold_refl_aovs_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_layout(object):
    def setupUi(self, main_layout):
        if not main_layout.objectName():
            main_layout.setObjectName(u"main_layout")
        main_layout.resize(400, 300)
        self.verticalLayout = QVBoxLayout(main_layout)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.label_layout = QHBoxLayout()
        self.label_layout.setObjectName(u"label_layout")
        self.available_aovs_label = QLabel(main_layout)
        self.available_aovs_label.setObjectName(u"available_aovs_label")
        self.available_aovs_label.setAlignment(Qt.AlignCenter)

        self.label_layout.addWidget(self.available_aovs_label)

        self.active_aovs_label = QLabel(main_layout)
        self.active_aovs_label.setObjectName(u"active_aovs_label")
        self.active_aovs_label.setAlignment(Qt.AlignCenter)

        self.label_layout.addWidget(self.active_aovs_label)


        self.verticalLayout.addLayout(self.label_layout)

        self.list_layout = QHBoxLayout()
        self.list_layout.setObjectName(u"list_layout")
        self.available_aovs_list = QListWidget(main_layout)
        self.available_aovs_list.setObjectName(u"available_aovs_list")
        self.available_aovs_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.list_layout.addWidget(self.available_aovs_list)

        self.active_aovs_list = QListWidget(main_layout)
        self.active_aovs_list.setObjectName(u"active_aovs_list")
        self.active_aovs_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.list_layout.addWidget(self.active_aovs_list)


        self.verticalLayout.addLayout(self.list_layout)

        self.btn_layout = QHBoxLayout()
        self.btn_layout.setObjectName(u"btn_layout")
        self.available_aovs_btn = QPushButton(main_layout)
        self.available_aovs_btn.setObjectName(u"available_aovs_btn")

        self.btn_layout.addWidget(self.available_aovs_btn)

        self.active_aovs_btn = QPushButton(main_layout)
        self.active_aovs_btn.setObjectName(u"active_aovs_btn")

        self.btn_layout.addWidget(self.active_aovs_btn)


        self.verticalLayout.addLayout(self.btn_layout)

        self.space_label = QLabel(main_layout)
        self.space_label.setObjectName(u"space_label")

        self.verticalLayout.addWidget(self.space_label)

        self.info_layout = QHBoxLayout()
        self.info_layout.setObjectName(u"info_layout")
        self.name_label = QLabel(main_layout)
        self.name_label.setObjectName(u"name_label")

        self.info_layout.addWidget(self.name_label)

        self.email_label = QLabel(main_layout)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.info_layout.addWidget(self.email_label)


        self.verticalLayout.addLayout(self.info_layout)


        self.retranslateUi(main_layout)

        QMetaObject.connectSlotsByName(main_layout)
    # setupUi

    def retranslateUi(self, main_layout):
        main_layout.setWindowTitle(QCoreApplication.translate("main_layout", u"Dialog", None))
        self.available_aovs_label.setText(QCoreApplication.translate("main_layout", u"Available AOVs", None))
        self.active_aovs_label.setText(QCoreApplication.translate("main_layout", u"Active AOVs", None))
        self.available_aovs_btn.setText(QCoreApplication.translate("main_layout", u">>", None))
        self.active_aovs_btn.setText(QCoreApplication.translate("main_layout", u"<<", None))
        self.space_label.setText("")
        self.name_label.setText(QCoreApplication.translate("main_layout", u"Bhavesh Budhkar", None))
        self.email_label.setText(QCoreApplication.translate("main_layout", u"bhaveshbudhkar@yahoo.com", None))
    # retranslateUi

