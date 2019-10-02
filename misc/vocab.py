from talon.voice import Context

# Remappings go in words.py, new vocab and deleting existing vocab goes in vocab.py

ctx = Context('vocab_amy')

ctx.vocab = [
    # important to keep this in alphabetical order!
    # 'batch effects',

    'amplicon',
    'anova',

    'bias',
    'biostat',
    'Bryan',

    'CAGs',
    'clinicians',
    'column', 'columns',
    'column space',
    'conda',
    'conda install',
    'conda activate',
    'confirmatory',
    'contig', 'contigs',
    'corncob',

    'Daniela',
    'deconvolve',
    'denoising',
    'devtools',
    'divnet',

    'eigendecomposition',
    'estimand',

    'gene',
    'generalized',
    'genome',
    'genomes',
    'genus',
    'Gitana',
    'github',
    'grant',
    'grants',

    'heteroskedastic',
    'homeworks',
    'homoskedastic',

    'idempotent',
    'identifiability',
    'inverse',
    'inverses',

    'lambda',

    'Mauricio',
    'metadata',
    'metagenome',
    'metagenomic',
    'metagenomics',
    'metaphlan',
    'MGS',
    'microbiome',
    'misc',
    'missingness',
    'mock',
    'modeling',

    'omics',
    'orthonormal'
    'OTU',

    'pangenomic',
    'pangenomics',
    'pangenome',
    'penalization',
    'Perlman',
    'phyla',
    'phylodivnet',
    'Poisson',
    'p-value',
    'p-values',

    'quantile', 'quantiles', 

    'rarefying',
    'reparameterize', 'reparameterizing', 'reparameterization',
    'resample', 'resamples',

    'rightarrow',

    'semidefinite',
    'semiparametric',

    'talon',
    'taxa',
    'taxon',
    'tibble',
    # 'theorem', 'theorems',

    'underdispersion',
    'unifrac',

    # Add American English :(
    'analyze',
    'analyzing',
    'generalize',
    'generalized',
    'itemize',
    'normalize',
    'organize',
    'organized',
    'rigorous',

]

ctx.vocab_remove = [
    'Brian',

    'Daniel',
    'Daniella',

    'filer',
    'Fareham'

    'Gino',
    'gonna',
    'Grant',
    'Grants',

    'improbability',

    'Jean',

    'Kaunda',

    'P value',
    'P values',
    'Pohlmann',

    'tax',
    'Tobias',
    'Theron',

    # Remove Australian English :(
    'analyse',
    'analysing',
    'generalise',
    'generalised',
    'itemise',
    'normalise',
    'organise',
    'organised',
    'rigourous',


]
