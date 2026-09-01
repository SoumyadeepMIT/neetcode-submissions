class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int r=matrix.size();
        int c = matrix[0].size();
        int top=0;
        int bot=r-1;
        while(top<=bot){
            int m=(top+bot)/2;
            if(target<matrix[m][0]){
                bot=m-1;
            }
            else if(target>matrix[m][c-1]){
                top = m+1;
            }
            else{
                break;
            }
        }
        if(!(top<=bot)){
            return false;
        }
        int lef = 0;
        int rig = c-1;
        int row = (top+bot)/2;
        while(lef<=rig){
            int m = (lef+rig)/2;
            if(target>matrix[row][m]){
                lef = m+1;
            }
            else if(target<matrix[row][m]){
                rig = m-1;
            }
            else{
                return true;
            }
        }
        return false;
    }
};
