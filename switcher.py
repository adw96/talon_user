from talon.voice import Word, Context, Key, Rep, Str, press
from talon import ui

apps = {}

def switch_app(m):
    name = str(m._words[1])
    full = apps.get(name)
    if not full:
        return
    for app in ui.apps():
        if app.name == full:
            app.focus()
            time.sleep(0.25)
            break


def short_application(m, app):
    m._words = [0, app]
    switch_app(m)

# Note to self : program only works if already open
ctx = Context('switcher')
keymap = {
    # 'fox {switcher.apps}': switch_app,
    'atomee': lambda x: short_application(x, 'Atom'),
    'termee': lambda x: short_application(x, 'Terminal'),
    'messagey': lambda x: short_application(x, 'Messages'),
    'chromie': lambda x: short_application(x, 'Google Chrome'),
    'asked judy': lambda x: short_application(x, 'RStudio'),
    'kenotee': lambda x: short_application(x, 'Keynote'),
    'calendii': lambda x: short_application(x, 'Calendar'),

}

ctx.keymap(keymap)

def update_lists():
    global apps
    new = {}
    for app in ui.apps():
        if app.background and not app.windows():
            continue
        words = app.name.split(' ')
        for word in words:
            if word and not word in new:
                new[word] = app.name
        new[app.name] = app.name
    if set(new.keys()) == set(apps.keys()):
        return
    ctx.set_list('apps', new.keys())
    apps = new

def ui_event(event, arg):
    update_lists()

ui.register('', ui_event)
update_lists()
