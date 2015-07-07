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

import subprocess
from ascii_art import AsciiArt
class Pig(object):
    def __init__(self):
        self.art = AsciiArt(pig_str)

    def __str__(self):
        return str(self.art)

    def __mul__(self, value):
        pig_list = []
        for i in range(0, value):
            pig_list.append(Pig())
        return pig_list

    def say(self, message):
        subprocess.call(['cowthink', '-f', './pig.cow', '\"{}\"'.format(message)])
