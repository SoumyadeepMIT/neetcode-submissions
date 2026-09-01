/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* origHead = head;
        Node* prev=NULL;
        Node* resHead = NULL;
        unordered_map<Node*, Node*> um;
        while(origHead!=nullptr){
            Node* temp = new Node(origHead->val);
            if(resHead==NULL){
                resHead = temp;
                prev=resHead;
            }
            else{
                prev->next = temp;
                prev=temp;
            }
            um[origHead]=temp;
            origHead=origHead->next;
        }
        origHead = head;
        Node* temp = resHead;
        while(origHead!=nullptr){
            if(origHead->random!=nullptr){
                temp->random = um[origHead->random];
            }
            origHead=origHead->next;
            temp = temp->next;
        }
        return resHead;
    }
};
