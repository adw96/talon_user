## Amy Willis
## Many thanks to Sean Anderson for providing the backbone of this at:
# https://github.com/seananderson/talon-config/blob/master/rstudio.py

from talon.voice import Word, Context, Key, Rep, Str, press
import time

ctx = Context('RStudio', bundle='org.rstudio.RStudio')

############# support for parsing numbers as command postfix

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


######### actions and helper functions

######### actions and helper functions
def jump_to_bol(m):
    line = text_to_number(m)
    press('cmd-shift-alt-g')
    time.sleep(0.15)
    Str(str(line))(None)
    press('enter')

def jump_to_end_of_line():
    press('cmd-right')

def jump_to_beginning_of_text():
    press('cmd-left')

def jump_to_nearly_end_of_line():
    press('left')

def jump_to_bol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        else:
            press('ctrl-a')
            press('cmd-left')
        then()
    return fn

def jump_to_eol_and(then):
    def fn(m):
        if len(m._words) > 1:
            jump_to_bol(m)
        press('cmd-right')
        then()
    return fn

def toggle_comments(*unneeded):
   Key('cmd-shift-c')

ctx.keymap({

#### MOVING AROUND
    'spring' + numerals: jump_to_bol,
    # 'trundle': toggle_comments,
    # 'trundle' + numerals: jump_to_bol_and(toggle_comments),
    'trundle':         Key('cmd-shift-C'),
    'reindent':         Key('cmd-i'),

  # base R functions
    'get working directory':    ['getwd()', Key('left')],
    'set working directory':    ['setwd()', Key('left')],
    'square root':    ['sqrt()', Key('left')],

    '(assign that) | rambo':    Key('alt--'),

    'make function':     ['function {}', Key('left'), Key('enter')],
    'R data frame':     'data.frame(',
    'R tibble':         'tibble(',

  # evaluating code
    'evaluate':        Key('cmd-enter'),
    'run it':        Key('cmd-enter'),
    # 'evaluate previous':     Key('cmd-shift-P'),
    # 'evaluate from top':     Key('cmd-alt-b'),
    # 'evaluate to end':       Key('cmd-alt-e'),
    # 'evaluate (function|funk)':    Key('cmd-alt-f'),
    # 'evaluate (previous|preeve) chunks': Key('cmd-alt-p'),
    # 'evaluate chunk':        Key('cmd-alt-c'),
    # 'evaluate next chunk':         Key('cmd-alt-n'),
    # 'evaluate all':          Key('cmd-shift-S'),

  # finding
    'Find and Replace':       Key('cmd-f'),
    'Find Next':        Key('cmd-g'),
    'Find Previous':    Key('cmd-shift-G'),

##### PACKAGES

  # dplyr
    'D-plier select':         'select(',
    'D-plier mutate':         'mutate(',
    'D-plier summarise':      'summarize(',
    'D-plier filter':         'filter(',
    'D-plier rename':         'rename(',
    'D-plier group by':       'group_by(',
    'D-plier inner join':     'inner_join(',
    'D-plier left join':      'left_join(',
    'D-plier bind rows':      'bind_rows(',
    'D-plier ungroup':      'ungroup(',

  # ggplot
    'G G plot':    'ggplot(',
    'G G aesthetic':    'aes(',
    'geom point':       'geom_point(',
    'geom line':        'geom_line(',
    'geom point':       'geom_point(',
    'geom segment':     'geom_segment(',
    'geom bar':         'geom_bar(',
    'geom area':        'geom_area(',
    'geom violin':      'geom_violin(',
    'geom boxplot':     'geom_boxplot(',
    'geom polygon':     'geom_polygon(',
    'geom (ab|A B) line':     'geom_abline(',
    'geom horizontal line':   'geom_hbline(',
    'geom vertical line':     'geom_vbline(',
    'G G ex label':     'xlab(',
    'G G why label':    'ylab(',

  # knitr

    'build PDF':       Key('cmd-shift-k'),
    'insert knitter chunk':       Key('cmd-alt-i'),

  # magrittr

    'pipe': Key('cmd-shift-m'), ## RStudio's ' %>% '
    'pipe back': ' %<>% ',
    'pipe and': [' %>% ', Key('enter')],
})
