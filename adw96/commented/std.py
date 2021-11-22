# from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
# from talon import app, ctrl, clip, ui
# from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
# import string
#
# # cleans up some Dragon output from <dgndictation>
# mapping = {
#     'semicolon': ';',
#     'new-line': '\n',
#     'new-paragraph': '\n\n',
# }
# # used for auto-spacing
# punctuation = set('.,-!?')
#
# def parse_word(word):
#     word = str(word).lstrip('\\').split('\\', 1)[0]
#     word = mapping.get(word, word)
#     return word
#
# def join_words(words, sep=' '):
#     out = ''
#     for i, word in enumerate(words):
#         if i > 0 and word not in punctuation:
#             out += sep
#         out += word
#     return out
#
# def parse_words(m):
#     return list(map(parse_word, m.dgndictation[0]._words))
#
# def insert(s):
#     Str(s)(None)
#
# def text(m):
#     # Added 10/9/18 because I want 'I' words to be capitalised automatically
#     insert(join_words(parse_words(m)))
#     # insert(join_words(parse_words(m)).lower())
#
#
# def sentence_text(m):
#     # text = join_words(parse_words(m)).lower() ## from repo
#     # Added 10/9/18 because I want 'I' words to be capitalised  automatically
#     text = join_words(parse_words(m))
#     insert(text.capitalize())
#
#
# def word(m):
#     text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
#     insert(text.lower())
#
# def surround(by):
#     def func(i, word, last):
#         if i == 0: word = by + word
#         if last: word += by
#         return word
#     return func
#
# def rot13(i, word, _):
#     out = ''
#     for c in word.lower():
#         if c in string.ascii_lowercase:
#             c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
#         out += c
#     return out
#
# formatters = {
#
#     ## about spacing/characters
#     # 'dunder': (True,  lambda i, word, _: '__%s__' % word if i == 0 else word),
#     'camel':  (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
#     'snake':  (True,  lambda i, word, _: word if i == 0 else '_'+word),
#     'dotsway':  (True,  lambda i, word, _: word if i == 0 else '.'+word),
#     'pathway':  (True,  lambda i, word, _: word if i == 0 else '/'+word),
#     'smash':  (True,  lambda i, word, _: word),
#     'spine':  (True,  lambda i, word, _: word if i == 0 else '-'+word), # spinal or kebab?
#
#     ## about cases
#     'squash':  (False, lambda i, word, _: word.lower()),
#     'yeller': (False, lambda i, word, _: word.upper()),
#
#     # experimenting with new words
#     'tiptoe':  (False, lambda i, word, _: word.capitalize()),
#     'sento':  (False, lambda i, word, _: word.capitalize() if i == 0 else word),
#     'loepoe':  (False, lambda i, word, _: word.lower()),
#
#     'dubstring': (False, surround('"')),
#     # 'string': (False, surround("'")),
#     'padded': (False, surround(" ")),
#     'rot-thirteen':  (False, rot13),
# }
#
# def FormatText(m):
#     fmt = []
#     for w in m._words:
#         if isinstance(w, Word):
#             fmt.append(w.word)
#     try:
#         words = parse_words(m)
#     except AttributeError:
#         with clip.capture() as s:
#             press('cmd-c')
#         words = s.get().split(' ')
#         if not words:
#             return
#
#     tmp = []
#     spaces = True
#     for i, word in enumerate(words):
#         word = parse_word(word)
#         for name in reversed(fmt):
#             smash, func = formatters[name]
#             word = func(i, word, i == len(words)-1)
#             spaces = spaces and not smash
#         tmp.append(word)
#     words = tmp
#
#     sep = ' '
#     if not spaces:
#         sep = ''
#     Str(sep.join(words))(None)
#
# def copy_bundle(m):
#     bundle = ui.active_app().bundle
#     clip.set(bundle)
#     app.notify('Copied app bundle', body='{}'.format(bundle))
#
# ctx = Context('input')
# ctx.keymap({
#     'say <dgndictation> [over]': text,
#     'phrase <dgndictation> [over]': text,
#     # TODO: try to rewire myself
#     # 'phrase <dgndictation> [over]': text,
#
#     'sento <dgndictation> [over]': sentence_text,
#     'comma <dgndictation> [over]': [', ', text],
#     'space <dgndictation> [over]': [' ', text],
#     # 'word <dgnwords>': word,
#
#     '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,
#
#     # more keys and modifier keys are defined in basic_keys.py
#
#     'slap': [Key('cmd-right enter')],
#     'questo': '?',
#     'swipe': ', ',
#     'tilde': '~',
#     'bang': '!',
#     'dollar | (dollar sign)': '$',
#     'crunder': '_',
#     'colon': ':',
#     '(paren | left paren)': '(', '(rparen | are paren | right paren)': ')',
#     '(brace | left brace)': '{', '(rbrace | are brace | right brace)': '}',
#     '(langle | left angle | less than)': '<',
#     '(rangle | are angle | right angle | greater than)': '>',
#
#     'star': '*',
#     '(pound | pounder | hash [sign])': '#',
#     'percy': '%',
#     'caret': '^',
#     'loco': '@',
#     '(and sign | ampersand | amper)': '&',
#     'spike': '|',
#
#     '(dubquote | double quote)': '"',
#     # 'triple quote': "'''",
#
#     '(dot dot | dotdot)': '..',
#
#     'args': ['()', Key('left')],
#     # 'prex': ['()', Key('left')],
#     'brax': ['[]', Key('left')],
#     'kirk': ['{}', Key('left')], # [' {}', Key('left enter enter up tab')],
#     'empty array': '[]',
#     'empty dict': '{}',
#
#     'comment see': '// ',
#     'comment py': '# ',
#     'dot py': '.py',
#     'dot MD': '.md',
#
#     # META
#     "save this": Key("cmd-s"), # previously Sage
#     "dizzle": Key("cmd-z"),
#     "rizzle": Key("cmd-shift-z"),
#
#     # amy mods
#     'plus': '+',
#     'lambo': '->',
#     'indirect': '&',
#     'dereference': '*',
#     'equeft': ' = ',
#     'deminus': ' - ',
#     'deplush': ' + ',
#
#     'longqual': ' == ',
#     'pausa': ' -- ',
#
#     'shebang bash': '#!/bin/bash -u\n',
#
#     'new window': Key('cmd-n'),
#     'next window': Key('cmd-`'),
#     'last window': Key('cmd-shift-`'),
#     'next tab': Key('ctrl-tab'),
#     'new tab': Key('cmd-t'),
#     'last tab': Key('ctrl-shift-tab'),
#
#     'next space': Key('cmd-alt-ctrl-right'),
#     'last space': Key('cmd-alt-ctrl-left'),
#
#     'scroll down': [Key('down')] * 30,
#     'scroll up': [Key('up')] * 30,
#
#     ## Amy's own commands
#     'close tab': Key('cmd-w'),
#     'quit program': Key('cmd-q'),
#
#     'copy bundle': copy_bundle,
# })
