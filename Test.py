class ExampleClass():
    def __init__(self, number):
        self.number = number

    def plus_2_times_4(self,x):
        return 4*(x + 2)

    def arithmetic(self):
        return self.plus_2_times_4(self.number)

instance = ExampleClass(number = 4)
print(instance.arithmetic())
