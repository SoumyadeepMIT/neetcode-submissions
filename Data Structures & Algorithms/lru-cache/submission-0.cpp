class LRUCache {
public:
    struct Node{
        int key;
        int val;
        Node* next;
        Node* prev;
        Node(int k,int v): key(k), val(v), prev(nullptr), next(nullptr){}
    };
    unordered_map<int, Node*> um;
    int cap;
    Node* dleft;
    Node* dright;
    LRUCache(int capacity) {
        cap = capacity;
        um.clear();
        dleft = new Node(0,0);
        dright = new Node(0,0);
        dleft->next = dright;
        dright->prev = dleft;
    }
    
    void insert(Node* nod){
        Node* pre = dright->prev;
        pre->next = nod;
        nod->prev = pre;
        nod->next = dright;
        dright->prev = nod;
    }
    void rem(Node* nod){
        Node* pre = nod->prev;
        Node* nex = nod->next;
        pre->next = nex;
        nex->prev = pre;
    }
    
    int get(int key) {
        if(um.find(key)!=um.end()){
            rem(um[key]);
            insert(um[key]);
            return um[key]->val;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(um.find(key)!=um.end()){
            rem(um[key]);
            delete um[key];
        }
        Node* nod = new Node(key,value);
        um[key]=nod;
        insert(um[key]);
    
        if(um.size()>cap){
            Node* lru = dleft->next;
            um.erase(lru->key);
            rem(lru);
            delete lru;
        }
    }
};
