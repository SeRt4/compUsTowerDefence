import re


class WaveEngine:
    def __init__(self, file):
        self.file1 = open(file).readlines()
        self.words = []
        self.numbers = []
        self.waves = []
        self.army = []

    def start(self):
        self.split()
        self.find_numbers()
        self.find_str()
        self.generation()

    def split(self):
        for i in self.file1:
            self.waves.append(list(i.split()))

    def find_numbers(self):
        for i in self.waves:
            for j in i:
                find = re.findall(r'\d+', j)
                str_find = ' '.join(find)
                self.numbers.append(int(str_find))
        return self.numbers

    def find_str(self):
        for i in self.waves:
            for j in i:
                find = re.findall(r'\D', j)
                str_find = ''.join(find)
                self.words.append(str(str_find))
        return self.words

    def generation(self):
        for i, j in zip(self.numbers, self.words):
            self.army.append(i * j)
        print(self.army)


wave = WaveEngine('wave.txt')
wave.start()
