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
class Pig(object):
    def __init__(self):
        pass

    def __str__(self):
        return pig_str

    def __mul__(self, value):
        pig_list = []
        for i in range(0, value):
            pig_list.append(Pig())
        return pig_list

    def say(self, message):
        subprocess.call(['cowthink', '-f', './pig.cow', '\"{}\"'.format(message)])
