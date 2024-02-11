import nuke

from kombinat_settings import CUSTOM_NODES_SHORTCUTS, GENERATORS, MENU_NAME, MODIFIERS
from kombinat_tools import channel_toggler


def add_nodes_to_menu():

    nuke_menu = nuke.menu("Nodes")
    kombinat = nuke_menu.addMenu(MENU_NAME)
    kombinat_generators = kombinat.addMenu("Generators")
    kombinat_modifiers = kombinat.addMenu("Modifiers")

    for node in GENERATORS:
        kombinat_generators.addCommand(node, "nuke.createNode('{}')".format(node))

    for node in MODIFIERS:
        kombinat_modifiers.addCommand(node, "nuke.createNode('{}')".format(node))


def add_tools_to_menu():
    menubar = nuke.menu("Nuke").addMenu(MENU_NAME)
    nodegraph = menubar.addMenu("nodegraph")
    nodegraph.addCommand("toggle channels", channel_toggler.toggle_channel, "q")


def add_custom_shortcuts():
    nodes = nuke.menu("Nodes")

    for menuitem, shortcut in CUSTOM_NODES_SHORTCUTS.items():
        node = nodes.findItem(menuitem)
        node.setShortcut(shortcut)

    nuke.menu("Nuke").findItem("Edit").findItem("Extract").setShortcut("e")


add_nodes_to_menu()
add_tools_to_menu()
add_custom_shortcuts()
