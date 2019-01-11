from talon.voice import Context

# I'm using this to replace my use of words.py
ctx = Context('vocab_amy')

ctx.vocab = [
    # important to keep this in alphabetical order!
    # 'batch effects',
    'Bryan',

    'CAGs',
    'confirmatory',
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

    'Poisson',
    'p-value',
    'p-values',

    'rarefying',
    
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

    'P value',
    'P values',

    'tax',

]
