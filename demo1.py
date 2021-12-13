class addition:

    def __init__(self, numb1, numb2):
        self.numb1 = numb1
        self.numb2 = numb2

    def add(self):
        s = self.numb1 + self.numb2
        return s


a = addition(10, 20)
result = a.add()
try:

    assert result == 50
except AssertionError:
    print(AssertionError)
else:
    print(result)
finally:
    print(result)