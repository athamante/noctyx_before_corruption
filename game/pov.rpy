"""For UI that needs to be POV-specific."""
init python:
    class POVTracker():
        def __init__(self):
            self.current_pov = "none"
            self.pov_specific_actions = {
                "alban": [self.disable_information_menu],
                "fulgur": [self.enable_information_menu],
                "protag": [self.disable_information_menu],
                "sonny": [self.disable_information_menu],
                "uki": [self.disable_information_menu],
            }

        def switch_pov(self, new_pov):
            self.current_pov = new_pov
            for action in self.pov_specific_actions[new_pov]:
                action()

        def enable_information_menu(self):
            renpy.show_screen("information_button", _zorder=100)

        def disable_information_menu(self):
            renpy.hide_screen("information_button")

    pov_tracker = POVTracker()
