class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)
        st = ["JFK"]
        res = []
        while st:
            cur = st[-1]
            if not adj[cur]:
                res.append(st.pop())
            else:
                st.append(adj[cur].pop())
        return res[::-1]