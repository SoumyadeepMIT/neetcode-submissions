/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* rev=NULL;
        ListNode* prev=NULL;
        while(head){
            rev = new ListNode(head->val);
            if(prev){
                rev->next = prev;
            }
            prev = rev;
            head = head->next;
        }
        return rev;
    }
};
