#include <algorithm>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

int solution(vector<int> &A, int x, int y, int z) {
    int maxwait = 0;
    vector<pair<string, int>> stations;
    stations.push_back({"X", x});
    stations.push_back({"Y", y});
    stations.push_back({"Z", z});
    unordered_map<string, int> occupied;

    for (auto fuel : A) {
        int canfill = 0;
        for (auto & station : stations) {
            if (station.second >= fuel) {
                canfill = 1;
                if (occupied.count(station.first)) {
                    maxwait = max(maxwait, occupied[station.first]);
                    occupied[station.first] += fuel;
                    station.second -= fuel;
                } else {
                    occupied[station.first] = fuel;
                    station.second -= fuel;
                }
                break;
            }
        }

        if (canfill == 0) return -1;
    }
    return maxwait;
};

int main() {
    vector<int> A = {2, 8, 4, 3, 2};
    int sol = solution(A, 7, 11, 3);
    cout << sol << endl;
}
