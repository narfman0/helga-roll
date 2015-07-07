import random, re
from helga.plugins import command

_help_text = 'Roll a dice. \
Usage: !roll d<sides>'
_roll_regex = re.compile('(\d+)?d(\d+)\+?(\d+)?')

def roll_dice(count=1, sides=20, modifier=0):
    """ Perform roll with given parameters """
    result = ''
    total = 0
    for _ in range(0, count):
        roll = random.randint(1, int(sides))
        result += str(roll) + ' '
        total += roll
    total += modifier
    result += '= ' + str(total)
    return result

def parse_roll(match):
    """ Parse the match to a roll and return string representation """
    count, sides, modifier = match.groups()
    count = 1 if not count else int(count)
    modifier = 0 if not modifier else int(modifier)
    return roll_dice(count, sides, modifier)

@command('roll', aliases=['dice'], help=_help_text, shlex=True)
def roll(client, channel, nick, message, cmd, args):
    """ Roll the bones... """
    result = 'Result of '
    for rolls in args:
        result += rolls + ': '
        match = re.search(_roll_regex, rolls)
        if match:
            result += parse_roll(match)
        elif ',' in rolls:
            roll_list = rolls.split(',')
            result += random.choice(roll_list)
        result += ', ' if rolls != args[-1] else ' '
    return result
