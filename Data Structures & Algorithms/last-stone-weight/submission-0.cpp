class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for(int n:stones){
            pq.push(n);
        }
        while(pq.size()>1){
            int x=pq.top();
            pq.pop();
            int y = pq.top();
            pq.pop();
            int v = x-y;
            if(v!=0){
                pq.push(v);
            }
        }
        if(pq.empty())
        {
            return 0;
        }
        return pq.top();
    }
};
