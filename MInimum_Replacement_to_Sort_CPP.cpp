#include <iostream>
#include <vector>

using namespace std;

long long minimumReplacement(vector<int>& nums) {
    long long ans = 0;

    int max = nums.back();
    for (int i = nums.size() - 2; i >= 0; --i) {
        const int ops = (nums[i] - 1) / max;
        ans += ops;
        max = nums[i] / (ops + 1);
    }

    return ans;
}

int main() {
    int n;
    cin >> n; // Read the number of elements in the array

    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i]; // Read the array elements
    }

    long long result = minimumReplacement(nums); // Calculate the result

    cout << result << endl; // Print the result

    return 0;
}
