
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool check(vector<int>& points, long long m, long long target) {
        int n = points.size();

        if (n == 1) {
            return (target + points[0] - 1) / points[0];
        }

        vector<long long> nums(n, 0);
        nums[0] = 1;

        long long total_visits = 1;

        for (int i = 0; i < n; i++) {
            long long games = (target + points[i] - 1) / points[i];
            long long remainingVisits = games - nums[i];

            if (i != n - 1) {
                if (remainingVisits > 0) {
                    nums[i] += remainingVisits;
                    nums[i + 1] += remainingVisits;

                    total_visits += 2 * remainingVisits;
                }

                if (i != n - 2 ||
                    nums[i + 1] < (target + points[i + 1] - 1) / points[i + 1]) {

                    nums[i + 1] += 1;
                    total_visits += 1;
                }
            }
            else {
                if (remainingVisits > 0) {
                    nums[i] += remainingVisits;
                    nums[i - 1] += remainingVisits;

                    total_visits += 2 * remainingVisits;
                }
            }

            if (total_visits > m) {
                return false;
            }
        }

        return true;
    }

    long long maxScore(vector<int>& points, int m) {
        long long low = 1;
        long long high = (long long)*min_element(points.begin(), points.end()) * m;

        long long ans = 0;

        while (low <= high) {
            long long mid = low + (high - low) / 2;

            if (check(points, m, mid)) {
                ans = mid;
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }

        return ans;
    }
};
