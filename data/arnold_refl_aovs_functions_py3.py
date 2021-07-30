'''

arnold_refl_aovs_functions_py2.py

This file is accessed when Python Version 3 is detected.

This file contains all required functions to run UI.

'''

import os
from PySide2 import QtCore, QtWidgets
import maya.cmds as cmds

def create_aov(name, lpe):
    '''
    Create AOV in scene, and do necessary connections to appear in
    Arnold Render.
    :param name: name of the AOV
    :param lpe: Light Path Expression of the AOV
    :return: None
    '''
    aov = cmds.createNode("aiAOV", n="aiAOV_" + name)
    cmds.setAttr(aov + ".type", 5)
    cmds.setAttr(aov + ".name", aov[6:], type="string")
    index = 0

    while cmds.connectionInfo("defaultArnoldRenderOptions.aovList" + str([index]), isExactDestination=True) == True:
        index += 1

    cmds.connectAttr(aov + ".message", "defaultArnoldRenderOptions.aovList" + str([index]), force=1)
    cmds.connectAttr("defaultArnoldDriver.message", aov + ".outputs" + str([0]) + ".driver", force=1)
    cmds.connectAttr("defaultArnoldFilter.message", aov + ".outputs" + str([0]) + ".filter", force=1)
    cmds.setAttr(aov + ".lightPathExpression", lpe, type="string")


def delete_aov(name):
    '''
    Delete existing AOV from scene.
    :param name: name of the AOV
    :return: None
    '''
    cmds.delete("aiAOV_" + name)

def in_to_out_list(ui, REFLECTION_AOVS_LIST):
    '''
    Transfer selected AOVs names from Available AOVs list
    to Active AOVs list.
    :param ui: UI object
    :param REFLECTION_AOVS_LIST: Reflection AOVs list
    :return: None
    '''
    selected_available_items = ui.available_aovs_list.selectedItems()
    selected_indexes = ui.available_aovs_list.selectedIndexes()

    unhide_active_items = []
    for index in selected_indexes:
        unhide_active_items.append(ui.active_aovs_list.item(index.row()))
        create_aov(REFLECTION_AOVS_LIST[index.row()][0], REFLECTION_AOVS_LIST[index.row()][1])

    for available_item, active_item in zip(selected_available_items, unhide_active_items):
        available_item.setHidden(True)
        active_item.setHidden(False)

def out_to_in_list(ui, REFLECTION_AOVS_LIST):
    '''
    Transfer selected AOVs names from Active AOVs list
    to Available AOVs list.
    :param ui: UI object
    :param REFLECTION_AOVS_LIST: Reflection AOVs list
    :return: None
    '''
    selected_active_items = ui.active_aovs_list.selectedItems()
    selected_indexes = ui.active_aovs_list.selectedIndexes()

    unhide_available_items = []
    for index in selected_indexes:
        unhide_available_items.append(ui.available_aovs_list.item(index.row()))
        delete_aov(REFLECTION_AOVS_LIST[index.row()][0])

    for available_item, active_item in zip(unhide_available_items, selected_active_items):
        available_item.setHidden(False)
        active_item.setHidden(True)

def available_double_click(ui, REFLECTION_AOVS_LIST):
    '''
    When Mouse double clicked any AOV from Available AOVs list,
    it transfers AOV name from Available AOVs list to Active AOVs list.
    :param ui: UI object
    :param REFLECTION_AOVS_LIST: Reflection AOVs list
    :return: None
    '''
    create_aov(REFLECTION_AOVS_LIST[ui.available_aovs_list.currentRow()][0], REFLECTION_AOVS_LIST[ui.available_aovs_list.currentRow()][1])
    ui.available_aovs_list.currentItem().setHidden(True)
    ui.active_aovs_list.item(ui.available_aovs_list.currentRow()).setHidden(False)

