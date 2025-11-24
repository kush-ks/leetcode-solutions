#include <queue>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(!head) return NULL;

        priority_queue<int,vector<int>,greater<int>> pq;
        ListNode* ptr = head;

        while(ptr) {
            pq.push(ptr->val);
            ptr = ptr->next;
        }

        ptr = head;
        while(ptr) {
            ptr->val = pq.top();
            pq.pop();
            ptr = ptr->next;
        }

        return head;
    }
};