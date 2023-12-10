init python:
    class CharacterBio:
        def __init__(self, name, description, is_mascot, sprite, stats=None):
            self.name = name
            self.description = description
            self.is_mascot = is_mascot
            self.sprite = sprite
            self.stats = stats

    character_bios = {
        "alban": CharacterBio(
            name="Alban Knox",
            description="An infamous phantom thief. His inherent nature \
makes him susceptible to trouble, but he's also a master of \
escape. Alban steals to support the slums, but most of the things \
he steals can't be sold and he is often scammed by the pawnbroker. \
For this reason, he also works part-time at a konbini.",
            is_mascot=False,
            sprite="sprites/alban/default.png",
            stats=rpg_characters["alban"],
        ),
        "briskadet": CharacterBio(
            name="Briskadet",
            description="An intelligent system in a chip, created as a \
form of protection for Sonny. Acting in part as Sonny's \
conscience, Briskadets work hard to maintain his sanity \
throughout his strenuous job.",
            is_mascot=True,
            sprite="misc/placeholder.png",
        ),
        "comfydant": CharacterBio(
            name="Comfydant",
            description="A sheep-shaped robot that acts as information \
storage. There are too many to count, but Fulgur usually keeps \
a black one and a white one around. Fulgur tends to act coldly \
towards them, but he still seems to dote on them in his own way.",
            is_mascot=True,
            sprite="misc/placeholder.png",
        ),
        "dead_protag": CharacterBio(
            # to be replaced with user-selected name
            name="Fake Protagonist",
            description="A top government agent previously on a mission \
to locate and secure a top secret item with huge implications. \
They were sent to work with Noctyx to save the future from a \
dangerous threat; unfortunately, the danger was too great and \
the mission cost them their life.",
            is_mascot=False,
            sprite="misc/placeholder.png",
            stats=rpg_characters["protag"],
        ),
        "fulgur": CharacterBio(
            name="Fulgur Ovid",
            description="A cyborg who carries out special missions \
for the government. A former soldier, he is often sent to the \
front line even though he's part of the logistics team. His base \
is a private ship that he was gifted for his many contributions. \
Out of spite towards the people he has to deal with on a daily \
basis, Fulgur occasionally sells information.",
            is_mascot=False,
            sprite="sprites/fulgur/default.png",
            stats=rpg_characters["fulgur"],
        ),
        "protag": CharacterBio(
            # to be replaced with user-selected name
            name="Fake Protagonist",
            description="A top government agent, on a mission to locate \
and secure a top secret item with huge implications. After a \
previous mission failure, they have been sent to work with \
Noctyx to save the future from a dangerous threat.",
            is_mascot=False,
            sprite="misc/placeholder.png",
            stats=rpg_characters["protag"],
        ),
        "sonny": CharacterBio(
            name="Sonny Brisko",
            description="An officer who is part of the VSF special forces. \
Privy to confidential government information, he is often tasked \
with killing special targets. He is implanted with a chip that \
controls his nerves, allowing him to be more resilient and strong \
but also making him less empathetic.",
            is_mascot=False,
            sprite="sprites/sonny/default.png",
            stats=rpg_characters["sonny"],
        ),
        "stargazer": CharacterBio(
            name="Stargazer",
            description="A plushie and Uki's mascot for his clothing line. \
Its design is fairly popular due to its round and friendly \
appearance. Uki is rarely seen without at least one by his side, \
and they seem to have a strong effect on his mental state.",
            is_mascot=True,
            sprite="misc/placeholder.png",
        ),
        "takaradachi": CharacterBio(
            name="Takaradachi",
            description="A failed mascot for the konbini. Alban pities them \
because he thinks they are both rather similar, so he likes to \
collect them whenever he sees one.",
            is_mascot=True,
            sprite="misc/placeholder.png",
        ),
        "uki": CharacterBio(
            name="Uki Violeta",
            description="A fashionista who owns a famous clothing store \
chain. He's also a psychic, although he tries to keep that hidden. \
Uki used to live in an orphanage in the slums, and he still \
visits occasionally, although he secretly dislikes the director. \
He is currently looking into opening a bar.",
            is_mascot=False,
            sprite="sprites/uki/default.png",
            stats=rpg_characters["uki"],
        ),
    }

    protag_alive = True
    current_character = character_bios["protag" if protag_alive else "dead_protag"]

