import nuke

DATA = {
    "Achannels": ["Achannels", "Bchannels", "output"],
    "falloff": ["output", "color"],
    "channels": ["channels"],
    "output": ["output"],
}

CYCLE = {"alpha": "rgba", "rgba": "rgb"}


class ChannelToggler(object):

    def __init__(self):
        selectedNodes = nuke.selectedNodes()
        for node in selectedNodes:
            channels = self.channels(node)
            self.toggle_channels(node, channels)

    def channels(self, node):
        channels = {}
        channel_types = []

        for knob_name in DATA.keys():
            if knob_name in node.knobs():
                channel_types.extend(DATA[knob_name])
                channels[1] = node.knob(knob_name).value()

        channels[0] = channel_types
        return channels

    def toggle_channels(self, node, channels):
        set_to = CYCLE[channels[1]] if channels[1] in CYCLE.keys() else "alpha"
        for channel in channels[0]:
            node.knob(channel).setValue(set_to)


def toggle_channel():
    ChannelToggler()
