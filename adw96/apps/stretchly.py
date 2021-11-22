import appscript
from talon import Module, actions
mod = Module()
@mod.action_class
class Actions:
    def stretchly_menu():
        "Activate the stretchly menu"
        x, y = appscript.app('System Events').processes['Stretchly'].menu_bars[2].position()
        actions.mouse_move(x, y)
        actions.mouse_click()
    def stretchly_long_break():
        "Activate a stretchly long break"
        actions.user.stretchly_menu()
        actions.key("down down down right enter")

    def talon_menu():
        "Activate the talon menu"
        x, y = appscript.app('System Events').processes['Talon'].menu_bars[2].position()
        actions.mouse_move(x, y)
        actions.mouse_click()
    def quit_talon():
        "Quit talon"
        actions.user.talon_menu()
        actions.key("down down down down down down down down down down enter")
