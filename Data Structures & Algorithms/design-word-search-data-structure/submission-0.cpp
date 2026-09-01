class TrieNode{
    public:
    vector<TrieNode*> child;
    bool eow;

    TrieNode() : child(26, nullptr), eow(false){}
};

class WordDictionary {
public:
    TrieNode* root;
    WordDictionary() {
        root = new TrieNode();
    }
    
    void addWord(string word) {
        TrieNode* curr = root;
        for(char c:word){
            int i = c- 'a';
            if(curr->child[i]==nullptr){
                curr->child[i]=new TrieNode();
            }
            curr = curr->child[i];
        }
        curr->eow = true;
    }
    
    bool search(string word) {
        TrieNode* curr = root;
        return dfs(word,curr,0);
    }
    private:
        bool dfs(string word, TrieNode* root, int i){
            TrieNode* cur = root;
            for(int j =i; j<word.size(); j++){
                if(word[j]=='.'){
                    for(TrieNode* ch: cur->child){
                        if(ch && dfs(word,ch,j+1)){
                            return true;
                        }
                    }
                    return false;
                }
                else{
                    if(cur->child[word[j]-'a']==nullptr){
                        return false;
                    }
                    cur = cur->child[word[j]-'a'];
                }
            }
            return cur->eow;
        }
};
