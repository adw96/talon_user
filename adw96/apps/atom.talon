app.name: Atom
-
### see also atom-latex.talon

alex right:
    key(cmd-k)
    key(cmd-right)
alex left:
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
select line <user.number_string>$:
    key(ctrl-g)
    insert(user.number_string)
    key(enter)
    key(cmd-l)
    key(cmd-l)

trundle:
    key(cmd-/)

# text
apostrophe ess:
    insert("'")
    key(delete)
    insert("s")
