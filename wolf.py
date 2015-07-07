wolf_str = """
*     *    *     /\\__/\\  *    ---    *
   *            /      \\    /     \\
        *   *  |  -  -  |  |       |*
 *   __________| \\     /|  |       |
   /              \\ T / |   \\     /
 /                      |  *  ---
|  ||     |    |       /             *
|  ||    /______\\     / |*     *
|  | \\  |  /     \\   /  |
 \\/   | |\\ \\      | | \\ \\
      | | \\ \\     | |  \\ \\
      | |  \\ \\    | |   \\ \\
      '''   '''   '''    '''
"""

import subprocess
class Wolf(object):
    def __init__(self):
        self.description = "Normal"

    def __str__(self):
        return wolf_str

    def say(self, message):
        subprocess.call(['cowthink', '-f', './wolf.cow', '\"{}\"'.format(message)])
