class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = (len(nums)-1)/2

        d = defaultdict(int)

        for num in nums:
            if d[num] == majority:
                return num
            d[num] +=1
