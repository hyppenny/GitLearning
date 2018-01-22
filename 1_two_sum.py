class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for idx, num in enumerate(nums, start=0):
            match = dic.get(target - num)
            if match is not None:
                return [match, idx]
            dic[num] = idx


assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
assert Solution().twoSum([3, 2, 4], 6) == [1, 2]