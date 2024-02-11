import json
from pathlib import Path

import nuke
from kombinat_settings import DEFAULT_FILENAME


class KombinatDefaults:

    def __init__(self) -> None:
        self.stored_defaults = self.read_defaults()

    def read_defaults(self):
        defaults_file = Path(__file__).parent.resolve() / DEFAULT_FILENAME

        # TODO sort by keys

        if defaults_file.is_file():
            with open(defaults_file, "r") as default_file:
                return json.load(default_file)
        else:
            return {}

    def apply_knob_defaults(self):
        for key, value in self.stored_defaults.items():
            nuke.knobDefault(key, value)

    def save_knob_defaults(self, values):
        # TODO build export from within nuke
        pass
