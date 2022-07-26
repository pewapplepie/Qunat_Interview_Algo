//Sliding Window Moving Average
// Input = {5,2,4,6} Output: 2,3,4
// Input = {3,0,0,-2,0,2,0,-2} Output: 0,0,0,0,0,0,0

#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;
// priority_queue<int> small, large;

// void addNum(int num) {
//     small.push(num);
//     large.push(-small.top());
//     small.pop();
//     if (small.size() < large.size()) {
//         small.push(-large.top());
//         large.pop();
//     }
// }

// double findMedian() {
//     return small.size() > large.size() ? small.top() : (small.top() - large.top()) / 2.0;
// }

// vector<double> medianSlidingWindow(vector<int> &nums, int k) {
//     multiset<int> window(nums.begin(), nums.begin() + k);
//     auto mid = next(window.begin(), k / 2);
//     vector<double> medians;

//     for (int i = 0; i < nums.size(); i++) {
//         if (i < k) {
//             addNum(nums[i]);
//             medians.push_back(findMedian());
//         } else {
//             medians.push_back((double(*mid) + *prev(mid, 1 - k % 2)) / 2);

//             if (i == nums.size()) {
//                 return medians;
//             }

//             window.insert(nums[i]);
//             if (nums[i] < *mid) {
//                 mid--;
//             }

//             if (nums[i - k] <= *mid) {
//                 mid++;
//             }
//             window.erase(window.lower_bound(nums[i - k]));
//         }
//     }
//     return medians;
// }

// int ArrayChallenge(int arr[], int arrLength) {
//     int k = arr[0];
//     vector<int> nums;
//     for (int i = 1; i < arrLength; i++) {
//         nums.push_back(arr[i]);
//     }

//     auto ans = medianSlidingWindow(nums, k);
//     // cout << ans << endl;
//     return 0;
// }
double findMedian(vector<int>& arr){
    int n = arr.size();
    sort(arr.begin(), arr.end());
    if (n&1){
        return arr[n/2];
    }else{
        return (arr[n/2] + arr[n/2 - 1])/2.0;
    }
     
}

string ArrayChallenge(int arr[], int arrLength) {
    int k = arr[0];
    double mid;
    vector<int> currMedian;
    string s;
    for (int i = 1; i < arrLength; i++) {
        if(i < k){
            currMedian.push_back(arr[i]);

            mid = findMedian(currMedian);
            s.append(to_string(mid));
        }else{
            currMedian.push_back(arr[i]);
            mid = findMedian(currMedian);
            currMedian.erase(currMedian.begin());
            s.append(to_string(mid));
        }
        if(i != arrLength - 1){
            s.append(",");
        }

    }
    return s;

}

int main(void) {
    int A[] = {3,0,0,-2,0,2,0,-2};
    int arrLength = sizeof(A) / sizeof(*A);

    cout << ArrayChallenge(A, arrLength) << endl;

    return 0;
}