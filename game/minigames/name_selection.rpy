init python in namelib:
    renpy.image("cg a_easter", "cgs/alban_easteregg.png")
    renpy.image("cg f_easter", "cgs/fulgur_easteregg.png")
    renpy.image("cg s_easter", "cgs/sonny_easteregg.png")
    renpy.image("cg u_easter", "cgs/uki_easteregg.png")

    def naming():
        alban = ["Alban", "Knox", "Albie",
            "Albanyan", "Auruban", "Aruban",
            "Neko-chan", "Phantom", "Thief",
            "Takaradachi", "Alice",]
        alban_crash = ["Konbini-kun",]

        fulgur = ["Fulgur", "Ovid", "Fungus",
            "Oblong", "Fulgar", "Fuuchan",
            "Fuufuuchan", "Fufuchan", "Borg",
            "Tea Kettle", "Hey", "Legatus",
            "Alan Binc", "Ian Binc", "Ovidia",
            "Archivist", "Cyborg", "Sheero",
            "Bleep", "Comfydant", "Dog",
            "Kat", "Cat",]
        fulgur_crash = ["Dad", "Daddy", "Papa",]

        sonny = ["Sonny", "Brisko", "Sani",
            "Sanni", "Onii-chan", "My Honey",
            "VSF", "Officer", "Police",
            "Briskadet", "Krill",]
        sonny_crash = ["My Man",]

        uki = ["Uki", "Violeta", "Violetta",
            "Ukiki", "My Cookie", "Mama",
            "Mom", "Mommy", "Bitch",
            "Tarot", "Twink", "Girlboss",
            "Feminism", "Psychic", "Gay",
            "Gaymen", "Deja vu", "Starlight",
            "Stargazer", "Ukinya",]
        uki_crash = ["Old", "Oldge", "Grandpa",
            "Grandma", "Fossil", "Bald",]

        noctyx = ["Noctyx", "Nocturnal", "Knock Dicks",
            "Dick Knockers", "Yugo", "Asuma",]
        lazulight = ["Lazulight", "Pomu", "Rainpuff",
            "Elira", "Pendora", "Finana",
            "Ryugu",]
        obsydia = ["Obsydia", "Selen", "Tatsuki",
            "Rosemi", "Lovelock", "Petra",
            "Gurin",]
        ethyria = ["Ethyria", "Millie", "Parfait",
            "Enna", "Alouette", "Reimu",
            "Endou", "Nina", "Kosaka",
            "Nani Kuso",]
        luxiem = ["Luxiem", "Vox", "Akuma",
            "Voxxy", "Ike", "Eveland",
            "Ikey", "Man of Sex", "Mysta",
            "Rias", "Luca", "Kaneshiro",
            "Lucaur", "Shu", "Yamino",
            "Shoe", "Shubert",]
        iluna = ["Iluna", "Kyo", "Kaneko",
            "Scarle", "Yonaguni", "Aia",
            "Amare", "Ren", "Zotto",
            "Aster", "Arcadia", "Maria",
            "Marionette",]
        xsolei = ["XSoleil", "Doppio", "Dropscythe",
            "Ver", "Vermillion", "Hex",
            "Haywire", "Kotoka", "Torahime",
            "Meloco", "Kyoran", "Kyouran",
            "Zaion", "Lanza",]
        krisis = ["Krisis", "Vanta", "Vantacrow",
            "Bringer", "Zali", "Vezalius",
            "Bandage", "Yu", "Q",
            "Wilson",]
        ttt = ["TTT", "Triple T", "Kunai",
            "Nakasato", "Vivi", "Victoria",
            "Brightshield", "Claude", "Clawmark",]
        ships = ["Psyborg", "Sonnyban", "Saniban",
            "Robocop", "Ukitty", "Violisko",
            "Knovid",]

        # loop for making sure player doesn't use 'forbidden' name
        while True:
            mobname = renpy.input("What is your name?", default='Mob-kun', length=32, exclude="0123456789+=,.?!<>{}[]").strip()

            if not mobname:
                mobname = "Mob-kun"
                return mobname

            elif mobname in alban:
                renpy.say(who=None, what="First your heart, then your name.")

            elif mobname in alban_crash:
                renpy.scene()
                renpy.show("cg a_easter")
                renpy.pause(1)
                renpy.quit()

            elif mobname in fulgur:
                renpy.say(who=None, what="Sorry, I can’t read you.")

            elif mobname in fulgur_crash:
                renpy.scene()
                renpy.show("cg f_easter")
                renpy.pause(1)
                renpy.quit()

            elif mobname in sonny:
                renpy.say(who=None, what="Don’t make us use lethal force.")

            elif mobname in sonny_crash:
                renpy.scene()
                renpy.show("cg s_easter")
                renpy.pause(1)
                renpy.quit()

            elif mobname in uki:
                renpy.say(who=None, what="Keep your eyes on the goal.")

            elif mobname in uki_crash:
                renpy.scene()
                renpy.show("cg u_easter")
                renpy.pause(1)
                renpy.quit()

            elif mobname in noctyx:
                renpy.say(who=None, what="Still stuck in the abyss?")

            elif mobname in lazulight:
                renpy.say(who=None, what="Not a Diamond City, but it has lights.")

            elif mobname in obsydia:
                renpy.say(who=None, what="A Blackout is close to an abyss.")

            elif mobname in ethyria:
                renpy.say(who=None, what="We still see all.")

            elif mobname in luxiem:
                renpy.say(who=None, what="Are you like a bee that seeks honey?")

            elif mobname in iluna:
                renpy.say(who=None, what="Do you want the game to get started now?")

            elif mobname in xsolei:
                renpy.say(who=None, what="We would be taking off if a proper name was chosen.")

            elif mobname in krisis:
                renpy.say(who=None, what="Maybe you should just be named Kris.")

            elif mobname in ttt:
                renpy.say(who=None, what="Did you know a possible reason why isekai titles are so long is because it can convey the entire plot with just a glance?")

            elif mobname in ships:
                renpy.say(who=None, what="Locked in, no stopping, you feel like you’re sitting in the cockpit.")

            else:
                return mobname
