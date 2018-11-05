import os
# from talon.api import ffi
from talon.voice import Context, Key
# from talon import ctrl, applescript
# import time


    # tell application "System Events"
    #     tell process "Dragon"
    #         click menu bar item "Quit Dragon" of menu 1
    #     end tell
    # end tell

# def open_dragon_pad(m):
#     applescript.run(
#         """
#     tell application "System Events" to tell process "Dragon" to tell (menu bar item 1 of menu bar 3)
#     end tell
#     """
#     )



ctx = Context("dragon")
ctx.keymap({
    "drag restart": lambda m: os.system("killall Dragon; sleep 2; open /Applications/Dragon.app"),
    # "dragon": open_dragon_pad
})
