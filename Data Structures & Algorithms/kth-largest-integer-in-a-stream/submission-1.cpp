class KthLargest {
public:
    int k;
    vector<int> nums;
    priority_queue<int,vector<int>,greater<int>> pq;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        this->nums = nums;
        for(int n:nums){
            if(pq.size()==k){
                if(pq.top()<n){
                    pq.pop();
                    pq.push(n);
                }
            }
            else{
                pq.push(n);
            }
        }
    }
    
    int add(int val) {
        if(pq.size()==k){
            if(pq.top()<val){
                pq.pop();
                pq.push(val);
            }
        }
        else{
            pq.push(val);
        }
        return pq.top();
    }
};
