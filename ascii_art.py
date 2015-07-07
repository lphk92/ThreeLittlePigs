class AsciiArt(object):
    def __init__(self, s):
        self.pic = s
        self.lines = s.split('\n')
        self.width = len(max(self.lines, key=len))
        self.height = len(self.lines)

    def __str__(self):
        return self.pic

    def _pad_lines(self):
        result = []
        for l in self.lines:
            diff = self.width - len(l)
            l += ' ' * diff
            result.append(l)
        return result

    def concat(self, art, padding=0):
        self_lines = self._pad_lines()
        art_lines = art._pad_lines()

        diff = len(self_lines) - len(art_lines)
        if diff > 0:
            for i in range(abs(diff)):
                art_lines.append(' ' * art.width)
        else:
            for i in range(abs(diff)):
                self_lines.append(' ' * self.width)

        combo_lines = [l[0] + ' ' * padding + l[1] for l in zip(self_lines, art_lines)]
        return AsciiArt("\n".join(combo_lines))
