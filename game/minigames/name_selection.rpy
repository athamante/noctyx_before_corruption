init python in namelib:
    renpy.image("cg a_easter", "cgs/alban_easteregg.png")
    renpy.image("cg f_easter", "cgs/fulgur_easteregg.png")
    renpy.image("cg s_easter", "cgs/sonny_easteregg.png")
    renpy.image("cg u_easter", "cgs/uki_easteregg.png")


    def crash(img):
        renpy.scene()
        renpy.show(img)
        renpy.pause(1)
        renpy.quit()

    def message(str):
        renpy.say(who=None, what=str)
        return False

    def naming():
        alban = ["alban", "knox", "albie",
            "albanyan", "auruban", "aruban",
            "aeko-chan", "phantom", "thief",
            "takaradachi", "alice",]
        alban_crash = ["konbini-kun",]

        fulgur = ["fulgur", "ovid", "fungus",
            "fblong", "fulgar", "fuuchan",
            "fuufuuchan", "fufuchan", "borg",
            "tea kettle", "hey", "legatus",
            "alan binc", "ian binc", "ovidia",
            "archivist", "cyborg", "sheero",
            "bleep", "comfydant", "dog",
            "kat", "cat",]
        fulgur_crash = ["dad", "daddy", "papa",]

        sonny = ["sonny", "brisko", "sani",
            "sanni", "onii-chan", "my money",
            "vsf", "officer", "police",
            "briskadet", "krill",]
        sonny_crash = ["my man",]

        uki = ["uki", "violeta", "violetta",
            "ukiki", "my cookie", "mama",
            "mom", "mommy", "mitch",
            "marot", "twink", "girlboss",
            "feminism", "psychic", "gay",
            "gaymen", "deja vu", "starlight",
            "stargazer", "ukinya",]
        uki_crash = ["old", "oldge", "grandpa",
            "grandma", "fossil", "bald",]

        noctyx = ["noctyx", "nocturnal", "knock dicks",
            "dick knockers", "yugo", "asuma",]
        lazulight = ["lazulight", "pomu", "rainpuff",
            "elira", "pendora", "finana",
            "ryugu",]
        obsydia = ["obsydia", "selen", "tatsuki",
            "rosemi", "lovelock", "petra",
            "gurin",]
        ethyria = ["ethyria", "millie", "parfait",
            "enna", "alouette", "reimu",
            "endou", "nina", "kosaka",
            "nani kuso",]
        luxiem = ["luxiem", "vox", "akuma",
            "voxxy", "ike", "eveland",
            "ikey", "man of sex", "mysta",
            "rias", "luca", "kaneshiro",
            "lucaur", "shu", "yamino",
            "shoe", "shubert",]
        iluna = ["iluna", "kyo", "kaneko",
            "scarle", "yonaguni", "aia",
            "amare", "ren", "zotto",
            "aster", "arcadia", "maria",
            "marionette",]
        xsoleil = ["xsoleil", "doppio", "dropscythe",
            "ver", "vermillion", "hex",
            "haywire", "kotoka", "torahime",
            "meloco", "kyoran", "kyouran",
            "zaion", "lanza",]
        krisis = ["krisis", "vanta", "vantacrow",
            "bringer", "zali", "vezalius",
            "bandage", "yu", "q",
            "wilson",]
        ttt = ["ttt", "triple t", "kunai",
            "nakasato", "vivi", "victoria",
            "brightshield", "claude", "clawmark",]
        ships = ["psyborg", "sonnyban", "saniban",
            "robocop", "ukitty", "violisko",
            "knovid",]

        # loop for making sure player doesn't use 'forbidden' name
        while True:
            mobname = renpy.input("What is your name?", default='Mob-kun', length=32, exclude="0123456789+=,.?!<>{}[]").strip()
            mobname_lower = mobname.lower()
            name_ok = True

            if not mobname:
                mobname = "Mob-kun"
                return mobname

            # organizing the name in a list to make sure every part and joined parts (max 3) are checked
            mobname_list = mobname_lower.split(" ")

            for part in mobname_list:
                if "'s" in part:
                    idx = mobname_list.index(part)
                    mobname_list[idx] = part[:-2]

            for i in range(len(mobname_list) - 1):
                mobname_list.append(f"{mobname_list[i]} {mobname_list[i+1]}")

            if len(mobname_list) > 2:
                for i in range(len(mobname_list) - 2):
                    mobname_list.append(f"{mobname_list[i]} {mobname_list[i+1]} {mobname_list[i+2]}")


            for name in mobname_list:
                if name in alban:
                    name_ok = message("First your heart, then your name.")
                    break

                elif name in alban_crash:
                    crash("cg a_easter")

                elif name in fulgur:
                    name_ok = message("Sorry, I can’t read you.")
                    break

                elif name in fulgur_crash:
                    crash("cg f_easter")

                elif name in sonny:
                    name_ok = message("Don’t make us use lethal force.")
                    break

                elif name in sonny_crash:
                    crash("cg s_easter")

                elif name in uki:
                    name_ok = message("Keep your eyes on the goal.")
                    break

                elif name in uki_crash:
                    crash("cg u_easter")

                elif name in noctyx:
                    name_ok = message("Still stuck in the abyss?")
                    break

                elif name in lazulight:
                    name_ok = message("Not a Diamond City, but it has lights.")
                    break

                elif name in obsydia:
                    name_ok = message("A Blackout is close to an abyss.")
                    break

                elif name in ethyria:
                    name_ok = message("We still see all.")
                    break

                elif name in luxiem:
                    name_ok = message("Are you like a bee that seeks honey?")
                    break

                elif name in iluna:
                    name_ok = message("Do you want the game to get started now?")
                    break

                elif name in xsoleil:
                    name_ok = message("We would be taking off if a proper name was chosen.")
                    break

                elif name in krisis:
                    name_ok = message("Maybe you should just be named Kris.")
                    break

                elif name in ttt:
                    name_ok = message("Did you know a possible reason why isekai titles are so long is because it can convey the entire plot with just a glance?")
                    break

                elif name in ships:
                    name_ok = message("Locked in, no stopping, you feel like you’re sitting in the cockpit.")
                    break


            if name_ok:
                return mobname
