// #include <bitset>/stdc++.h>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

int discount_calc(string Type, int discount, int value) {
    cout << "original: " << value << " ";
    if (Type == "0") {
        value = discount;
    } else if (Type == "1") {
        if (discount * value % 100 != 0) {
            value = value - discount * value / 100 - 1;
        } else {
            value = value - discount * value / 100;
        }

    } else if (Type == "2") {
        value -= discount;
    }

    cout << "final: " << value << endl;
    return value;
}

int findLowestPrice(vector<vector<string>> products, vector<vector<string>> discounts) {
    unordered_map<string, pair<string, int>> discount_table;
    for (auto& discount : discounts) {
        discount_table[discount[0]] = {discount[1], stoi(discount[2])};
    }

    int total = 0;

    for (auto& product : products) {
        int cost = stoi(product[0]);
        int discounted = cost;
        for (int i = 1; i < product.size(); i++) {
            string tag = product[i];
            discounted = min(discounted, discount_calc(discount_table[tag].first,
                                                       discount_table[tag].second, cost));
        }
        total += discounted;
    }

    return total;
}

int main() {
    // vector<vector<string>> products = {
    // {"10", "d0", "d1"}, {"15", "EMPTY", "EMPTY"}, {"20", "d1", "EMPTY"}};
    // vector<vector<string>> discounts = {{"d0", "1", "27"}, {"d1", "2", "5"}};
    vector<vector<string>> products = {{"10", "sale", "january-sale"}, {"200", "sale", "EMPTY"}};
    vector<vector<string>> discounts = {{"sale", "0", "10"}, {"january-sale", "1", "10"}};

    cout << findLowestPrice(products, discounts) << endl;
    return 0;
}