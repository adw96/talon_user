from talon.voice import Key, Context, Str, press


def go_to_path(path):
    def path_function(m):
        press("cmd-shift-g")
        Str(path)(None)
        press("return")

    return path_function


ctx = Context("Finder", bundle="com.apple.finder")
ctx.keymap(
    {
        # actions
        "delete that": Key("cmd-backspace"),
        "show package contents": Key("cmd-alt-o"),

        # navigation
        "all files": Key("cmd-shift-f"),
        "go to": Key("cmd-shift-g"),
        "find desktop": Key("cmd-shift-d"),
        "find documents": Key("cmd-shift-o"),
        "find downloads": Key("cmd-shift-l"),
        "find applications": Key("cmd-shift-a"),
        "find talon": go_to_path("~/.talon/user"),
        "find research": go_to_path("/Users/adwillis/research"),
        "find grants": go_to_path("/Users/adwillis/grants"),
    }
)
