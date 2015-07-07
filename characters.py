cow_file_top = """
$the_cow = <<EOC
   $thoughts
     $thoughts
"""

cow_file_bottom = """
EOC
"""

import subprocess
from ascii_art import AsciiArt
class Character(object):
    def __init__(self, art_str):
        self.art = AsciiArt(art_str)

    def __str__(self):
        return str(self.art)

    def say(self, message):
        with open('/tmp/curr.cow', 'w') as f:
            f.write(cow_file_top + str(self.art).replace("\\", "\\\\") + cow_file_bottom)
        subprocess.call(['cowthink', '-f', '/tmp/curr.cow', '\"{}\"'.format(message)])

class Pig(Character):
    def __init__(self):
        Character.__init__(self, pig_str)

    def __mul__(self, value):
        pig_list = []
        for i in range(0, value):
            pig_list.append(Pig())
        return pig_list

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
