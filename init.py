import nuke


def extend_plugin_path():
    paths = ["./icons", "./gizmos"]

    for path in paths:
        nuke.pluginAddPath(path)


extend_plugin_path()
