class Robot:

    def __init__(self, c, h, w):
        self.color = c
        self.height = h
        self.weight = w

    def fire(self):
        print('총알')

class NewRo(Robot):

    def __init__(self, c, h, w):
        super().__init__(c, h, w)

    def fire(self):
        super().fire()
        print('총총알')

newro = NewRo('초록', 'ㅇ', 'ㄹ')
newro.fire()