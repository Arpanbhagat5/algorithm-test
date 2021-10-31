from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:
    table = dict()
    pattern_length = len(pattern)
    table = {pattern[i]:max(1, pattern_length-i-1) for i in range(pattern_length)}
    if not len(table):
        raise Exception("TODO")
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)
        self.pattern_length = len(pattern)
        self.text_length = len(text)

    def decide_slide_width(self, index_of_text: int) -> int:
        # assert len(c) == 1
        if self.text[index_of_text] in self.table.keys():
            return self.table[self.text[index_of_text]]
        else:
            return self.pattern_length
        # raise Exception("TODO")
        # return -1

    def search(self) -> int:

        for it in range(self.pattern_length-1, self.text_length):
            for ip in range(self.pattern_length-1, -2, -1):
                if ip == -1:
                    print(f'Found {self.pattern} in {self.text} at {it+1}')
                    return it+1

                if self.pattern[ip] != self.text[it]:
                    it = it + self.decide_slide_width(it)
                    break
                if self.pattern[ip] == self.text[it]:
                    it -= 1

        # raise Exception("TODO")
        print(f'Did not find {self.pattern} in {self.text}')
        return -1
