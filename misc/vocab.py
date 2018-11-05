from talon.voice import Context

# I'm using this to replace my use of words.py
ctx = Context('vocab_amy')

ctx.vocab = [
    # important to keep this in alphabetical order!
    # 'batch effects',
    'Bryan',

    'CAGs',
    'corncob',

    'gene',
    'genome',
    'genomes',
    'genus',


    'metagenome',
    'metagenomic',
    'metagenomics',
    'mock', 
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
