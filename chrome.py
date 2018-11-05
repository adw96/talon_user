from talon.voice import Word, Context, Key, Rep, Str, press
import time

ctx = Context('Chrome', bundle='com.google.Chrome')


ctx.keymap({

    # email
    'open work email': ['mail.google.com/mail/u/0/#inbox', Key('Enter'), Key('Enter')],
    'open personal email': ['mail.google.com/mail/u/1/', Key('Enter'), Key('Enter')],

    # slack
    'open Talon slack': ['talonvoice.slack.com/', Key('Enter'), Key('Enter')],
    'open omics slack': ['omicshour.slack.com', Key('Enter'), Key('Enter')],
    'open lab slack': ['statdivlab.slack.com', Key('Enter'), Key('Enter')],

})
