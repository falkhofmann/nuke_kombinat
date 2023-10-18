import nuke

NODES = ["Haze", "IterationRolloff"]



def add_nodes_to_menu():
    toolbar = nuke.menu("Nodes")
    nodes = toolbar.addMenu("fhofmann/nodes")

    for node in NODES:
        nodes.addCommand(node, "nuke.createNode('{}')".format(node))



add_nodes_to_menu()