# The script of the game goes in this file.
init python:
    from store.namelib import name_selection_controller
    from store.timedchoice import death_or_live_choice
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Let's test out naming system."

    $ name_selection_controller.run_name_selection()

    protagonist "I'm [name_selection_controller.mobname]."

    $ achievement_tracker.complete_achievement("Fake Protagonist")

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "Let's test out the dress-up minigame."

    scene clothing_store
    call screen dress_up_minigame

    show eileen happy

    e "Did you have fun picking an outfit?"

    $ add_to_journal("kat_virus")
    $ add_to_journal("test_info_enabled")

    $ pov_tracker.switch_pov("fulgur")

    e "Let's test the information screen. Try clicking the Nijisanji logo in the top left."

    e "This information screen can also be opened from the menu."

    e "You now have to make a choice within a time limit."

    $ list_of_choices = [ ("choice 1", "result1"), ("choice 2", "result2"), ("choice 3", "result3") ]

    $ result = death_or_live_choice(list_of_choices, 2, renpy)

    if result == False:
        "Game Over"
        return
    else:
        "in time limit"
        $ narrator(result)


    $ achievement_tracker.complete_achievement("True Ending")

    # This ends the game.

    return
