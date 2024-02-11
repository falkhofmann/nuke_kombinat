import nuke


def extend_plugin_path():
    paths = ["./kombinat_icons", "./kombinat_gizmos", "./kombinat_start_up"]

    for path in paths:
        nuke.pluginAddPath(path)


extend_plugin_path()
