class Iterator:

    def __init__(self, up_to):
        self.up_to = up_to
        self.n = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.up_to:
            num_temp = self.n
            self.n += 1
            return num_temp, num_temp+1
        else:
            raise StopIteration


for num_temp, next_num in Iterator(7):
    print(num_temp, next_num)