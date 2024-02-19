screen death_or_live(time_limit, fail_part):

    timer 1.0 repeat True action If(time_limit > 0, true=SetVariable('time_limit', time_limit - 1.0), false=[Hide("death_or_live"),Jump(fail_part)])
