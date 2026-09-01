class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<double,double>> cars;
        int n = position.size();
        for(int i=0;i<n;i++){
            cars.push_back({(double)position[i],(double)speed[i]});
        }
        sort(cars.begin(),cars.end(), [](const pair<double, double> &a, const pair<double, double> &b){
            return a.first<b.first;
        });
        vector<double> time(n,0.0);
        stack<int> st;
        for(int i=n-1;i>=0;i--){
            double t = (target - cars[i].first)/cars[i].second;
            time[i]=t;
            if(!st.empty() && time[st.top()]<t){
                st.push(i);
            }
            else if(st.empty()){
                st.push(i);
            }
        }
        return st.size();
    }
};