def active_single_click(ui):
    '''
    When Mouse single clicked any AOV from Active AOVs list,
    it selects that aiAOV node.
    :param ui: UI object
    :return: None
    '''
    cmds.select(("aiAOV_" + str(ui.active_aovs_list.selectedItems()[0].text())))

def aovs_list():
    '''
    Loads AOVs list defined in data/arnold_refl_aovs_list.txt
    :return: Reflection AOVs list
    '''
    list_file = open(f"{os.path.dirname(__file__)}/arnold_refl_aovs_list.txt", "r")
    lines = list_file.readlines()
    REFLECTION_AOVS_LIST = []
    for line in lines:
        REFLECTION_AOVS_LIST.append([line.split(",")[0], line.split(",")[1]])
    list_file.close()
    return REFLECTION_AOVS_LIST

def arnold_default_check():
    '''
    Checks Arnold Default Drivers, creates if not exist.
    :return: None
    '''
    if cmds.objExists("defaultArnoldRenderOptions") == False:
        cmds.createNode("aiOptions", n="defaultArnoldRenderOptions")
    if cmds.objExists("defaultArnoldDriver") == False:
        cmds.createNode("aiAOVDriver", n="defaultArnoldDriver")
    if cmds.objExists("defaultArnoldFilter") == False:
        cmds.createNode("aiAOVFilter", n="defaultArnoldFilter")

def all_light_groups(REFLECTION_AOVS_LIST):
    '''
    Extract all Light Groups from scene and append in Reflection AOVs list.
    :param REFLECTION_AOVS_LIST: Reflection AOVs list
    :return: None
    '''
    all_lights_list = cmds.ls(type=["light", "aiAreaLight", "aiSkyDomeLight", "aiMeshLight", "aiPhotometricLight"])
    light_group_list = []

    for light_group in all_lights_list:
        if cmds.getAttr(light_group+".ai_aov") != "default":
            light_group_list.append(cmds.getAttr(light_group+".ai_aov"))
    light_group_list.sort()

    for light_group in light_group_list:
        if light_group not in REFLECTION_AOVS_LIST:
            REFLECTION_AOVS_LIST.append(["refl_RGBA_" + light_group, "C<RS>.*<L.'" + light_group + "'>"])

def available_aov_list(ui, REFLECTION_AOVS_LIST):
    '''
    Generates Available AOVs list, and present in UI.
    :param ui: UI Object
    :param REFLECTION_AOVS_LIST: Reflection AOVs list
    :return: None
    '''
    for reflection_aov in REFLECTION_AOVS_LIST:
        available_aov_item = QtWidgets.QListWidgetItem(reflection_aov[0])
        ui.available_aovs_list.addItem(available_aov_item)

    available_aov_list_items = []
    for index in range(ui.available_aovs_list.count()):
        if cmds.objExists("aiAOV_"+REFLECTION_AOVS_LIST[index][0])==True:
            available_aov_list_items.append(ui.available_aovs_list.item(index))

    for item in available_aov_list_items:
        item.setHidden(True)

def active_aov_list(ui, REFLECTION_AOVS_LIST):
    '''
    Generates Active AOVs list, and present in UI.
    :param ui: UI Object
    :param REFLECTION_AOVS_LIST: Reflection AOVs list
    :return: None
    '''
    for reflection_aov in REFLECTION_AOVS_LIST:
        active_aov_item = QtWidgets.QListWidgetItem(reflection_aov[0])
        ui.active_aovs_list.addItem(active_aov_item)

    active_aov_list_items = []
    for index in range(ui.active_aovs_list.count()):
        if cmds.objExists("aiAOV_"+REFLECTION_AOVS_LIST[index][0])==False and ui.active_aovs_list.findItems(REFLECTION_AOVS_LIST[index][0], QtCore.Qt.MatchExactly)[0].text() == REFLECTION_AOVS_LIST[index][0]:
            active_aov_list_items.append(ui.active_aovs_list.item(index))

    for item in active_aov_list_items:
        item.setHidden(True)