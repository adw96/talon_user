from talon.voice import Context

# Remappings go in words.py, new vocab and deleting existing vocab goes in vocab.py

ctx = Context('vocab_amy')

ctx.vocab = [
    # important to keep this in alphabetical order!
    # 'batch effects',

    'anova',

    'bias',
    'Bryan',

    'CAGs',
    'confirmatory',
    'corncob',

    'Daniela',
    'denoising',
    'divnet',

    'estimand',

    'gene',
    'genome',
    'genomes',
    'genus',
    'Gitana',

    'identifiability',

    'lambda',

    'Mauricio',
    'metagenome',
    # 'metagenomic',
    'metagenomics',
    'metaphlan',
    'MGS',
    'microbiome',
    'misc',
    'mock',
    'modeling',

    'omics',
    'OTU',

    'pangenomic',
    'phyla',
    'phylodivnet',
    'Poisson',
    'p-value',
    'p-values',

    'rarefying',

    'talon',
    'taxa',
    'taxon',
    'tibble',

    'unifrac',

    # Add American English :(
    'analyze', 'analyzing',
    'generalize', 'generalized',
    'itemize',
    'rigorous',

]

ctx.vocab_remove = [
    'Brian',

    'Daniel',
    'Daniella',

    'filer',

    'Gino',
    'gonna',

    'Jean',

    'P value',
    'P values',

    'tax',
    'Tobias',

    # Remove Australian English :(
    'analyse', 'analysing',
    'generalise', 'generalised',
    'itemise',
    'rigourous',


]
