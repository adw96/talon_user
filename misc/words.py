from talon.voice import Context, Key, Str

ctx = Context('words')

# Remapping is go in words.py, new vocab and deleting existing vocab goes in vocab.py

keymap = {

    'batch of facts': 'batch effects',
    'beige and': 'Bayesian',
    'Peter': 'beta',

    # 'Kaunda': 'conda',

    'D-plier': 'dplyr',

    'hi dimensional': 'high dimensional',

    'Lavender': 'lambda',
    'Lander': 'lambda',

    'Maceo': 'Mauricio',
    'Mark': 'mock',


    'poison': 'Poisson',
    'python': 'python', 


    'stat Dev lab': 'Stat Div Lab',

    # 'Theron': 'theorem',
    # 'filer': 'phyla',
    # 'Tobias': 'to bias',
}

ctx.keymap(keymap)
