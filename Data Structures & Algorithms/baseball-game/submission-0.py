class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                t1, t2 = stack[-1], stack[-2]
                stack.append(t1+t2)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                p1 = 2 * stack[-1]
                stack.append(p1)
            else:
                stack.append(int(op))
        return sum(stack) 