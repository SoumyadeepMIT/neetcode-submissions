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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* nth = dummy;
        ListNode* nthFront = head;
        while(n>0){
            nthFront = nthFront->next;
            n--;
        }
        while(nthFront!=nullptr){
            nth = nth->next;
            nthFront = nthFront->next;
        }
        nth->next = nth->next->next;
        return dummy->next;
    }
};
