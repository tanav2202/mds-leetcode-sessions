class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rand = {}
        for i in range(len(nums)):
            rand[nums[i]] = i
        
        for i in range(len(nums)):
            x = target - nums[i]
            if x in rand and i != rand[x]:
                return [i , rand[x]]

        

        