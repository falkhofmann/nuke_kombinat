import nuke

from kombinat_start_up.knob_defaults import KombinatDefaults
from kombinat_start_up.kombinat_settings import (
    CUSTOM_MENU_SHORTCUTS,
    CUSTOM_NODES_SHORTCUTS,
    GENERATORS,
    KOMBINAT_NODE_MENU_NAME,
    KOMBINAT_TOOL_MENU_NAME,
    MODIFIERS,
)
from kombinat_tools import channel_toggler
from kombinat_utils import node_utils, viewer_utils


def add_nodes_to_menu():
    nuke_menu = nuke.menu("Nodes")
    kombinat = nuke_menu.addMenu(KOMBINAT_NODE_MENU_NAME, icon="godzilla_invert.png")
    kombinat_generators = kombinat.addMenu("Generators")
    kombinat_modifiers = kombinat.addMenu("Modifiers")

    for node in GENERATORS:
        kombinat_generators.addCommand(node, f"nuke.createNode('{node}')")

    for node in MODIFIERS:
        kombinat_modifiers.addCommand(node, f"nuke.createNode('{node}')")


def add_tools_to_menu():

    for menu in ["Nuke", "Nodes"]:
        icon = "godzilla.png" if menu == "Nodes" else None
        sub_menu = nuke.menu(menu).addMenu(KOMBINAT_TOOL_MENU_NAME, icon)
        nodegraph = sub_menu.addMenu("nodegraph")
        viewer = sub_menu.addMenu("viewer")
        nodegraph.addCommand("clear animation", node_utils.clear_animation)
        nodegraph.addCommand("cornerpint ref frame", node_utils.cornerpin_ref_frame)
        nodegraph.addCommand("delete all viewer nodes", node_utils.delete_all_viewer)
        nodegraph.addCommand("toggle channels", channel_toggler.toggle_channel, "q")
        nodegraph.addCommand(
            "turn off postage stamps", node_utils.turn_postage_stamps_off
        )
        viewer.addCommand(
            "cycle LUT up",
            "viewer_utils.cycle_lut_menu(-1)",
            "shift+up",
            shortcutContext=1,
        )
        viewer.addCommand(
            "cycle LUT down",
            "viewer_utils.cycle_lut_menu(1)",
            "shift+down",
            shortcutContext=1,
        )


def add_custom_shortcuts():
    nodes = nuke.menu("Nodes")
    for menuitem, shortcut in CUSTOM_NODES_SHORTCUTS.items():
        nodes.findItem(menuitem).setShortcut(shortcut)

    menu = nuke.menu("Nuke")
    for menuitem, shortcut in CUSTOM_MENU_SHORTCUTS.items():
        menu.findItem(menuitem).setShortcut(shortcut)


def apply_knob_defaults():
    kombinat_default = KombinatDefaults()
    kombinat_default.apply_knob_defaults()


add_tools_to_menu()
add_nodes_to_menu()
add_custom_shortcuts()
apply_knob_defaults()
