#include <string>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <iostream>     // std::cout, std::end

using namespace std;
class DisjointSet {
private:
    vector<int> weights; // Used to store weights of each nodes
    vector<int> parents;

public:
    void Union(int a, int b) {
        int rootA = Find(a);
        int rootB = Find(b);
        // If both a and b have same root, i.e. they both belong to the same set, hence we don't need to take union
        if (rootA == rootB) return;

        // Weighted union
        if (this->weights[rootA] > this->weights[rootB]) {
            // In case rootA is having more weight
            // 1. Make rootA as the parent of rootB
            // 2. Increment the weight of rootA by rootB's weight
            this->parents[rootB] = rootA;
            this->weights[rootA] += this->weights[rootB];
        } else {
            // Otherwise
            // 1. Make rootB as the parent of rootA
            // 2. Increment the weight of rootB by rootA's weight
            this->parents[rootA] = rootB;
            this->weights[rootB] += this->weights[rootA];
        }
    }

    int Find(int a) {
        // Traverse all the way to the top (root) going through the parent nodes
        while (a != this->parents[a]) {
            // Path compression
            // a's grandparent is now a's parent
            this->parents[a] = this->parents[parents[a]];
            a = this->parents[a];
        }
        return a;
    }

    bool isInSameGroup(int a, int b) {
        // Return true if both a and b belong to the same set, otherwise return false
        return Find(a) == Find(b);
    }

    // Initialize weight for each node to be 1
    DisjointSet(int N) {
        this->parents.resize(N + 1);
        this->weights.resize(N + 1);
        // Set the initial parent node to itself
        for (int i = 1; i <= N; ++i) {
            this->parents[i] = i;
            this->weights[i] = 1;
        }
    }
};

class Solution {
public:
    int minimumCost(int N, vector<vector<int>>& connections) {
        DisjointSet *disjointset = new DisjointSet(N);
        // Sort connections based on their weights (in increasing order)
        sort(connections.begin(), connections.end(),
            [](const vector<int> &a, const vector<int> &b) {
                return a[2] < b[2];
            });
        // Keep track of total edges added in the MST
        int total = 0;
        // Keep track of the total cost of adding all those edges
        int cost = 0;
        for (int i = 0; i < connections.size(); ++i) {
            int a = connections[i][0];
            int b = connections[i][1];
            // Do not add the edge from a to b if it is already connected
            if (disjointset->isInSameGroup(a, b)) continue;
            // If a and b are not connected, take union
            disjointset->Union(a, b);
            // increment cost
            cost += connections[i][2];
            // increment number of edges added in the MST
            total++;
        }
        // If all N nodes are connected, the MST will have a total of N - 1 edges
        if (total == N - 1) {
            return cost;
        } else {
            return -1;
        }
    }
};

int main(){
    //int n = 3;
    vector<vector<int>> testcase{{"A","B","1"},{"B","C","4"},{"B","D","6"},{"D","E","5"},{"C","E","1"}};
    Solution sol;
    int ans = sol.minimumCost(testcase);
    cout << ans << endl;
    return 0;
};
