from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

# cleans up some Dragon output from <dgndictation>
mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
# used for auto-spacing
punctuation = set('.,-!?')

def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out

def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))

def insert(s):
    Str(s)(None)

def text(m):
    # Added 10/9/18 because I want 'I' words to be capitalised automatically
    insert(join_words(parse_words(m)))
    # insert(join_words(parse_words(m)).lower())


def sentence_text(m):
    # text = join_words(parse_words(m)).lower() ## from repo
    # Added 10/9/18 because I want 'I' words to be capitalised  automatically
    text = join_words(parse_words(m))
    insert(text.capitalize())

def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())

def surround(by):
    def func(i, word, last):
        if i == 0: word = by + word
        if last: word += by
        return word
    return func

def rot13(i, word, _):
    out = ''
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        out += c
    return out

formatters = {
    'dunder': (True,  lambda i, word, _: '__%s__' % word if i == 0 else word),
    'camel':  (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'snake':  (True,  lambda i, word, _: word if i == 0 else '_'+word),
    'smash':  (True,  lambda i, word, _: word),
    # spinal or kebab?
    'spine':  (True,  lambda i, word, _: word if i == 0 else '-'+word),
    'sentence':  (False, lambda i, word, _: word.capitalize() if i == 0 else word),
    'title':  (False, lambda i, word, _: word.capitalize()),
    # 'squash':  (False, lambda i, word, _: word.lower()),
    'allcaps': (False, lambda i, word, _: word.upper()),
    'dubstring': (False, surround('"')),
    'string': (False, surround("'")),
    'padded': (False, surround(" ")),
    'rot-thirteen':  (False, rot13),
}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press('cmd-c')
        words = s.get().split(' ')
        if not words:
            return

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)

def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify('Copied app bundle', body='{}'.format(bundle))

