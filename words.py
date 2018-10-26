from talon.voice import Context, Key, Str

ctx = Context('words')

# This is for remapping certain words to others
# Check out vocab.py for adding and removing vocab
keymap = {

    'D-plier': 'dplyr',

    'fee': 'phi',



}

ctx.keymap(keymap)
