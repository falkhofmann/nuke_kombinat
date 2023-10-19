import nuke

GENERATORS = ["lines", "radialGradient", "radialRays", "ringing"]
MODIFIERS = ["Haze", "IterationRolloff", "Kontrast", "Vibrant"]


def add_nodes_to_menu():
    for menu in ["Nuke", "Nodes"]:
        nuke_menu = nuke.menu(menu)
        kombinat = nuke_menu.addMenu("nuke_kombinat")
        kombinat_nodes = kombinat.addMenu("Nodes")
        kombinat_generators = kombinat_nodes.addMenu("generators")
        kombinat_modifiers = kombinat_nodes.addMenu("MODIFIERS")

        for node in GENERATORS:
            kombinat_generators.addCommand(node, "nuke.createNode('{}')".format(node))

        for node in MODIFIERS:
            kombinat_modifiers.addCommand(node, "nuke.createNode('{}')".format(node))


add_nodes_to_menu()