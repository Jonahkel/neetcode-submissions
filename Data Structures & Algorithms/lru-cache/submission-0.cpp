class LRUCache {
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        auto cache_itr = cache.find(key);
        if (cache_itr == cache.end()) return -1;
        keys.erase(key_to_itr[key]);
        keys.push_front(key);
        key_to_itr[key] = keys.begin();
        return cache_itr->second;
    }
    
    void put(int key, int value) {
        auto cache_itr = cache.find(key);
        if (cache_itr == cache.end()) {
            if (cache.size() == capacity) {
                cache.erase(keys.back());
                keys.pop_back();
            } 
        } else {
            keys.erase(key_to_itr[key]);
        }
        cache[key] = value;
        keys.push_front(key);
        key_to_itr[key] = keys.begin();
    }

private:
    list<int> keys;
    unordered_map<int, int> cache;
    unordered_map<int, list<int>::iterator> key_to_itr;
    int capacity;
};
