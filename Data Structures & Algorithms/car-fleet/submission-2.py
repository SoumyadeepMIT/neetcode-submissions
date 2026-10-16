class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        for i in range(n):
            cars.append((position[i], speed[i]))
        cars.sort(key = lambda x: x[0])
        st = []
        for i in range(n-1, -1, -1):
            t = (target - cars[i][0])/cars[i][1]
            if len(st)>0 and t<=st[-1]:
                continue
            else:
                st.append(t)
        return len(st)