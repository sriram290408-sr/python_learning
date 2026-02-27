class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add_num(self):
        return self.a + self.b

    def sub_num(self):
        return self.a - self.b

    def multi_num(self):
        return self.a * self.b

    def div_num(self):
        return self.a/self.b

mycal = Calculator(5,3)
mycal.add_num()