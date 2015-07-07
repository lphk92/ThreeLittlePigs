import subprocess
from ascii_art import AsciiArt
class Character(object):
    def __init__(self, art_str):
        self.art = AsciiArt(art_str)

    def __str__(self):
        return str(self.art)

    def say(self, message):
        result = ""
        message_lines = [message[i : i + self.art.width] for i in range(0, len(message), self.art.width)]
        w = min(self.art.width, len(message))
        result += " " + "-" * (w + 2) + "\n"
        for m in message_lines:
            if len(m) < w:
                m += ' ' * (w - len(m))
            result += "| " + m + " |" + "\n"
        result += " " + "-" * (w + 2) + "\n"
        result += " " * (w/2) + "|" + "\n"
        result += str(self.art)
        return AsciiArt(result)

class Pig(Character):
    def __init__(self):
        Character.__init__(self, pig_str)

    def __mul__(self, value):
        result = Pig().art
        for i in range(1, value):
            result = result.concat(Pig().art)
        return result

class Wolf(Character):
    def __init__(self):
        Character.__init__(self, wolf_str)

    def huff_and_puff(self, house=None):
        wind = AsciiArt(wind_str)
        result = self.art.concat(wind, padding=3).concat(wind)
        if house != None:
            result = result.concat(house.art, padding=3)
        return result

class Man(Character):
    def __init__(self):
        Character.__init__(self, man_str)

pig_str = """
    _,--.       ,--._
    \\  > `-\"\"\"-' <  /
     `-.         .-'
       / 'e___e` \\
      (   (o o)   )
      _\\_  `='  _/_
     / /|`-._.-'|\\ \\
    / /||_______||\\ \\
  _/ /_||=======||_\\ \\_
 / _/==||       ||==\\_ \\
 `'(   ^^       ^^   )`'
    \\               /
     \\______|______/
     |______|______|
       )__|   |__(
      /   ]   [   \\
"""

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

man_str = """
           ,/////\\\\,
         ,/////////\\\\\\
       ,///////////\\\\\\\\
       ////  __     _\\\\
       /// //  \\  //  \\
       /,  \\\\_O/  \\\\_O/
       \\_         \\   |
         \\      ,__>  /
         |\\   ,____  /
         | \\   \\__| /
         |  '._____/
         |      |
       /``"--._ \\/`\\
      /        \\|  /`--.
    /```""--..__;.'     `\\
"""
