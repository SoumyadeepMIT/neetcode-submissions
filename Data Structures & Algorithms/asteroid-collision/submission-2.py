class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for stone in asteroids:
            if stone > 0:
                st.append(stone)
            else:
                while len(st)>0 and st[-1]>0 and abs(stone) > st[-1]:
                    st.pop()
                if len(st) == 0 or st[-1]<0:
                    st.append(stone)
                elif st[-1] == abs(stone):
                    st.pop()
        return st