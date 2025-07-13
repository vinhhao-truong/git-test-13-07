from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
        hashed_nums = {}
        
        for i in range (len(nums)):
            if type(hashed_nums.get(nums[i])) is int:
                hashed_nums[nums[i]] = [hashed_nums.get(nums[i]), i]
            else:
                hashed_nums[nums[i]] = i
                
        for i in range (len(nums)):
            remain = target - nums[i]
            if hashed_nums.get(remain) != None:
              if hashed_nums.get(remain) != i:
                  if type(hashed_nums.get(remain)) is int:
                      return [i, hashed_nums.get(remain)]
                  else:
                      return hashed_nums.get(remain)
        
print(twoSum([2,5,5,11], 10))