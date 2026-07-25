class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        front = 0
        triplets = []
        while front <= len(nums) - 3:
            mid = front+1
            back = len(nums) - 1
            target = -nums[front]
            while mid < back:
                if nums[mid] + nums[back] < target:
                    temp = nums[mid]
                    while mid < back and nums[mid] == temp: mid+=1
                elif nums[mid] + nums[back] > target:
                    temp = nums[back]
                    while mid < back and nums[back] == temp: back -= 1
                else:
                    triplets.append([nums[front], nums[mid], nums[back]])
                    temp = nums[mid]
                    while mid < back and nums[mid] == temp: mid+=1
                    temp = nums[back]
                    while mid < back and nums[back] == temp: back -= 1
            temp = nums[front]
            while front <= len(nums) - 3 and nums[front] == temp: front += 1
        return triplets