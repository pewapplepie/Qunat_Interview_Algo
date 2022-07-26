#include<stack>
#include <iostream>
#include <cstdio>
#include<string>
#include<vector>
using namespace std;

vector<int> sunsetViews(vector<int> buildings, string direction) {
  // Write your code here.
	stack<int> buildingIdx;
	if (direction == "EAST"){
		for(int i = 0; i < buildings.size(); ++i){
			buildingIdx.push(i);
			int currheight = buildings[buildingIdx.top()];
            cout << "curr h:" << currheight << " ,";
			if(currheight <= buildings[i]){
				buildingIdx.pop();
			}
		}
	}else{
		for(int i = buildings.size()-1; i >=0; i--){
			buildingIdx.push(i);
			int currheight = buildings[buildingIdx.top()];
			if(currheight <= buildings[i]){
				buildingIdx.pop();
			}
		}
	}
    printf("start\n");
	vector<int> ans;
	while(!buildingIdx.empty()){
		cout<<buildingIdx.top();
//		ans.push_back(buildingIdx.top());
		buildingIdx.pop();
	}
  return ans;
}
int main(){
    vector<int> buildings {3,5,4,4,3,1,3,2};
    string directrion = "EAST";
    sunsetViews(buildings, directrion);
}