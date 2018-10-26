from talon.voice import Context

# I'm using this to replace my use of words.py
ctx = Context('vocab_amy')

ctx.vocab = [
    # important to keep this in alphabetical order!
    'Bryan',

    'CAGs',
    'corncob',

    'gene',
    'genome',
    'genus',


    'metagenome',
    'metagenomic',
    'metagenomics',
    'modeling',

    'OTU',

    'p-value',
    'p-values',

    'talon',
    'taxa',
    'taxon',
    'tibble',


]

ctx.vocab_remove = [
    'Brian',

    'Daniel',

    'Gino',

    'Jean',

    'modelling',

    'P value',
    'P values',

    'tax',

]
