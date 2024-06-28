# ## take from https://raw.githubusercontent.com/AndreasArvidsson/andreas-talon/master/plugins/mode_indicator/mode_indicator.talon 
# ## on Oct 4 2023 by adw96

settings():
    # Don't show mode indicator by default
    user.mode_indicator_show = true
    # 30pixels diameter
    user.mode_indicator_size = 30
    # Center horizontally
    user.mode_indicator_x = 0.8325
    # Align top
    user.mode_indicator_y = 0
    # Slightly transparent
    user.mode_indicator_color_alpha = 0.7
    # Grey gradient
    user.mode_indicator_color_gradient = 0.5

    # ~~Black "000000"~~ red color for when the microphone is muted (set to "None")
    user.mode_indicator_color_mute = "000000"

    # # red for muted
    # user.mode_indicator_color_muted = "FF0000"
    # # green for listening
    # user.mode_indicator_color_listening = "3cb371"

    # ~~CornflowerBlue "6495ed"~~ green color for command mode
    user.mode_indicator_color_command = "3cb371"
    
    # Grey color for sleep mode
    user.mode_indicator_color_sleep = "808080"
    # Black color for disabled microphone
    user.mode_indicator_color_off = "000000"
    # Gold color for dictation mode
    user.mode_indicator_color_dictation = "ffd700"
    # MediumSeaGreen color for mixed mode
    user.mode_indicator_color_mixed = "3cb371"
    # GhostWhite color for other modes
    user.mode_indicator_color_other = "f8f8ff"
    