init python:
    class InformationEntry:
        def __init__(self, index, location, description):
            self.index = index
            self.location = location
            self.description = description
            self.enabled = False

    information_dict = {
        'kat_virus': InformationEntry(
            index=0,
            location="Fulgur's Ship",
            description="Dog and Cat are showing strange symptoms, but Kat isn't. Kat's chip is also broken.",
        ),
        'test_info_enabled': InformationEntry(
            index=1,
            location="Fake Location 1",
            description="Fake description for testing purposes. Will be enabled.",
        ),
        'test_info_disabled': InformationEntry(
            index=2,
            location="Fake Location 2",
            description="Fake description for testing purposes. Will be disabled.",
        ),
    }

    def add_to_journal(info_name):
        information_dict[info_name].enabled = True

screen information_button():
    vbox:
        xalign 0.03
        yalign 0.03
        imagebutton auto "misc/nijisanji_logo_%s.png" action ShowMenu("information")

screen information():

    tag menu

    use game_menu(
        "Information Journal",
        scroll=("vpgrid" if gui.history_height else "viewport"),
        yinitial=1.0,
    ):
        style_prefix "information"

        $ enabled_entries = [entry for entry in information_dict.values() if entry.enabled]

        for entry in sorted(enabled_entries, key=lambda e: e.index):

            window:
                has fixed:
                    yfit True

                label entry.location:
                    style "information_location"

                text entry.description

        if not enabled_entries:
            label _("The information journal is empty.")


style information_window is empty

style information_location is gui_label
style information_location_text is gui_label_text
style information_text is gui_text

style information_label is gui_label
style information_label_text is gui_label_text

style information_window:
    xfill True
    ysize gui.history_height

style information_location:
    xpos 300
    xanchor 1.0
    xsize 300

style information_location_text:
    textalign 1.0

style information_text:
    xpos 350
    xanchor 0.0
    xfill True
    textalign 0.0
    layout "subtitle"

style information_label:
    xfill True

style information_label_text:
    xalign 0.5