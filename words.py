from talon.voice import Context, Key, Str

ctx = Context('words')
def shrink_word(m):
    word = str(m.dgndictation[0]._words[0]).lower()
    if not word in shrink_map:
        raise Exception('%s not in shrink map' % word)
    Str(shrink_map[word])(None)

keymap = {
    # # abbreviations
    # 'e jee': 'e.g., ',

    # names
      'brian': 'Bryan',
      'daniella': 'Daniela',

    # software
      'corn cob': 'corncob',

    # statistics
      'p values': 'p-values',
      'p value': 'p-value',

    # microbiome
      'cags': 'CAGs',
      'janice': 'genus',
      '(matter genomics) | (meta- genomics)': 'metagenomics',
      '(matter genomic) | (meta- genomic)': 'metagenomic',
      '(matter genome) | (meta- genome)': 'metagenome',
      'g nine': 'genome', 

    'shrink <dgndictation>': shrink_word,
}

shrink_map = {

    'administrator': 'admin',
    'et cetera': 'etc.',

}

ctx.keymap(keymap)
