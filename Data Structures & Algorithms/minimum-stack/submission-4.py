class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []
        self.minv = float("inf")

    def push(self, val: int) -> None:
        self.st.append(val)
        self.minv = min(self.minst[-1], val) if len(self.minst)>0 else val
        self.minst.append(self.minv)

    def pop(self) -> None:
        if len(self.st)<=0: return None
        self.st.pop()
        self.minst.pop()

    def top(self) -> int:
        if len(self.st)<=0: return -1
        return self.st[-1]

    def getMin(self) -> int:
        if len(self.minst)<=0: return -1
        return self.minst[-1]
