#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <limits>
using namespace std;

int maxSubarraySum(const vector<int>& arr) {
    int currentMax = arr[0];
    int maxSoFar = arr[0];
    for (int i = 1; i < (int)arr.size(); i++) {
        currentMax = max(arr[i], currentMax + arr[i]);
        maxSoFar = max(maxSoFar, currentMax);
    }
    return maxSoFar;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        string line;
        if (!getline(cin, line)) break;  
        if (line == "END") break;

        stringstream ss(line);
        vector<int> numbers;
        int x;
        while (ss >> x) {
            numbers.push_back(x);
        }

        if (!numbers.empty()) {
            int result = maxSubarraySum(numbers);
            cout << result << "\n";
        }
    }
    return 0;
}
