from talon.voice import Context, Key, Str

ctx = Context('words')

# This is for remapping certain words to others
# Check out vocab.py for adding and removing vocab
keymap = {

    # 'batch of facts': 'batch effects',

    'D-plier': 'dplyr',

    'fee': 'phi',

    'Lavender': 'lambda',
    'Lander': 'lambda',

    'Mark': 'mock',

    'poison': 'Poisson',
}

ctx.keymap(keymap)
