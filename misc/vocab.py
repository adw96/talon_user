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

    'Daniela',

    'gene',
    'genome',
    'genomes',
    'genus',


    'metagenome',
    'metagenomic',
    'metagenomics',
    'metaphlan',
    'mock',
    'modeling',

    'OTU',

    'pangenomic',
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
    'Daniella',

    'Gino',

    'Jean',

    'P value',
    'P values',

    'tax',

]
