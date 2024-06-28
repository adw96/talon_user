swipe: ", "
tinker: "`"
colon space: ": "
semi space: "; "
pausa: " -- "
deplush: " + "
deminus: " - "
apostrophe ess: "'s"
# (bracket | brack | left bracket): "{"
# (rbrack | are bracket | right bracket): "}"
# gravy:
#     insert("```")
# (dot dot | dotdot): ".."
# biosketch: insert("Biosketch") #ffs
(ellipses | dotdotdot | dot dot dot): "..."
args:
	insert("()")
	key(left)
brax:
	insert("[]")
	key(left)
brace:
	insert("{}")
	key(left)
(bracket | brace) that:
    text = edit.selected_text()
    user.paste("{{{text}}}")
args that:
    text = edit.selected_text()
    user.paste("({text})")
quote that:
    text = edit.selected_text()
    user.paste('"{text}"')
# angle that:
#     text = edit.selected_text()
#     user.paste("<{text}>")
# (grave | back tick) that:
#     text = edit.selected_text()
#     user.paste('`{text}`')
