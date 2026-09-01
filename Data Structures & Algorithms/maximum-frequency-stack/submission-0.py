class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = [[]]

    def push(self, val: int) -> None:
        fval = 1 + self.freq.get(val, 0)
        self.freq[val] = fval
        if fval >= len(self.stacks):
            self.stacks.append([])
        self.stacks[fval].append(val)

    def pop(self) -> int:
        res = self.stacks[-1].pop()
        self.freq[res] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return res      


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()