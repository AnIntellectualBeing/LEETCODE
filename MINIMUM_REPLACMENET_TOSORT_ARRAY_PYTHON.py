def minimumReplacement(nums):
    ans = 0

    max_val = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        ops = (nums[i] - 1) // max_val
        ans += ops
        max_val = nums[i] // (ops + 1)

    return ans

if __name__ == "__main__":
    n = int(input())  # Read the number of elements in the array

    nums = []
    for _ in range(n):
        element = int(input())  # Read one element at a time
        nums.append(element)

    result = minimumReplacement(nums)  # Calculate the result

    print(result)  # Print the result
