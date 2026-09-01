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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode* curr = dummy;
        int c=0;
        while(l1!=nullptr && l2!=nullptr){
            int v = l1->val + l2->val + c;
            c=v/10;
            ListNode* nod = new ListNode(v%10);
            curr->next = nod;
            curr = curr->next;
            l1=l1->next;
            l2 = l2->next;
        }
        while(l1){
            int v = l1->val + c;
            c=v/10;
            ListNode* nod = new ListNode(v%10);
            curr->next = nod;
            curr = curr->next;
            l1=l1->next;
        }
        while(l2){
            int v = l2->val + c;
            c=v/10;
            ListNode* nod = new ListNode(v%10);
            curr->next = nod;
            curr = curr->next;
            l2 = l2->next;
        }
        if(c!=0){
            ListNode* nod = new ListNode(c);
            curr->next = nod;
            curr=curr->next;
        }
        return dummy->next;
    }
};
