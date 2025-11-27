using namespace std;

class Solution {
private:
    int* postorder(TreeNode* ptr, int &maxSum) {
        // return type: [ min, max, curr_sum ]
        if(!ptr) return new int[3]{ INT_MAX, INT_MIN, 0 };

        int currSum = INT_MIN;
        int *l  = postorder(ptr->left, maxSum);
        int *r = postorder(ptr->right, maxSum);
        int *res = new int[3]{ INT_MIN, INT_MAX, 0 };

        // maxLeft < node < minRight
        if(ptr->val < *r && ptr->val > *(l+1)) {
            currSum = *(l+2)+*(r+2)+ptr->val;
            res[0] = min(ptr->val,*l);
            res[1] = max(ptr->val,*(r+1));
        }

        if(currSum > INT_MIN) {
            res[2] = currSum;
            maxSum = max(maxSum, currSum);
        }

        delete[] l,r;
        return res; 
    }

public:
    int maxSumBST(TreeNode* root) {
        int maxSum = INT_MIN;
        postorder(root,maxSum);
        return max(0,maxSum);
    }
};