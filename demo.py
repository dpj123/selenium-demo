class addition():
    def __init__(self, numb1, numb2):
        self.numb1 = numb1
        self.numb2 = numb2

    def add(self):
        sumation = self.numb1 + self.numb2
        return sumation


a = addition(10, 20)
print(a.add())
a = addition(50, 20)
print(a.add())