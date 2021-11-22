app.name: Atom
-
build pdf:
    key(cmd-.)
insert italics:
    insert("\\textit{}")
    key(left)
insert bold text:
    insert("\\textbf{}")
    key(left)
insert item: "\\item "
(framework itemize) | (itemize framework):
    key(cmd-left)
    insert("\\begin{}")
    key(left)
    insert("itemize")
    key(right)
    key(enter)
    key(enter)
    insert("\\end{}")
    key(left)
    insert("itemize")
    key(up)
    key(tab)
    insert("\item ")
(framework enumerate) | (enumerate framework):
    key(cmd-left)
    insert("\\begin{}")
    key(left)
    insert("enumerate")
    key(right)
    key(enter)
    key(enter)
    insert("\\end{}")
    key(left)
    insert("enumerate")
    key(up)
    key(tab)
    insert("\item ")
(framework align) | (align framework):
    key(cmd-left)
    insert("\\begin{}")
    key(left)
    insert("align")
    key(right)
    key(enter)
    key(enter)
    insert("\\end{}")
    key(left)
    insert("align")
    key(up)
    key(tab)
