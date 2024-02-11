import nuke
import nukescripts


def clear_animation():

    for node in nuke.selectedNodes():
        for knob in node.knobs():
            if nuke.Knob.isAnimated(node[knob]):
                nuke.Knob.clearAnimated(node[knob])


def cornerpin_ref_frame():
    selected_nodes = nuke.selectedNodes(filter="CornerPin2D")

    for node in selected_nodes:
        tab_knob = nuke.Tab_Knob("reference_frame", "reference frame")
        ref_frame_knob = nuke.Int_Knob("ref_frame", "reference frame")
        ref_frame_knob.setTooltip("Define the reference frame on the anmiation.")
        ref_frame_knob.setValue(nuke.frame())

        node.addKnob(tab_knob)
        node.addKnob(ref_frame_knob)
        for idx in range(1, 5):
            node[f"from{idx}"].setExpression(f"to{idx}(ref_frame)")


def declone_selected():
    for node in nuke.selectedNodes():
        nukescripts.declone(node)


def delete_all_viewer():
    for node in nuke.allNodes(recurseGroups=True):
        if node.Class() == "Viewer":
            nuke.delete(node)


def turn_postage_stamps_off():

    for node in nuke.allNodes(recurseGroups=True):
        if "postage_stamp" in node.knobs():
            node["postage_stamp"].setValue(False)
