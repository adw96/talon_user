#defines the commands that sleep/wake Talon
mode: all
-
^(welcome back)+$:
    user.mouse_wake()
    user.history_enable()
    user.talon_mode()
^sleep all$:
    user.switcher_hide_running()
    user.history_disable()
    user.homophones_hide()
    user.help_hide()
    user.mouse_sleep()
    speech.disable()
    user.engine_sleep()
^talon sleep [<phrase>]$: speech.disable()
^(talon wake)+$: speech.enable()

# #defines the commands that sleep/wake Talon
# mode: all
# -
# # ^welcome back$:
# #     user.mouse_wake()
# #     user.history_enable()
# #     user.talon_mode()
# # ^sleep all$:
# #     user.switcher_hide_running()
# #     user.history_disable()
# #     user.homophones_hide()
# #     user.help_hide()
# #     user.mouse_sleep()
# #     speech.disable()
# #     user.engine_sleep()

# ## sleep
# # ^go to sleep$: speech.disable()
# ^go to sleep$:
#     user.switcher_hide_running()
#     user.history_disable()
#     user.homophones_hide()
#     user.help_hide()
#     user.mouse_sleep()
#     speech.disable()
#     user.engine_sleep()


# ## wake
# ^be alert$: speech.enable()
# ^talon wake$: speech.enable()