ctx = Context('input')
ctx.keymap({
    'say <dgndictation> [over]': text,
    'phrase <dgndictation> [over]': text,
    # TODO: try to rewire myself
    # 'phrase <dgndictation> [over]': text,

    'sentence <dgndictation> [over]': sentence_text,
    'comma <dgndictation> [over]': [', ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],
    'space <dgndictation> [over]': [' ', text],
    'word <dgnwords>': word,

    '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    # more keys and modifier keys are defined in basic_keys.py

    'slap': [Key('cmd-right enter')],
    '(question | questo)': '?',
    'swipe': ', ',
    'tilde': '~',
    '(bang | exclamation point)': '!',
    'dollar [sign]': '$',
    'crunder': '_',
    'colon': ':',
    '(paren | left paren)': '(', '(rparen | are paren | right paren)': ')',
    '(brace | left brace)': '{', '(rbrace | are brace | right brace)': '}',
    '(angle | left angle | less than)': '<', '(rangle | are angle | right angle | greater than)': '>',

    '(star | asterisk)': '*',
    '(pound | pounder | hash [sign] | octo | thorpe | number sign)': '#',
    'percy': '%',
    'caret': '^',
    'loco': '@',
    '(and sign | ampersand | amper)': '&',
    'spike': '|',

    '(dubquote | double quote)': '"',
    'triple quote': "'''",

    '(dot dot | dotdot)': '..',
    'cd': 'cd ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),

    'run make (durr | dear)': 'mkdir ',
    'run get': 'git ',
    'run get (R M | remove)': 'git rm ',
    'run get add': 'git add ',
    # 'run get bisect': 'git bisect ',
    'run get branch': 'git branch ',
    'run get checkout': 'git checkout ',
    'run get clone': 'git clone ',
    'run get commit': ['git commit -a -m ""', Key('left')],
    'run get diff': 'git diff ',
    # 'run get fetch': 'git fetch ',
    # 'run get grep': 'git grep ',
    'run get in it': 'git init ',
    # 'run get log': 'git log ',
    'run get merge': 'git merge ',
    'run get move': 'git mv ',
    'run get pull': 'git pull ',
    'run get push': 'git push ',
    # 'run get rebase': 'git rebase ',
    # 'run get reset': 'git reset ',
    # 'run get show': 'git show ',
    'run get status': 'git status ',
    # 'run get tag': 'git tag ',
    'run (them | vim)': 'vim ',
    'run L S': 'ls\n',
    'dot pie': '.py',
    # 'run make': 'make\n',
    # 'run jobs': 'jobs\n',

    # 'const': 'const ',
    # 'static': 'static ',
    # 'tip pent': 'int ',
    # 'tip char': 'char ',
    # 'tip byte': 'byte ',
    # 'tip float': 'float ',
    # 'tip double': 'double ',

    'args': ['()', Key('left')],
    'prex': ['()', Key('left')],
    'brax': ['[]', Key('left')],
    # 'index': ['[]', Key('left')],
    'kirk': ['{}', Key('left')], # [' {}', Key('left enter enter up tab')],
    'empty array': '[]',
    'empty dict': '{}',

    'state (def | deaf | deft)': 'def ',
    'state else if': 'elif ',
    'state if': 'if ',
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state for': 'for ',
    'state switch': ['switch ()', Key('left')],
    'state case': ['case \nbreak;', Key('up')],
    'state goto': 'goto ',
    'state import': 'import ',
    'state class': 'class ',

    # 'state include': '#include ',
    # 'state include system': ['#include <>', Key('left')],
    # 'state include local': ['#include ""', Key('left')],
    # 'state type deaf': 'typedef ',
    # 'state type deaf struct': ['typedef struct {\n\n};', Key('up'), '\t'],

    'comment see': '// ',
    'comment py': '# ',

    # 'word queue': 'queue',
    # 'word eye': 'eye',
    # 'word bson': 'bson',
    # 'word iter': 'iter',
    # 'word no': 'NULL',
    # 'word cmd': 'cmd',
    # 'word dup': 'dup',
    # 'word streak': ['streq()', Key('left')],
    # 'word printf': 'printf',
    # 'word (dickt | dictionary)': 'dict',
    # 'word shell': 'shell',

    # 'word lunixbochs': 'lunixbochs',
    'word talon': 'talon',
    # 'word Point2d': 'Point2d',
    # 'word Point3d': 'Point3d',
    # 'title Point': 'Point',
    # 'word angle': 'angle',

    # 'dunder in it': '__init__',
    # 'self taught': 'self.',
    # 'dickt in it': ['{}', Key('left')],
    # 'list in it': ['[]', Key('left')],
    # 'string utf8': "'utf8'",
    # 'state past': 'pass',

# amy mods
    'plus': '+',
    'arrow': '->',
    'call': '()',
    'indirect': '&',
    'dereference': '*',
    'equeft': ' = ',
    # 'op (minus | subtract)': ' - ',
    # 'op (plus | add)': ' + ',
    # 'op (times | multiply)': ' * ',
    # 'op divide': ' / ',
    # 'op mod': ' % ',
    # '[op] (minus | subtract) equals': ' -= ',
    # '[op] (plus | add) equals': ' += ',
    # '[op] (times | multiply) equals': ' *= ',
    # '[op] divide equals': ' /= ',
    # '[op] mod equals': ' %= ',

    # '(op | is) greater [than]': ' > ',
    # '(op | is) less [than]': ' < ',
    # '(op | is) equal': ' == ',
    'longqual': ' == ',
    'pausa': ' -- ',
    # '(op | is) not equal': ' != ',
    # '(op | is) greater [than] or equal': ' >= ',
    # '(op | is) less [than] or equal': ' <= ',
    # '(op (power | exponent) | to the power [of])': ' ** ',
    # 'op and': ' && ',
    # 'op or': ' || ',
    # '[op] (logical | bitwise) and': ' & ',
    # '[op] (logical | bitwise) or': ' | ',
    # '(op | logical | bitwise) (ex | exclusive) or': ' ^ ',
    # '[(op | logical | bitwise)] (left shift | shift left)': ' << ',
    # '[(op | logical | bitwise)] (right shift | shift right)': ' >> ',
    # '(op | logical | bitwise) and equals': ' &= ',
    # '(op | logical | bitwise) or equals': ' |= ',
    # '(op | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    # '[(op | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    # '[(op | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    'shebang bash': '#!/bin/bash -u\n',

    'new window': Key('cmd-n'),
    'next window': Key('cmd-`'),
    'last window': Key('cmd-shift-`'),
    # 'next app': Key('cmd-tab'),
    # 'last app': Key('cmd-shift-tab'),
    'next tab': Key('ctrl-tab'),
    'new tab': Key('cmd-t'),
    'last tab': Key('ctrl-shift-tab'),

    'next space': Key('cmd-alt-ctrl-right'),
    'last space': Key('cmd-alt-ctrl-left'),

    'scroll down': [Key('down')] * 30,
    'scroll up': [Key('up')] * 30,

    ## Amy's own commands
    'save this': Key('cmd-s'),
    'close tab': Key('cmd-w'),
    'dizzle': Key('cmd-z'),
    'rizzle': Key('cmd-shift-z'),

    'copy bundle': copy_bundle,
})
