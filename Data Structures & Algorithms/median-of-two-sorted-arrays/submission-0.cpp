class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>& A = nums1;
        vector<int>& B = nums2;
        if (A.size() > B.size()) {
            swap(A, B); // Ensuring A is the smaller array
        }
        
        int total = A.size() + B.size();
        int half = total / 2;
        
        int l = 0;
        int r = A.size();
        
        while (l <= r) {
            int i = l + (r - l) / 2;    // Middle of A
            int j = half - i;           // Corresponding index in B
            
            int Aleft = (i == 0) ? INT_MIN : A[i - 1];
            int Aright = (i == A.size()) ? INT_MAX : A[i];
            int Bleft = (j == 0) ? INT_MIN : B[j - 1];
            int Bright = (j == B.size()) ? INT_MAX : B[j];
            
            // Correct partition
            if (Aleft <= Bright && Bleft <= Aright) {
                if (total % 2 == 0) {
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0;
                } else {
                    return min(Aright, Bright);
                }
            } else if (Aleft > Bright) {
                r = i - 1; // Move the right pointer left
            } else {
                l = i + 1; // Move the left pointer right
            }
        }
        
        // If there is no solution, which should not be the case
        throw std::invalid_argument("Input arrays are not sorted or of incorrect size");
    }
};