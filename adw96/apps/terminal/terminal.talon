app: apple_terminal
-
#comment or remove tags for command sets you don't want
tag(): user.file_manager
tag(): user.generic_terminal
tag(): user.git
# tag(): user.kubectl
tag(): user.tabs
tag(): terminal


(search | look) for something:
    insert("grep -rnw . -e ''")
    key(left)
abandon that:
    key(ctrl-c)
(go to | open) talon directory:
    insert("cd /Users/amy/.talon/user/talon_user/adw96")
    key(enter)
open finder here:
    insert("open .")
    key(enter)

# rerun search:
#     key(ctrl-r)
# suspend:
#     key(ctrl-z)
