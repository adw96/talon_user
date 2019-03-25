from talon.voice import Context, Key, Str

ctx = Context('words')

# Remapping is go in words.py, new vocab and deleting existing vocab goes in vocab.py

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
    # 'filer': 'phyla',
    # 'Tobias': 'to bias',
}

ctx.keymap(keymap)
