# originally from https://github.com/JonathanNickerson/talon_voice_user_scripts
# and https://github.com/pimentel/talon_user/blob/master/repeat.py

from talon.voice import Context, Rep, RepPhrase, talon
from . import utils

ctx = Context("repeater")

def repeat(m):
    # TODO: This could be made more intelligent:
    #         * Apply a timeout after which the command will not repeat previous actions
    #         * Prevent stacking of repetitions upon previous repetitions
    repeat_count = user.utils.m_to_number(m)

    if repeat_count != None and repeat_count >= 2:
        repeater = RepPhrase(repeat_count - 1)
        repeater.ctx = talon
        return repeater(None)

ctx.keymap(
        {
        "wink | repple": Rep(1),
        "creek": RepPhrase(1),
        "soup": Rep(2),
        "trace": Rep(3),
        "quarr": Rep(4),
        "fypes": Rep(5),
        
        # "(repeat | repple)" + utils.numerals: repeat, # Doesn't work?
        # "(repeat | repple) (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)+": repeat,
        'repple two': Rep(2),
        'repple three': Rep(3),
        'repple (for | four)': Rep(4),
        'repple five': Rep(5),
        'repple six': Rep(6),
        'repple seven': Rep(7),
        'repple eight': Rep(8),
        'repple nine': Rep(9),
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
    }
)
