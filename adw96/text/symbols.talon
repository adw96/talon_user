biosketch: insert("Biosketch") #ffs
swipe: ", "
tinker: "`"
colon space: ": "
semi space: "; "
pausa: " -- "
deplush: " + "
deminus: " - "
apostrophe ess: "'s"
(bracket | brack | left bracket): "{"
(rbrack | are bracket | right bracket): "}"
gravy:
    insert("```")
(dot dot | dotdot): ".."
ellipses: "..."
args:
	insert("()")
	key(left)
brax:
	insert("[]")
	key(left)
kirk:
	insert("{}")
	key(left)
angle that:
    text = edit.selected_text()
    user.paste("<{text}>")
(bracket | brace) that:
    text = edit.selected_text()
    user.paste("{{{text}}}")
args that:
    text = edit.selected_text()
    user.paste("({text})")
quote that:
    text = edit.selected_text()
    user.paste('"{text}"')
(grave | back tick) that:
    text = edit.selected_text()
    user.paste('`{text}`')
