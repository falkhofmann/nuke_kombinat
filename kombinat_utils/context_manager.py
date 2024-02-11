import logging
from time import perf_counter

import nuke
import nukescripts


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

    def __exit__(self, exc_type, ec_value, traceback):
        for node in self.selected_nodes:
            node.setSelected(True)
