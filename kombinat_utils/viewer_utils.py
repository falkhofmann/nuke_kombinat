# -*- coding: utf-8 -*-
import nuke
from PySide2 import QtWidgets


def find_active_viewer_widget():
    for widget in QtWidgets.QApplication.allWidgets():
        if widget.windowTitle() == nuke.activeViewer().node().name():
            return widget


def find_view_menu_object(qtObject, tooltip_starts_with):
    for children in qtObject.children():
        found = find_view_menu_object(children, tooltip_starts_with)
        if found:
            return found
        try:
            if children.toolTip().startswith(tooltip_starts_with):
                return children
        except:
            pass


def cycle_lut_menu(direction=1):

    viewer = nuke.activeViewer().node()["viewerProcess"]
    values = viewer.values()
    current = values.index(viewer.value())
    update = current + direction
    last = len(values) - 1

    if update <= last and update > 0:
        viewer.setValue(update)
    elif update == -1:
        viewer.setValue(last)
    else:
        viewer.setValue(0)
