

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from shiboken2 import wrapInstance
from maya import OpenMayaUI as omui

import fx_lib.fx_lib_ui_ps2 as fx_lib_ui_ps2

import maya.cmds as cmds
import maya.mel as mel


def mayaMainWindow():
    '''
    Get the main Maya window as a QMainWindow instance
    :return: QMainWindow instance of the top level Maya windows
    '''
    ptr = omui.MQtUtil.mainWindow()
    if ptr is not None:
        return wrapInstance(long(ptr), QMainWindow)



class TN_Fx(QMainWindow, fx_lib_ui_ps2.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TN_Fx, self).__init__(parent)

        self.setupUi(self)
        self.setWindowTitle("aaaaa")
        path = "O:/08_FX/01_Scene/assetlib/master/3D/F/_Icon/TN_FireChacoal_Fx_A.JPG"
        self.toolButton.setIcon(QIcon(path))
        self.toolButton.clicked.connect(self.func)





import fx_lib.fx_lib_ui_ps2
reload(fx_lib.fx_lib_ui_ps2)
if __name__ == "__main__":

    global tnfx
    try:
        tnfx.close()
    except:
        pass

    mayawin = mayaMainWindow()
    tnfx = TN_Fx(parent=mayawin)
    tnfx.show()



# QMediaPlayer *player = new QMediaPlayer(this);
# QVideoWidget *vw = new QVideoWidget(this);
#
# QMediaPlaylist *PlayList = new QMediaPlaylist(this);
# PlayList->addMedia(QUrl::fromLocalFile("/home/user/Videos/video.mp4"));
# PlayList->setPlaybackMode(QMediaPlaylist::Loop);
#
# QVBoxLayout *layout = new QVBoxLayout;
# layout->addWidget(vw);
#
# player->setVideoOutput(vw);
# player->setPlaylist(PlayList);
#
# vw->setGeometry(0,0,800,480);
# vw->show();
# player->play();




#
# import fx.utilities.logger as logger;
#
# reload(logger);
# logger.Track_Users('Library', tools=True);
#
# import fx.menus.cmdLib._general as _general;
# _general.assetLibrary();