class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        window = [] 

        for i, num in enumerate(nums):
            
            pos_left = bisect_left(window, num - valueDiff)

            if pos_left < len(window) and abs(window[pos_left] - num) <= valueDiff:
                return True

     
            insort(window, num)

            if i >= indexDiff:
                old_val = nums[i - indexDiff]
                del window[bisect_left(window, old_val)]

        return False
            