import nuke


def extend_plugin_path():
    paths = ["./icons", "./gizmos", "./kombinat_start_up"]

    for path in paths:
        nuke.pluginAddPath(path)


extend_plugin_path()
