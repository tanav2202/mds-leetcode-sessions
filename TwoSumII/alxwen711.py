class Solution:
    def twoSum(self, numbers, target: int):
        #nlogn able, start from largest then binary search in remaining array
        #do not forget to add 1 to indices at the end
        x = len(numbers)
        for i in range(x):
            b = x-i-1
            req = target-numbers[b]
            a = self.search(numbers,req,b)
            if a != -1:
                ans = list()
                ans.append(a+1)
                ans.append(b+1)
                return ans
    
    def search(self, nums, target: int, cap: int) -> int:
        # find specific value (if it exists) in first 'cap' values of list
        high = cap-1
        low = 0
        while high - low > 1:
            mid = (low+high)//2
            if nums[mid] == target: return mid
            elif nums[mid] > target: high = mid
            else: low = mid
        if nums[low] == target: return low
        if nums[high] == target: return high
        return -1
    
            
        