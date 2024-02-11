import logging
from time import perf_counter

import nuke
import nukescripts

from kombinat_utils import viewer_utils


class Timer:
    "Context manager to measure performance during developing."

    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0

    def __exit__(self, *args):
        self.end = perf_counter()
        passed = self.end - self.start
        logging.info(f"{passed} seconds")


class SaveSelection:
    "Context manager to store and restore selection."

    def __init__(self) -> None:
        self.selected_nodes = nuke.selectedNodes()

    def __enter__(self) -> None:
        nukescripts.clear_selection_recursive()

    def __exit__(self, exc_type, exc_value, traceback):
        for node in self.selected_nodes:
            node.setSelected(True)


class PausedViewer:
    """Context manager to pause and unpause the active viewer.

    In case the viewer is paused already the toggle is skipped."""

    def __init__(self) -> None:
        self.viewer = viewer_utils.find_active_viewer_widget()
        self.pause_button = viewer_utils.find_view_menu_object(self.viewer, "Pause")
        self.initial_paused = self.pause_button.isChecked()

    def __enter__(self) -> None:
        if not self.initial_paused:
            self.pause_button.toggle()

    def __exit__(self, exc_type, exc_value, traceback):
        if not self.initial_paused:
            self.pause_button.toggle()