image current_sprite:
    "[current_character.sprite]"
    zoom 0.6

screen character_bios():

    tag menu

    use game_menu(_("Character Bios")):

        vbox:
            frame:
                style "character_bio_frame"
                hbox:
                    hbox:
                        style "character_bio_sprite_hbox"
                        add "current_sprite" at truecenter
                    vbox:
                        style_prefix "character_bio_details"
                        label "[current_character.name]"
                        text "[current_character.description]"

                        hbox:
                            style_prefix "character_bio_stats"
                            if not current_character.is_mascot:
                                label "Character Stats"

                        frame:
                            style "character_bio_stats_frame"
                            if not current_character.is_mascot:
                                grid 4 3:
                                    style_prefix "character_bio_rpg_stats"
                                    xspacing 50

                                    label "HP"
                                    text "[current_character.stats.hp]"

                                    label "CRIT"
                                    text "[current_character.stats.crit]"

                                    label "ATK"
                                    text "[current_character.stats.atk]"

                                    label "ACC"
                                    text "[current_character.stats.acc]"

                                    label "DEF"
                                    text "[current_character.stats.defence]"

                                    label "EVD"
                                    text "[current_character.stats.evd]"

            frame:
                style_prefix "character_select"
                hbox:
                    if protag_alive:
                        imagebutton:
                            auto "misc/spy_%s.png"
                            action SetVariable("current_character", character_bios["protag"])
                    else:
                        imagebutton:
                            auto "misc/rip_%s.png"
                            action SetVariable("current_character", character_bios["dead_protag"])

                    imagebutton:
                        auto "misc/mask_%s.png"
                        action SetVariable("current_character", character_bios["alban"])
                    imagebutton:
                        auto "misc/mask_%s.png"
                        action SetVariable("current_character", character_bios["takaradachi"])

                    imagebutton:
                        auto "misc/sheep_%s.png"
                        action SetVariable("current_character", character_bios["fulgur"])
                    imagebutton:
                        auto "misc/sheep_%s.png"
                        action SetVariable("current_character", character_bios["comfydant"])

                    imagebutton:
                        auto "misc/chain_%s.png"
                        action SetVariable("current_character", character_bios["sonny"])
                    imagebutton:
                        auto "misc/chain_%s.png"
                        action SetVariable("current_character", character_bios["briskadet"])

                    imagebutton:
                        auto "misc/crystal_ball_%s.png"
                        action SetVariable("current_character", character_bios["uki"])
                    imagebutton:
                        auto "misc/crystal_ball_%s.png"
                        action SetVariable("current_character", character_bios["stargazer"])

style character_bio_frame is empty
style character_bio_sprite_hbox is default
style character_bio_details_vbox is default
style character_bio_details_label is gui_label
style character_bio_details_label_text is gui_label_text
style character_bio_details_text is gui_text

style character_bio_stats_frame is empty
style character_bio_stats_label is gui_label
style character_bio_stats_text is gui_text

style character_bio_rpg_stats_hbox is default
style character_bio_rpg_stats_grid is default
style character_bio_rpg_stats_label is gui_label
style character_bio_rpg_stats_label_text is gui_label_text
style character_bio_rpg_stats_text is gui_text

style character_select_frame is empty
style character_select_hbox is default
style character_select_button is gui_button

style character_bio_sprite_hbox:
    xsize 550
    xmargin 50
    ysize 550

style character_bio_details_vbox:
    xmargin 30
    yalign 0.0

style character_bio_details_label:
    bottom_margin 30

style character_bio_details_label_text:
    size 48

style character_bio_details_text:
    xsize 750
    size 30

style character_bio_stats_frame:
    yfill True

style character_bio_stats_label:
    ymargin 40
    size 36

style character_bio_rpg_stats_label_text:
    size 30

style character_bio_rpg_stats_text:
    xalign 0.5
    size 30

style character_select_frame:
    xfill True
    yalign 1.0
    yoffset -135

style character_select_hbox:
    xfill True
    spacing 20
