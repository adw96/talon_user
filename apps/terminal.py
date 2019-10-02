from talon.voice import Word, Context, Key, Rep, Str, press
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import time

ctx = Context('Terminal', bundle='com.apple.Terminal')


ctx.keymap({


    'cd': 'cd ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),

    'run make (durr | dear)': 'mkdir ',
    'run get': 'git ',
    'run get (R M | remove)': 'git rm ',
    'run get add': 'git add ',
    'run get branch': 'git branch ',
    'run get checkout': 'git checkout ',
    'run get clone': 'git clone ',
    'run get commit': ['git commit -a -m ""', Key('left')],
    'run get diff': 'git diff ',
    'run get in it': 'git init ',
    'run get merge': 'git merge ',
    'run get move': 'git mv ',
    'run get pull': 'git pull ',
    'run get push': 'git push ',
    'run get status': 'git status ',
    'run (them | vim)': 'vim ',
    'run L S': 'ls\n',
    'dot pie': '.py',
    # 'run make': 'make\n',
    # 'run jobs': 'jobs\n',

    'open Talon directory': ['cd ~/.talon/user/', Key('Enter')], 

    'Kunda activate': ['conda activate ']
})
