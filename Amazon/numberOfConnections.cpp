#include <string>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <iostream>   
using namespace std;
int numberOfConnections(vector<vector<int>> gridOfNodes){
    int n = gridOfNodes.size();
    int m = gridOfNodes[0].size();
    int ans = 0;
    int prev = 0;
    int curr = 0;
    

    for(int i = 0; i < n; i++){
        int count = 0;
        for(int j = 0; j < m; j++){
            count += gridOfNodes[i][j];
        }
        if(i == 0) {
            prev = count;
            continue;
        }

        if(count == 0) continue;
        
        curr = count;
        ans += prev*curr;
        cout << "curr at " << i << " count :" << count << " ans is " << ans <<endl;
        prev = curr;
        
    }
    return ans;
}

int main(){
    vector<vector<int>> test {{1,1,1},{0,1,0},{0,0,0},{1,1,0}};
    int out = numberOfConnections(test);
    cout << out << endl;
    return 0;
}