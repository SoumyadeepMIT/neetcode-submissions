class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        priority_queue<pair<int,int>> pq;
        queue<pair<int,int>> q;
        vector<int> freq(26,0);
        for(char c:tasks){
            freq[c-'A']++;
        }
        for(int i=0;i<26;i++){
            if(freq[i]!=0)
                pq.push({freq[i],i});
        }
        int t = 0;
        while(!(pq.empty() && q.empty())){
            t++;
            while(!q.empty() && t>=q.front().second){
                pq.push({freq[q.front().first], q.front().first});
                q.pop();
            }
            if(!pq.empty()){
                pair<int,int> p = pq.top();
                pq.pop();
                freq[p.second]--;
                if(freq[p.second]!=0){
                    q.push({p.second,t+n+1});
                }
           }
        }
        return t;
    }
};
