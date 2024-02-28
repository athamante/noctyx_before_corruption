
# This a screen with limited-time choice.
# Takes "time_max" as the maximum time for the choice and
# "fail_part" as the label to jump to when the time runs out.

screen death_or_live(time_max, fail_part):

    # Rollback is disabled and blocked for this screen.
    $ config.rollback_enabled = False

    default current_time = str(time_max)
    default time_limit = time_max

    vbox:
        xalign 0.5
        yalign 0.1
        text "[current_time]" # Current time as a string.

    # The timer is updated every 0.01 seconds.
    # When the time runs out, the screen is hidden and we jump to the fail_part label.
    timer 0.01 repeat True action If(time_limit > 0, true=[SetLocalVariable('time_limit', round((time_limit - 0.01),2)), SetLocalVariable('current_time', manual_timer_text(time_limit))], false=[Hide("death_or_live"),Jump(fail_part)])

    $ renpy.block_rollback()
    $ config.rollback_enabled = True

init python:

    # This function is used to format the time as a string, to avoid a flickering effect.
    def manual_timer_text(time_value):
        time_text = str(time_value)
        if time_text.find(".") == -1:
                time_text += "."
        while len(time_text) < time_text.find(".") + 3:
            time_text = time_text + "0"
        
        return time_text
        