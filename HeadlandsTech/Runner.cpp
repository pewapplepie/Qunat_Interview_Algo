#include <iomanip>
#include <iostream>
#include <regex>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;

vector<int> parseInts(string str) {
    stringstream ss(str);
    char ch;
    int num;
    vector<int> ans;
    while (ss >> num) {
        ans.push_back(num);
        ss >> ch;
    }
    return ans;
}

int main() {
    const regex pattern("[0-9]+,[0-9]+,[0-9]+");
    std::smatch base_match;
    string header;
    cin >> header;
    if (header != "#job_id,runtime_in_seconds,next_job_id") {
        cout << "Malformed Input" << endl;
        return 0;
    }
    string line;
    int index = 0;
    unordered_map<int, int> parent_table;
    unordered_map<int, int> index_table;
    unordered_map<int, vector<int>> summary;

    while (cin >> line) {
        if (regex_match(line, base_match, pattern)) {
            vector<int> nums = parseInts(line);
            // cout << nums << endl;
            if (!parent_table.count(nums[0])) {
                // new chain
                parent_table[nums[2]] = nums[0];
                index_table[nums[0]] = index;
                summary[index] = {nums[0], -1, 1, nums[1],
                                  -1};  // start, last, number of jobs, total time, average time
                index++;
            } else {
                // existing chain
                int parent = parent_table[nums[0]];
                int chain_no = index_table[parent];
                summary[chain_no][2]++;
                summary[chain_no][3] += nums[1];
                if (nums[2] != 0) {
                    parent_table[nums[2]] = nums[0];
                } else {
                    summary[chain_no][1] = nums[0];
                    summary[chain_no][4] = summary[chain_no][3] / summary[chain_no][2];
                }
            }

        } else
        {
            cout << "Malformed Input" << endl;
            break;
        }
    }

    cout << "-" << endl;
    for (auto item : summary) {
        cout << "start_job: " << item.second[0] << endl;
        cout << "last_job: " << item.second[1] << endl;
        cout << "number_of_jobs: " << item.second[2] << endl;
        int hour = item.second[3] / 3600;
        int min = item.second[3] / 60 % 60;
        int sec = item.second[3] % 60;
        cout << "job_chain_runtime: " << std::setfill('0') << std::setw(2) << hour << ":"
             << std::setw(2) << min << ":" << std::setw(2) << sec << endl;
        hour = item.second[4] / 3600;
        min = item.second[4] / 60 % 60;
        sec = item.second[4] % 60;
        cout << "average_job_time: " << std::setw(2) << hour << ":" << std::setw(2) << min << ":"
             << std::setw(2) << sec << endl;
        // cout << item.second << endl;
        cout << "-" << endl;
    }

    return 0;
}