from talon.voice import Context, Rep, talon
from user.utils import parse_words_as_integer

ctx = Context('repeater')

# TODO: This could be made more intelligent:
#         * Apply a timeout after which the command will not repeat previous actions
#         * Prevent stacking of repetitions upon previous repetitions
def repple(m):
    repeat_count = parse_words_as_integer(m._words[1:])

    if repeat_count != None and repeat_count >= 2:
        repeater = Rep(repeat_count)
        # repeater = Rep(repeat_count - 1)
        repeater.ctx = talon
        return repeater(None)
    elif repeat_count == None or repeat_count == 1:
        repeater = Rep(1)
        repeater.ctx = talon
        return repeater(None)

ctx.keymap({
    'repple (2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)+': repple,
    'repple': Rep(1),
    'repple ten': Rep(10),
    'repple eleven': Rep(11),
    'repple twelve': Rep(12),
    'repple thirteen': Rep(13),
    'repple fourteen': Rep(14),
    'repple fifteen': Rep(15),
    'repple sixteen': Rep(16),
    'repple seventeen': Rep(17),
    'repple eighteen': Rep(18),
    'repple nineteen': Rep(19),
    'repple twenty': Rep(20),
    'repple thirty': Rep(30),
    'repple forty': Rep(40),
    'repple fifty': Rep(50),
    'repple sixty': Rep(60),
    'repple seventy': Rep(70),
    'repple eighty': Rep(80),
    'repple ninety': Rep(90),
})
