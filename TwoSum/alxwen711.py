class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Note: only values that appear at most twice actually need
        to be considered by the constraints of the problem

        Technically O(n) even though this uses 2 passthroughs of the array; 1 passthrough solution is possible
        """
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]) == None: d[nums[i]] = list()
            d[nums[i]].append(i)
        for j in range(len(nums)):
            t = target-nums[j]
            if d.get(t) != None:
                if d[t][0] != j: return [j,d[t][0]]
                elif len(d[t]) != 1: return [j,d[t][1]]
        return [] # no sol found (impossible)
        