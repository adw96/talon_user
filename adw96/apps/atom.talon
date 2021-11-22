app.name: Atom
-
pane right:
    key(cmd-k)
    key(cmd-right)
pane left:
    key(cmd-k)
    key(cmd-left)
go to line <user.number_string>$:
    key(ctrl-g)
    insert(user.number_string)
    key(enter)
spring <user.number_string>$:
    key(ctrl-g)
    insert(user.number_string)
    key(enter)
comment line <user.number_string>$:
    key(ctrl-g)
    insert(user.number_string)
    key(enter)
    key(cmd-/)
delete line <user.number_string>$:
    key(ctrl-g)
    insert(user.number_string)
    key(enter)
    key(ctrl-shift-k)

trundle:
    key(cmd-/)

# text
apostrophe ess:
    insert("'")
    key(delete)
    insert("s")
