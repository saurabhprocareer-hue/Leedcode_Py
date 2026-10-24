class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i,val in enumerate(nums):
            remainingVal = target - val
            if remainingVal in hashmap:
                return [i,hashmap[remainingVal]]
            hashmap[val] = i
        return []