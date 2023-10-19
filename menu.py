import nuke

NODES = ["Haze", "IterationRolloff"]



def add_nodes_to_menu():
    for menu in ["Nuke", "Nodes"]:
        nuke_menu = nuke.menu(menu)
        kombinat = nuke_menu.addMenu("nuke_kombinat")
        kombinat_nodes = kombinat.addMenu("Nodes")

        for node in NODES:
            kombinat_nodes.addCommand(node, "nuke.createNode('{}')".format(node))



add_nodes_to_menu()