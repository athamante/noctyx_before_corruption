# Placeholder for testing purposes
image smaller_uki:
    "sprites/uki/default.png"
    zoom 0.8

screen dress_up_minigame():
    hbox:
        frame:
            style "dress_up_display"
            # This should be the actual command, but since we don't have the pieces
            # to make the composite sprite we're using a placeholder for now.
            # add "uki_sprite" at truecenter
            add "smaller_uki" at truecenter

        frame:
            style_prefix "dress_up_choices"

            vbox:
                label "Choose your outfit for the day!"

                # Currently assumes four variations of every option, can be updated later.
                hbox:
                    textbutton "Prev" action SetVariable("uki_hair_index", (uki_hair_index - 1) % 4)
                    text "Hair"
                    textbutton "Next" action SetVariable("uki_hair_index", (uki_hair_index + 1) % 4)

                hbox:
                    textbutton "Prev" action SetVariable("uki_eyewear_index", (uki_eyewear_index - 1) % 4)
                    text "Eyewear"
                    textbutton "Next" action SetVariable("uki_eyewear_index", (uki_eyewear_index + 1) % 4)

                hbox:
                    textbutton "Prev" action SetVariable("uki_outerwear_index", (uki_outerwear_index - 1) % 4)
                    text "Outerwear"
                    textbutton "Next" action SetVariable("uki_outerwear_index", (uki_outerwear_index + 1) % 4)

                hbox:
                    textbutton "Prev" action SetVariable("uki_top_index", (uki_top_index - 1) % 4)
                    text "Top"
                    textbutton "Next" action SetVariable("uki_top_index", (uki_top_index + 1) % 4)


                hbox:
                    textbutton "Prev" action SetVariable("uki_bottom_index", (uki_bottom_index - 1) % 4)
                    text "Bottom"
                    textbutton "Next" action SetVariable("uki_bottom_index", (uki_bottom_index + 1) % 4)

                hbox:
                    textbutton "Prev" action SetVariable("uki_shoes_index", (uki_shoes_index - 1) % 4)
                    text "Shoes"
                    textbutton "Next" action SetVariable("uki_shoes_index", (uki_shoes_index + 1) % 4)

                hbox:
                    textbutton "Done" action Return()

style dress_up_display is gui_frame
style dress_up_choices_frame is gui_frame
style dress_up_choices_vbox is default
style dress_up_choices_hbox is default
style dress_up_choices_label is gui_label
style dress_up_choices_text is gui_text
style dress_up_choices_button is gui_button
style dress_up_choices_button_text is gui_button_text

style dress_up_display:
    xsize 1200
    xmargin 20
    ymargin 20
    yfill True

style dress_up_choices_frame:
    xfill True
    yfill True
    ymargin 20
    right_margin 20

style dress_up_choices_vbox:
    yfill True
    xfill True
    xalign 0.5
    yalign 0.5

style dress_up_choices_label:
    ymargin 30
    xalign 0.5
    yalign 0.5

style dress_up_choices_hbox:
    xalign 0.5
    xsize 300
    bottom_margin 20

style dress_up_choices_text:
    xsize 150
    xmargin 10
    xalign 0.5
    yalign 0.5

style dress_up_choices_button:
    xalign 0.5
    xsize 150

style dress_up_choices_button_text:
    xalign 0.5
