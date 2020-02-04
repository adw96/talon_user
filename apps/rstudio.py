## Amy Willis
## Many thanks to Sean Anderson for providing the backbone of this at:
# https://github.com/seananderson/talon-config/blob/master/rstudio.py

# - https://github.com/mrob95/MR-talon/blob/master/config/r.toml
# - https://github.com/seananderson/talon-config/blob/master/rstudio.py

from talon.voice import Word, Context, Key, Rep, Str, press
import time

ctx = Context('RStudio', bundle='org.rstudio.RStudio')


############## support for parsing numbers as command postfix

numeral_map = dict((str(n), n) for n in range(0, 20))
for n in [20, 30, 40, 50, 60, 70, 80, 90]:
    numeral_map[str(n)] = n
numeral_map["oh"] = 0 # synonym for zero

numerals          = ' (' + ' | '.join(sorted(numeral_map.keys())) + ')+'
optional_numerals = ' (' + ' | '.join(sorted(numeral_map.keys())) + ')*'

def text_to_number(m):

    tmp = [str(s).lower() for s in m._words]
    words = [parse_word(word) for word in tmp]

    result = 0
    factor = 1
    for word in reversed(words):
        if word not in numerals:
            # we consumed all the numbers and only the command name is left.
            break

        result = result + factor * int(numeral_map[word])
        factor = 10 * factor

    return result

def parse_word(word):
    word = word.lstrip('\\').split('\\', 1)[0]
    return word

def jump_to_bol(m):
    line = text_to_number(m)
    press('ctrl-g')
    time.sleep(0.35)        # DON'T MESS WITH THE LAG
    Str(str(line))(None)
    time.sleep(0.25)
    press('enter')

ctx.keymap({

# core functions
    'rambo':    Key('alt--'),
    'make function':     ['function {', Key('enter')],

    #### MOVING AROUND
    "spring" + numerals: jump_to_bol,       # Got this working January 31 2020!
    'trundle': Key('shift-cmd-c'),
    'comment this': Key('shift-cmd-c'),
    'reindent': Key('cmd-i'),
    'editor | (edit script) | (script editor)': Key('ctrl-1'),
    'console | (code prompt)': Key('ctrl-2'),

  # base R functions -- alphabetical by command
    'absolute value': 'abs(',
    'get working directory': 'getwd(',
    'function had': 'head(',
    'and Nicole': 'ncol(',
    'Andrew': 'nrow(',
    'set working directory': 'setwd(',
    'square root':  'sqrt(',
    'tibble':         'tibble(',

  # evaluating code
    'run it':        Key('cmd-enter'),

  # finding
    'Find and Replace':       Key('cmd-f'),
    'Find Next':        Key('cmd-g'),
    'Find Previous':    Key('cmd-shift-G'),

  # dplyr
    'D-plier select':         'select(',
    'D-plier mutate':         'mutate(',
    'D-plier summarise':      'summarize(',
    'D-plier filter':         'filter(',
    'D-plier rename':         'rename(',
    'D-plier group by':       'group_by(',
    'D-plier inner join':     'inner_join(',
    'D-plier left join':      'left_join(',
    'D-plier right join':      'right_join(',
    'D-plier bind rows':      'bind_rows(',
    'D-plier ungroup':      'ungroup(',
    'D-plier arrange':      'arrange(',
    'decreasing order':      'desc(',

  # ggplot
    'G G plot':    'ggplot(',
    'G G aesthetic':    'aes(',
    'geom point':       'geom_point(',
    'geom line':        'geom_line(',
    'geom violin':      'geom_violin(',
    'geom boxplot':     'geom_boxplot(',

  # knitr
    '(built PDF) | (build PDF)': Key('cmd-shift-k'),
    '(insert knitter chunk) | (insert chunk)':       Key('cmd-alt-i'),

  # magrittr
    'pipe': Key('cmd-shift-m'), ## RStudio's ' %>% '
    'pipe back': ' %<>% ',
    'pipe and': [' %>% ', Key('enter')],
})
