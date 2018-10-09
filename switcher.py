## script from aegis, slack, help channel, October3
from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ui
import time
import os

running = {}
launch = {}

def switch_app(m):
    name = str(m['switcher.running'][0])
    full = running.get(name)
    if not full: return
    for app in ui.apps():
        if app.name == full:
            app.focus()
            # TODO: replace sleep with a check to see when it is in foreground
            time.sleep(0.25)
            break

def launch_app(m):
    name = str(m['switcher.launch'][0])
    path = launch.get(name)
    if path:
        ui.launch(path=path)

def launch_rstudio():
    launch_app('RStudio')

ctx = Context('switcher')
ctx.keymap({
    'fox {switcher.running}': switch_app,
    'launch {switcher.launch}': launch_app,
    'run program': launch_rstudio,
    # 'fox {switcher.apps}': switch_app,
    # 'atomee': lambda x: short_application(x, 'Atom'),
    # 'termee': lambda x: short_application(x, 'Terminal'),
    # 'messagey': lambda x: short_application(x, 'Messages'),
    # 'chromie': lambda x: short_application(x, 'Google Chrome'),
    # 'asked judy': lambda x: short_application(x, 'RStudio'),
    # 'kenotee': lambda x: short_application(x, 'Keynote'),
    # 'calendii': lambda x: short_application(x, 'Calendar'),
    # 'findy': lambda x: short_application(x, 'Finder'),
})

def update_lists():
    global running
    global launch
    new = {}
    for app in ui.apps():
        if app.background and not app.windows():
            continue
        words = app.name.split(' ')
        for word in words:
            if word and not word in new:
                new[word] = app.name
        new[app.name] = app.name
    running = new
    ctx.set_list('running', running.keys())

    new = {}
    for base in '/Applications', '/Applications/Utilities':
        for name in os.listdir(base):
            path = os.path.join(base, name)
            name = name.rsplit('.', 1)[0]
            new[name] = path
            words = name.split(' ')
            for word in words:
                if word and word not in new:
                    if len(name) > 6 and len(word) < 3:
                        continue
                    new[word] = path
    launch = new
    ctx.set_list('launch', launch.keys())

def ui_event(event, arg):
    if event in ('app_activate', 'app_launch', 'app_close', 'win_open', 'win_close'):
        update_lists()

ui.register('', ui_event)
update_lists()

#
#
#
# from talon.voice import Word, Context, Key, Rep, Str, press
# from talon import ui
#
# apps = {}
#
# def switch_app(m):
#     name = str(m._words[1])
#     full = apps.get(name)
#     if not full:
#         return
#     for app in ui.apps():
#         if app.name == full:
#             app.focus()
#             time.sleep(0.25)
#             break
#
#
# def short_application(m, app):
#     m._words = [0, app]
#     switch_app(m)
#
# # Note to self : program only works if already open
# ctx = Context('switcher')
# keymap = {
#     'fox {switcher.apps}': switch_app,
#     'atomee': lambda x: short_application(x, 'Atom'),
#     'termee': lambda x: short_application(x, 'Terminal'),
#     'messagey': lambda x: short_application(x, 'Messages'),
#     'chromie': lambda x: short_application(x, 'Google Chrome'),
#     'asked judy': lambda x: short_application(x, 'RStudio'),
#     'kenotee': lambda x: short_application(x, 'Keynote'),
#     'calendii': lambda x: short_application(x, 'Calendar'),
#     'findy': lambda x: short_application(x, 'Finder'),
# }
#
# ctx.keymap(keymap)
#
# ## from  https://github.com/pimentel/talon_user/blob/master/switcher.py
# def update_lists():
#     global apps
#     new = {}
#     for app in ui.apps():
#         # if not app.windows():
#         #     continue
#         words = app.name.split(' ')
#         for word in words:
#             if word and not word in new:
#                 new[word] = app.name
#         new[app.name] = app.name
#     if set(new.keys()) == set(apps.keys()):
#         return
#     ctx.set_list('apps', new.keys())
#     apps = new
#
#
# def ui_event(event, arg):
#     if event in ('app_activate', 'app_launch', 'app_close', 'win_open', 'win_close'):
#         update_lists()
#
# # ## from https://github.com/talonvoice/examples/blob/master/switcher.py
# # def update_lists():
# #     global apps
# #     new = {}
# #     for app in ui.apps():
# #         if app.background and not app.windows():
# #             continue
# #         words = app.name.split(' ')
# #         for word in words:
# #             if word and not word in new:
# #                 new[word] = app.name
# #         new[app.name] = app.name
# #     if set(new.keys()) == set(apps.keys()):
# #         return
# #     ctx.set_list('apps', new.keys())
# #     apps = new
# #
# # def ui_event(event, arg):
# #     update_lists()
#
# ui.register('', ui_event)
# update_lists()
