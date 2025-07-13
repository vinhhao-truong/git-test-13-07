from typing import List

def trimNums (nums:List[int]):
  if nums[-1] == 0:
    return trimNums(nums[:-1])
  return nums

def jumpSteps(nums: List[int], checking:List[int], idx:int = -1, time:int = 0) -> bool:
  if time == 5:
    return True
  print(time)
  if len(nums) == 0:
    return False
  if len(nums) == 1:
    return True
  if len(checking) <= 1:
    return True
  
  if nums[0] == 0:
    return False
  
  if idx == -1:
    return jumpSteps(nums, nums[1:], )
  
  
  
        
  return False
      
print(jumpSteps([3,2,1,0,4]))