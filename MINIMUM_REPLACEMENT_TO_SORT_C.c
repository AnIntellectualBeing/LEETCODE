#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n); // Read the number of elements in the array

    int nums[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]); // Read the array elements
    }

    int ans = 0;

    int max = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        int ops = (nums[i] - 1) / max;
        ans += ops;
        max = nums[i] / (ops + 1);
    }

    printf("%d\n", ans); // Print the result

    return 0;
}
