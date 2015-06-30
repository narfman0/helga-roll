import random, re
from helga.plugins import command

_help_text = 'Roll a dice. \
Usage: !roll d<sides>'

@command('roll', aliases=['dice'], help=_help_text)
def roll(client, channel, nick, message, cmd, args):
    """ Roll the bones... """
    result = 'Result of '
    for rolls in args:
        result += rolls + ': '
        count, sides = rolls.split('d')
        count = 1 if not count else int(count)
        try:
            sides, plus = sides.split('+')
        except ValueError:
            plus = 0
        total = 0
        for _ in range(0, count):
            roll = random.randint(1, int(sides))
            result += str(roll) + ' '
            total += roll
        total += int(plus)
        result += '= ' + str(total)
        result += ', ' if rolls != args[-1] else ' '
    return result
