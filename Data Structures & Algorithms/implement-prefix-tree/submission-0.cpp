class TrieNode {
    public:
    TrieNode* child[26];
    bool eow;
    TrieNode() {
        for(int i=0;i<26;i++){
            child[i]=nullptr;
        }
        eow=false;
    }
};

class PrefixTree {
    
    TrieNode* root;
public:
    PrefixTree() {
        root = new TrieNode();
    }
    
    void insert(string word) {
        TrieNode* cur = root;
        for(char c:word){
            int i = c - 'a';
            if(cur->child[i]==nullptr){
                cur->child[i] = new TrieNode();
            }
            cur = cur->child[i];
        }
        cur->eow = true;
    }
    
    bool search(string word) {
        TrieNode* cur = root;
        for(char c:word){
            int i = c-'a';
            if(cur->child[i]==nullptr){
                return false;
            }
            cur = cur->child[i];
        }
        return cur->eow;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = root;
        for(char c:prefix){
            int i = c-'a';
            if(cur->child[i]==nullptr){
                return false;
            }
            cur = cur->child[i];
        }
        return true;
    }
};
