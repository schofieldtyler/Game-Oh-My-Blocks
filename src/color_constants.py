"""Provide RGB color constants and a colors dictionary with
elements formatted: colors[colorname] = CONSTANT"""

from collections import namedtuple, OrderedDict

Color = namedtuple('RGB', 'red, green, blue')
colors = {}  # dict of colors


class RGB(Color):
    def hex_format(self):
        '''Returns color in hex format'''
        return '#{:02X}{:02X}{:02X}'.format(self.red, self.green, self.blue)


# Color Contants
ALICEBLUE = RGB(240, 248, 255)
ANTIQUEWHITE = RGB(250, 235, 215)
ANTIQUEWHITE1 = RGB(255, 239, 219)
ANTIQUEWHITE2 = RGB(238, 223, 204)
ANTIQUEWHITE3 = RGB(205, 192, 176)
ANTIQUEWHITE4 = RGB(139, 131, 120)

# Add colors to colors dictionary
colors['aliceblue'] = ALICEBLUE
colors['antiquewhite'] = ANTIQUEWHITE
colors['antiquewhite1'] = ANTIQUEWHITE1
colors['antiquewhite2'] = ANTIQUEWHITE2
colors['antiquewhite3'] = ANTIQUEWHITE3
colors['antiquewhite4'] = ANTIQUEWHITE4

colors = OrderedDict(sorted(colors.items(), key=lambda t: t[0]))
