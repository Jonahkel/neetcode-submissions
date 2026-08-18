class LRUCache {
public:
    LRUCache(int capacity) : capacity(capacity) {}
    
    int get(int key) {
        auto itr = key_to_itr.find(key);
        if (itr == key_to_itr.end()) return -1;
        items.splice(items.begin(), items, itr->second);
        return itr->second->value;
    }
    
    void put(int key, int value) {
        auto itr = key_to_itr.find(key);
        if (itr == key_to_itr.end()) {
            if (key_to_itr.size() == capacity) {
                key_to_itr.erase(items.back().key);
                items.pop_back();
            }
            items.push_front({key, value}) ;
            key_to_itr[key] = items.begin();
        } else {
            itr->second->value = value;
            items.splice(items.begin(), items, itr->second);
        }
    }

private:

    struct Item {
        int key;
        int value;
    };

    list<Item> items;
    unordered_map<int, list<Item>::iterator> key_to_itr;
    int capacity;
};
