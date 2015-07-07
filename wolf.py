wolf_str = """
*     *    *     /\\__/\\  *     *
   *            /      \\
        *   *  |  -  -  |    *
 *   __________| \\     /|     *
   /              \\ T / |
 /                      |  *
|  ||     |    |       /         *
|  ||    /______\\     / |*    *
|  | \\  |  /     \\   /  |
 \\/   | |\\ \\      | | \\ \\
      | | \\ \\     | |  \\ \\
      | |  \\ \\    | |   \\ \\
      '''   '''   '''    '''
"""

wind_str = """
~   ~   ~
  ~   ~   ~
~   ~   ~
  ~   ~   ~
~   ~   ~
  ~   ~   ~
~   ~   ~
  ~   ~   ~
~   ~   ~
"""

import subprocess
from ascii_art import AsciiArt
class Wolf(object):
    def __init__(self):
        self.description = "Normal"
        self.art = AsciiArt(wolf_str)

    def __str__(self):
        return str(self.art)

    def huff_and_puff(self):
        wind = AsciiArt(wind_str)
        print self.art.concat(wind, padding=3).concat(wind)

    def say(self, message):
        subprocess.call(['cowthink', '-f', './wolf.cow', '\"{}\"'.format(message)])
