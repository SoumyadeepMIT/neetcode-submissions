from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        n = len(hand)
        if n%gs!=0: return False
        hand.sort()
        freq = defaultdict(int)
        for h in hand:
            freq[h] = freq[h]+1
        for h in hand:
            if freq[h]>0:
                for i in range(h, h+gs):
                    if freq[i]<=0: return False
                    freq[i] -= 1
        return True