from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance

import maya.OpenMayaUI as apiUI
from maya import OpenMayaUI as omui
import maya.cmds as cmds

currentPanel = cmds.getPanel(withFocus=True)
view = apiUI.M3dView()
apiUI.M3dView.getM3dViewFromModelPanel(currentPanel, view)
viewWidget = wrapInstance(long(view.widget()), QMainWindow)



global myBtn
try:
    myBtn.deleteLater()
except:
    pass
myBtn = QPushButton(parent=viewWidget)
myBtn.setText('testing!')

myBtn.setStyleSheet('''QPushButton {
                                    text-align: center;
                                    background: rgb(0, 0, 0, 200); color: rgb(255, 255, 255);
                                    border-style: solid;
                                    font: 30px;}
                    ''')
myBtn.resize(200, 50)
# myBtn.move(100, 100) #Relative to top-left corner of viewport
myBtn.show()



#
#
# import maya.OpenMaya as OpenMaya
# import maya.OpenMayaUI as OpenMayaUI
#
# maya3DViewHandle = OpenMayaUI.M3dView()
# activeView = maya3DViewHandle.active3dView()
#
# textPositionNearPlane = OpenMaya.MPoint()
# textPositionFarPlane = OpenMaya.MPoint()
#
# activeView.viewToWorld(400, 400, textPositionNearPlane, textPositionFarPlane)
# activeView.beginOverlayDrawing()
# activeView.drawText("Some Text", textPositionNearPlane, OpenMayaUI.M3dView.kLeft)
# activeView.endOverlayDrawing()

