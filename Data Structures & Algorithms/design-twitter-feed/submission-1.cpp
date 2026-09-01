class Twitter {
public:
    unordered_map<int, unordered_set<int>> userFollow;
    unordered_map<int, vector<pair<int,int>>> userTweet;
    int tweet; 
    Twitter() {
        tweet=0;
    }
    
    void postTweet(int userId, int tweetId) {
        userTweet[userId].push_back({tweet++,tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        priority_queue<pair<int,int>> pq;
        if(userTweet.find(userId)!=userTweet.end()){
            for(pair<int,int> p:userTweet[userId]){
                pq.push(p);
            }
        }
        for(int u:userFollow[userId]){
            if(userTweet.find(u)!=userTweet.end()){
                for(pair<int,int> p:userTweet[u]){
                    pq.push(p);
                }
            }
        }
        vector<int> res;
        int r=10;
        while(r>0 && !pq.empty()){
            pair<int,int> p = pq.top();
            res.push_back(p.second);
            pq.pop();
            r--;
        }
        return res;
    }
    
    void follow(int followerId, int followeeId) {
        if(followerId!=followeeId)
            userFollow[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId){
        if(followerId!=followeeId)
            userFollow[followerId].erase(followeeId);
    }
};
