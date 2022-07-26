#include <string>
#include <algorithm>
#include <vector>
#include <unordered_set>
#include <iostream>  
using namespace std;

int seriesOfDecreaseRating(vector<int> &ratings){
    int res = 0, i = 0, m = ratings.size();
    for(int j = 0; j < m; j++){
        if(j > 0 && ratings[j] < ratings[j-1]){
            res += j - i + 1;
        }
        else{
            res += 1;
            i = j;
        }
    }
    return res;
}

int main(){
    vector<int> test {4,2,5,4,3};
    int ans = seriesOfDecreaseRating(test);
    cout << ans << endl;
    return 0;
}