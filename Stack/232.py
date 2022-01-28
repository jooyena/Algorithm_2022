class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.ouput.append(self.input.pop())

            return self.ouput[-1]

    def empty(self):
        return self.input == [] and self.ouput == []
