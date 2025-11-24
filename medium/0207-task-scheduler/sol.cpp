#include <queue>
#include <vector>
#include <unordered_map>

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prq) {
        vector<int> deg(numCourses,-1);
        unordered_map<int,vector<int>> conn;
        queue<int> Q;
        int key;
        bool ans = true;

        // build indegrees
        for(int i=0;i<prq.size();i+=1) {
            deg[prq[i][0]] = max(0, deg[prq[i][0]]) + 1;
            deg[prq[i][1]] = max(0, deg[prq[i][1]]);
            if(conn.find(prq[i][1]) != conn.end())
                conn[prq[i][1]].push_back( prq[i][0] );
            else
                conn[prq[i][1]] = { prq[i][0] };
        }

        // find indegrees = 0
        for(int i=0;i<numCourses;i+=1)
            if(deg[i]==0) Q.push(i);

        // topological sort
        while(!Q.empty()) {
            key = Q.front();
            Q.pop();
            if(conn.find(key)!=conn.end()) {
                for(int i=0;i<conn[key].size();i+=1) {
                    deg[conn[key][i]] -= 1;
                    if(deg[conn[key][i]] == 0)
                        Q.push(conn[key][i]);
                }
            }
        }  

        // if indegree > 0 exist then cycle exist
        for(int i=0;i<numCourses;i+=1)
            if(deg[i]>0) {
                ans = false;
                break;
            }
        
        return ans;
    }
};
