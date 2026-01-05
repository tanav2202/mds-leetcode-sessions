class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashgod = {}
        temp_list = []
        for i in range(0,len(nums)):
            hashgod[nums[i]] = i
        for i in range(0, len(nums)):
            x = target - nums[i] #X is the other value
            if (x in hashgod) and (i != hashgod[x]):
                #Checking if other value is in hash table, and othervalue's index not equal to i(original value) 
                temp_list.append(i)
                temp_list.append(hashgod[x])
                return temp_list
