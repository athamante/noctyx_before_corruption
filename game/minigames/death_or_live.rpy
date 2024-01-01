init python in timedchoice:
    def death_or_live_choice(list_of_choices, time_limit, renpy):
        start_time = renpy.time.time()

        result = renpy.display_menu(list_of_choices)

        elapsed_time = renpy.time.time() - start_time
        
        if elapsed_time > time_limit:
            return False
        return result
