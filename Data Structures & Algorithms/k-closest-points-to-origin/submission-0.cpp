class Solution {
public:
    constexpr static auto dist_cmp = [](const vector<int>& p1, const vector<int>& p2) constexpr {
        double dist1 = p1[0]*p1[0] + p1[1]*p1[1];
        double dist2 = p2[0]*p2[0] + p2[1]*p2[1];
        return dist1 < dist2;
    };
    
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        std::priority_queue<vector<int>, vector<vector<int>>, decltype(dist_cmp)> pq(points.begin(), points.begin()+k);

        for (int i = k; i < points.size(); ++i){
            pq.push(points[i]);
            pq.pop();
        }

        std::vector<vector<int>> results;
        while (!pq.empty()) {
            results.push_back(pq.top());
            pq.pop();
        }

        return results;

    }
};
