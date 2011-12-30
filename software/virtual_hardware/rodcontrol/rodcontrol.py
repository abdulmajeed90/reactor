# -*- coding: utf-8 -*-

"""Rod control panel"""

import sys

from PySide import QtCore
from PySide import QtGui
from PySide import QtDeclarative


class Controller(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.Slot(QtCore.QObject)
    def switch_changed(self, switch_instance):
        # Switched to center
        if (int(switch_instance.property('value')) == 0):
            if (int(switch_instance.property('prevValue')) == 1):
                print "pin %d went high (ie switch stopped pulling down)" % int(switch_instance.property('upPin'))
            else:
                print "pin %d went high (ie switch stopped pulling down)" % int(switch_instance.property('downPin'))
            return
        # Switched up/down
        if (int(switch_instance.property('value')) == 1):
            print "pin %d went low" % int(switch_instance.property('upPin'))
        else:
            print "pin %d went low" % int(switch_instance.property('downPin'))
        return

        

app = QtGui.QApplication(sys.argv)

view = QtDeclarative.QDeclarativeView()
view.setWindowTitle(__doc__)
view.setResizeMode(QtDeclarative.QDeclarativeView.SizeRootObjectToView)

rc = view.rootContext()

controller = Controller()
rc.setContextProperty('controller', controller)

view.setSource(__file__.replace('.py', '.qml'))

view.show()
app.exec_()

