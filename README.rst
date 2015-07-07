helga-roll
==========

Roll dice

Usage
-----

``!roll <count>d<sides>+<modifier>`` - rolls <count> <sides>-sided dice with
modifier

To roll a dice and specify how many sides, place an integer in <sides>

``!roll d6`` - rolls a single d6, printing the output

Can add multiple in fron of d to roll multiples of a particular die. The total
is given at the end.

``!roll 3d6`` - rolls 3 d6s, then sums them up.

Can add modifiers which will get added to the sum of the rolls

``!roll 3d6+6`` - rolls 3 d6s the same as ``3d6``, but adds 6 at the end

A random decision can be given by giving a comma separated list (surrounded
by quotation marks)

``!roll "red,blue,green"`` - return a single random item from list, e.g. "red"


License
-------

Copyright (c) 2015 Jon Robison

See included LICENSE for licensing information
