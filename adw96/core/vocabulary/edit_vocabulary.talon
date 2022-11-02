mode: command
mode: dictation
-
add to vocab [as <phrase>]$: user.add_selection_to_vocabulary(phrase or "")
# Automatically adds possessive form by appending "'s".
add name to vocab [as <phrase>]$:
    user.add_selection_to_vocabulary(phrase or "", "name")
# Automatically adds plural form by simply appending "s".
add noun to vocab [as <phrase>]$:
    user.add_selection_to_vocabulary(phrase or "", "noun")
add to replacements as <phrase>$: user.add_selection_to_words_to_replace(phrase)
# Automatically adds possessive form by appending "'s".
add name to replacements as <phrase>$:
    user.add_selection_to_words_to_replace(phrase, "name")
# Automatically adds plural form by simply appending "s".
add noun to replacements as <phrase>$:
    user.add_selection_to_words_to_replace(phrase, "noun")
