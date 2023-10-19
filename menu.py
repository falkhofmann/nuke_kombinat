import nuke

UTILS = ["Haze", "IterationRolloff"]
GENERATORS = ["radialGradient"]



def add_nodes_to_menu():
    for menu in ["Nuke", "Nodes"]:
        nuke_menu = nuke.menu(menu)
        kombinat = nuke_menu.addMenu("nuke_kombinat")
        kombinat_nodes = kombinat.addMenu("Nodes")
        kombinat_generators = kombinat_nodes.addMenu("generators")
        kombinat_utils = kombinat_nodes.addMenu("utils")

        for node in GENERATORS:
            kombinat_generators.addCommand(node, "nuke.createNode('{}')".format(node))

        for node in UTILS:
            kombinat_utils.addCommand(node, "nuke.createNode('{}')".format(node))


add_nodes_to_menu()