#include <string>
#include <unordered_map>
#include <vector>

class TimeMap {
private:
    unordered_map<string, vector<pair<int,string>>> mem;

public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        if(mem.find(key) != mem.end()) {
            mem[key].push_back({ timestamp, value });
        }
        else {
            mem[key] = {{ timestamp, value }};
        }
    }
    
    string get(string key, int timestamp) {
        if(mem.find(key) == mem.end())
            return "";

        int n = mem[key].size();

        // check boundary overflow
        if(timestamp < mem[key][0].first)
            return "";
        if(timestamp > mem[key][n-1].first)
            return mem[key][n-1].second;

        
        // binary search
        int low = 0, high = n-1;
        int mid, index = 0;

        while(low<=high) {
            mid = low+(high-low)/2;
            if(mem[key][mid].first <= timestamp) {
                index = mid;
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }

        return mem[key][index].second;
    }
};

