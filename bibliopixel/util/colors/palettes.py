from . make import make_colors as _colors
from bibliopixel.colors import conversions

"""
Map names to palettes
==========================

First, the name is looked up in the mutable ``USER_PALETTES`` dictionary.
The project set ``USER_PALETTES`` from its "palettes" Section.

If that fails, the name is looked up in a fixed, immutable dictionary
``GLOBAL_PALETTES``.
"""

DEFAULT_PALETTE = 'rainbow'


def get(name=DEFAULT_PALETTE):
    """
    Return a named Palette, or None if no such name exists.

    If ``name`` is omitted, the default value is used.
    """
    if isinstance(name, str):
        return USER_PALETTES.get(name) or GLOBAL_PALETTES.get(name)


# This global variable is changed by the Project to allow color settings
# in Animations and other classes to use palette names.  TODO: fix this.
# types would somehow need to know about the current Project, non-trivial.
USER_PALETTES = {}

GLOBAL_PALETTES = {
    # "Classic" palettes from old BP
    'rainbow': _colors(conversions.HUE_RAINBOW),
    'raw': _colors(conversions.HUE_RAW),
    'spectrum': _colors(conversions.HUE_SPECTRUM),
    'three_sixty': _colors(conversions.HUE_360),

    # Custom palettes
    'flag': _colors('red, white, blue'),
    'checker': _colors('white, black', serpentine=True),
    'primary': _colors('red, green, blue'),
    'secondary': _colors('yellow, magenta, cyan'),
    'eight': _colors('black, red, yellow, green, cyan, blue, magenta, white'),
    'van_gogh': _colors('gold, teal, spring green 3, ivory black'),
    'trendy': _colors('medium aquamarine, orange red, chocolate 1, gainsboro'),
    'muted': _colors('navajo white 3, ivory 3, white smoke, ivory black'),
    'bold': _colors('black, dodger blue 4, hot pink 4, orange red 3'),
    'clean': _colors('light cyan 2, dark gray, brown 1, snow 2'),
    'warm': _colors('snow 3, dark grey, indian red 4, burly wood 3'),
    'sharp': _colors('sea green 3, ivory black, burly wood 2, gray'),
    'pastel': _colors('azure 3, eggshell, sienna 2, goldenrod'),
    'tints': _colors('plum 4, dark grey, antique white 2, linen'),
    'splash': _colors('steel blue 3, gainsboro, gold, tan 2'),
    'energy': _colors('magenta, yellow, cyan, beige'),
}