'''

arnold_refl_aovs_main_py2.py

This file is accessed when Python Version 2 is detected.

This file contains Class ReflectionAOV,
Main Window loading and Signals and Slots for UI building.

'''

from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

import data.arnold_refl_aovs_functions_py2 as func
import data.arnold_refl_aovs_ui as window

def maya_main_window():
    '''
    Maya Main Window Pointer
    :return: QtWidgets.QWidget Object
    '''
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class ReflectionAOV(QtWidgets.QDialog):
    '''
    Reflection AOV main UI and functions.
    '''
    def __init__(self):
        '''
        Initializing Cunstructor
        '''
        super(ReflectionAOV, self).__init__(maya_main_window())

        self.setWindowTitle("Arnold Reflection AOVs")
        self.setFixedWidth(412)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.aovs_list()
        self.arnold_default_check()
        self.all_light_groups()
        self.init_ui()
        self.available_aov_list()
        self.active_aov_list()
        self.create_connections()

    def init_ui(self):
        '''
        py ui file load
        :return: None
        '''
        self.ui = window.Ui_main_layout()
        self.ui.setupUi(self)

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
        data.arnold_refl_aovs_functions_py2: aovs_list()
        :return:
        '''
        self.REFLECTION_AOVS_LIST = func.aovs_list()

    def arnold_default_check(self):
        '''
        data.arnold_refl_aovs_functions_py2: arnold_default_check()
        :return:
        '''
        func.arnold_default_check()

    def all_light_groups(self):
        '''
        data.arnold_refl_aovs_functions_py2: all_light_groups()
        :return:
        '''
        func.all_light_groups(self.REFLECTION_AOVS_LIST)

    def available_aov_list(self):
        '''
        data.arnold_refl_aovs_functions_py2: available_aov_list()
        :return:
        '''
        func.available_aov_list(self.ui, self.REFLECTION_AOVS_LIST)

    def active_aov_list(self):
        '''
        data.arnold_refl_aovs_functions_py2: active_aov_list()
        :return:
        '''
        func.active_aov_list(self.ui, self.REFLECTION_AOVS_LIST)

    def in_to_out_list(self):
        '''
        data.arnold_refl_aovs_functions_py2: in_to_out_list()
        :return:
        '''
        func.in_to_out_list(self.ui, self.REFLECTION_AOVS_LIST)

    def out_to_in_list(self):
        '''
        data.arnold_refl_aovs_functions_py2: out_to_in_list()
        :return:
        '''
        func.out_to_in_list(self.ui, self.REFLECTION_AOVS_LIST)

    def available_double_click(self):
        '''
        data.arnold_refl_aovs_functions_py2: available_double_click()
        :return:
        '''
        func.available_double_click(self.ui, self.REFLECTION_AOVS_LIST)

    def active_single_click(self):
        '''
        data.arnold_refl_aovs_functions_py2: active_single_click()
        :return:
        '''
        func.active_single_click(self.ui)