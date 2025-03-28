class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort the array
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicates
                continue

            left, right = i + 1, n - 1

            while left < right:
                sum_value = nums[i] + nums[left] + nums[right]

                if sum_value == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Move pointers to skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif sum_value < 0:
                    left += 1  # Need a bigger number
                else:
                    right -= 1  # Need a smaller number

        return result

