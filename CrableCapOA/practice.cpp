#include <iostream>    
#include <iterator>    
#include <list>        
#include <algorithm>   
using namespace std;
int main()
{
    // Declaring first container
    list<int> v1 = { 1, 2, 3, 7, 8, 9 };
  
    // Declaring second container
    list<int> v2 = { 4, 5, 6 };
  
    list<int>::iterator i1;
    i1 = v1.begin();
    // i1 points to 1 in v1
  
    list<int>::iterator i2;
    // i2 = v1.begin() + 3;
    // This cannot be used with lists
    // so use std::next for this
  
    i2 = std::next(i1, 3);
  
    // Using std::copy
    // std::copy(i1, i2, std::back_inserter(v2));
    // // v2 now contains 4 5 6 1 2 3
  
    // // Displaying v1 and v2
    // cout << "v1 = ";
  
    // int i;
    // for (i1 = v1.begin(); i1 != v1.end(); ++i1) {
    //     cout << *i1 << " ";
    // }
  
    cout << "\nv2 = ";
    for(auto i:i2){
        cout << i << " ";
    }
  
    return 0;
}