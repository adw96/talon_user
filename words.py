from talon.voice import Context, Key

ctx = Context('amywords')

keymap = {

# names
  'brian': ' Bryan',
  'daniella': ' Daniela',

# software
  'corn cob': 'corncob',

# statistics
  'spine p values': 'p-values',

# microbiome
  'janice': 'genus',
  'matter genomics': 'metagenomics',
  'meta- genomics': 'metagenomics',
  'cags': 'CAGs',


    # 'word get hub': 'github',
    # 'title get hub': 'GitHub',
}

ctx.keymap(keymap)
