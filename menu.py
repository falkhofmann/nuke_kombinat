import nuke

GENERATORS = ["Lines", "Mandelbrot", "RadialGradient", "RadialRays", "Ringing"]
MODIFIERS = ["Haze", "IterationRolloff", "Kontrast", "Vibrant"]


def add_nodes_to_menu():
    for menu in ["Nuke", "Nodes"]:
        nuke_menu = nuke.menu(menu)
        kombinat = nuke_menu.addMenu("nuke_kombinat")
        kombinat_generators = kombinat.addMenu("Generators")
        kombinat_modifiers = kombinat.addMenu("Modifiers")

        for node in GENERATORS:
            kombinat_generators.addCommand(node, "nuke.createNode('{}')".format(node))

        for node in MODIFIERS:
            kombinat_modifiers.addCommand(node, "nuke.createNode('{}')".format(node))


add_nodes_to_menu()