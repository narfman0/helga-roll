import random, re
from helga.plugins import command


HELP_TEXT = 'Roll a dice. \
Usage: !roll d<sides>'
ROLL_REGEX = re.compile(r'(\d+)?d(\d+)\+?(\d+)?')


def roll_dice(count=1, sides=20, modifier=0):
    """ Perform roll with given parameters """
    result = ''
    total = 0
    for _ in range(0, count):
        roll_result = random.randint(1, int(sides))
        result += str(roll_result) + ' '
        total += roll_result
    total += modifier
    result += '= ' + str(total)
    return result


def parse_roll(match):
    """ Parse the match to a roll and return string representation """
    count, sides, modifier = match.groups()
    count = 1 if not count else int(count)
    modifier = 0 if not modifier else int(modifier)
    return roll_dice(count, sides, modifier)


@command('roll', aliases=['dice'], help=HELP_TEXT, shlex=True)
def roll(_client, _channel, _nick, _message, _cmd, args):
    """ Roll the bones... """
    result = 'Result of '
    for rolls in args:
        result += rolls + ': '
        match = re.search(ROLL_REGEX, rolls)
        if match:
            result += parse_roll(match)
        elif ',' in rolls:
            roll_list = rolls.split(',')
            result += random.choice(roll_list)
        result += ', ' if rolls != args[-1] else ' '
    return result
