'''

arnold_refl_aovs_main_py2.py

This file is accessed when Python Version 3 is detected.

This file contains Class ReflectionAOV,
Main Window loading and Signals and Slots for UI building.

'''

import os

from PySide2 import QtCore, QtWidgets, QtUiTools
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

import data.arnold_refl_aovs_functions_py3 as func

def maya_main_window():
    '''
    Maya Main Window Pointer
    :return: QtWidgets.QWidget Object
    '''
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class ReflectionAOV(QtWidgets.QDialog):
    '''
    Reflection AOV main UI and functions.
    '''
    def __init__(self, ui_path=None, parent=maya_main_window()):
        '''
        Initializing Cunstructor
        '''
        super().__init__(parent)

        self.setWindowTitle("Arnold Reflection AOVs")
        self.resize(412, 300)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.init_ui(ui_path)
        self.create_layout()
        self.aovs_list()
        self.arnold_default_check()
        self.all_light_groups()
        self.available_aov_list()
        self.active_aov_list()
        self.create_connections()

    def init_ui(self, ui_path):
        '''
        py ui file load
        :return: None
        '''
        if not ui_path:
            ui_path = f"{os.path.dirname(__file__)}/arnold_refl_aovs_ui.ui"

        file = QtCore.QFile(ui_path)
        file.open(QtCore.QFile.ReadOnly)

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(file)

        file.close()

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(6, 6, 6, 6)
        main_layout.addWidget(self.ui)

    def create_connections(self):
        '''
        All connections of Signals snd Slots
        :return: None
        '''
        self.ui.available_aovs_btn.clicked.connect(self.in_to_out_list)
        self.ui.active_aovs_btn.clicked.connect(self.out_to_in_list)
        self.ui.available_aovs_list.doubleClicked.connect(self.available_double_click)
        self.ui.active_aovs_list.clicked.connect(self.active_single_click)

    def aovs_list(self):
        '''
        data.arnold_refl_aovs_functions_py3: aovs_list()
        :return:
        '''
        self.REFLECTION_AOVS_LIST = func.aovs_list()

    def arnold_default_check(self):
        '''
        data.arnold_refl_aovs_functions_py3: arnold_default_check()
        :return:
        '''
        func.arnold_default_check()

    def all_light_groups(self):
        '''
        data.arnold_refl_aovs_functions_py3: all_light_groups()
        :return:
        '''
        func.all_light_groups(self.REFLECTION_AOVS_LIST)

    def available_aov_list(self):
        '''
        data.arnold_refl_aovs_functions_py3: available_aov_list()
        :return:
        '''
        func.available_aov_list(self.ui, self.REFLECTION_AOVS_LIST)

    def active_aov_list(self):
        '''
        data.arnold_refl_aovs_functions_py3: active_aov_list()
        :return:
        '''
        func.active_aov_list(self.ui, self.REFLECTION_AOVS_LIST)

    def in_to_out_list(self):
        '''
        data.arnold_refl_aovs_functions_py3: in_to_out_list()
        :return:
        '''
        func.in_to_out_list(self.ui, self.REFLECTION_AOVS_LIST)

    def out_to_in_list(self):
        '''
        data.arnold_refl_aovs_functions_py3: out_to_in_list()
        :return:
        '''
        func.out_to_in_list(self.ui, self.REFLECTION_AOVS_LIST)

    def available_double_click(self):
        '''
        data.arnold_refl_aovs_functions_py3: available_double_click()
        :return:
        '''
        func.available_double_click(self.ui, self.REFLECTION_AOVS_LIST)

    def active_single_click(self):
        '''
        data.arnold_refl_aovs_functions_py3: active_single_click()
        :return:
        '''
        func.active_single_click(self.ui)