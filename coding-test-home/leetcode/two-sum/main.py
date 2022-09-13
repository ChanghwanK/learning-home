from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answers = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    answers.append(i)
                    answers.append(j)

        return answers

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i+1)]


# print(solution.twoSum([2, 7, 11, 15], 9))
# print(solution.twoSum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum2([2, 7, 11, 15], 9))
