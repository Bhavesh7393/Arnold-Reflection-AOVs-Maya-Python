'''

load_ui.py

This file is linked with 7 files, which are located inside "data" folder.
Python 3 files: arnold_refl_aovs_functions_py3.py, arnold_refl_aovs_main_py3.py
Python 2 files: arnold_refl_aovs_functions_py2.py, arnold_refl_aovs_main_py2.py
aovs list file: arnold_refl_aovs_list.txt
Qt Designer ui file: arnold_refl_aovs_ui.ui
pyside2-uic converted py file: arnold_refl_aovs_ui.py

Replace "path" with your local directory till "arnold_reflection_aovs" folder.
Execute the script in Maya-Python Script Editor.

Tested on:
Maya [2018-2020] Python 2
Maya 2022 Python 2 and Python 3

Features:
1. Exact same UI and functionality as Arnold AOV Browser in Maya Render Settings.
2. 2 additional Beauty AOVs: specular_only and hair.
   Arnold considers aiStandardSurface Specular and aiStandardHair Specular
   as same specular AOV and does not differentiate.
   specular_only AOV only extracts aiStandardSurface Specular,
   and hair AOV only extracts aiStandardHair Specular
3. All possible Beauty AOVs have their Reflection AOVs.
4. Emission have 2 additional Reflection AOVs:
   refl_light_emission: Light Emission in Reflection
   refl_object_emission: Shader Emission in Reflection
5. refl_RGBA_default Reflection Light Group is provided by default.
   any additional Light Groups will automatically appear in the list
   as refl_lightgroup AOVs.

Limitation:
1. If you add refl_lightgroup AOV in the scene and later delete the light
   associated with that Light Group, relaunching UI will automatically
   remove the name of the AOV from the list, but Light Group AOV won't
   be removed and you will have to manually delete the AOV.
2. Any new Reflection Light Group AOV will append in the list at the bottom,
   you will have to relaunch the UI for list to refresh.

Document: https://bhavesh7393.artstation.com/pages/reflection-aovs

Author:
Bhavesh Budhkar
bhaveshbudhkar@yahoo.com

'''

import sys

path = r"/path/arnold_reflection_aovs"

if path not in sys.path:
    sys.path.append(path)

if sys.version[0] == str(3):
    from data.arnold_refl_aovs_main_py3 import ReflectionAOV
else:
    from data.arnold_refl_aovs_main_py2 import ReflectionAOV

try:
    reflection_aov.close()
    reflection_aov.deleteLater()
except:
    pass
reflection_aov = ReflectionAOV()
reflection_aov.show()