from talon.voice import Word, Context, Key, Rep, Str, press
import time

ctx = Context('Chrome', bundle='com.google.Chrome')


ctx.keymap({

    # Google Docs
    'strikethrough': Key('cmd-shift-x'),
    'superscript': Key('cmd-.'),
    'subscript': Key('cmd-,'),

    # email
    'open work email': ['mail.google.com/mail/u/0/#inbox', Key('enter'), Key('enter')],
    'open personal email': ['mail.google.com/mail/u/1/', Key('enter'), Key('enter')],

    # slack
    'open Talon slack': ['talonvoice.slack.com/', Key('enter'), Key('enter')],
    'open omics slack': ['omicshour.slack.com', Key('enter'), Key('enter')],
    'open lab slack': ['statdivlab.slack.com', Key('enter'), Key('enter')],

})
