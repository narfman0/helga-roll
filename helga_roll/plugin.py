import random, re
from helga.plugins import command

_help_text = 'Roll a dice. \
Usage: !roll d<sides>'
_roll_regex = re.compile('(\d+)?d(\d+)\+?(\d+)?')

@command('roll', aliases=['dice'], help=_help_text)
def roll(client, channel, nick, message, cmd, args):
    """ Roll the bones... """
    result = 'Result of '
    for rolls in args:
        result += rolls + ': '
        count, sides, modifier = re.search(_roll_regex, rolls).groups()
        count = 1 if not count else int(count)
        modifier = 0 if not modifier else int(modifier)
        total = 0
        for _ in range(0, count):
            roll = random.randint(1, int(sides))
            result += str(roll) + ' '
            total += roll
        total += modifier
        result += '= ' + str(total)
        result += ', ' if rolls != args[-1] else ' '
    return result
