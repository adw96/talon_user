from talon.voice import Context, Key, Str

ctx = Context('words')

# This is for remapping certain words to others
# Check out vocab.py for adding and removing vocab
keymap = {

    'batch of facts': 'batch effects',
    'bays': 'Bayes',
    'beige and': 'Bayesian',

    'D-plier': 'dplyr',

    'fee': 'phi',

    'hi dimensional': 'high dimensional',

    'Lavender': 'lambda',
    'Lander': 'lambda',

    'Maceo': 'Mauricio',
    'Mark': 'mock',

    'poison': 'Poisson',
    'filer': 'phyla', 
    # 'Tobias': 'to bias',
}

ctx.keymap(keymap)
