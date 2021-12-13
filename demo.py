class addition:
    b = []

    def __init__(self, numb1, numb2):
        self.numb1 = numb1
        self.numb2 = numb2

    def add(self):
        s = self.numb1 + self.numb2
        return s

    def list_append(self):
        l = ["jain", "jojo"]
        r = self.add()
        print(r)
        for x in l:
            self.b.append(x)
        return self.b


a = addition(10, 20)
result = a.list_append()
print(result[0] + "\n" + result[1])
