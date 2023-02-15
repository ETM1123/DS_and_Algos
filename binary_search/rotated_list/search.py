"""Search"""
from count_rotation import binary_search, count_rotation

def search(nums : list[int], target : int) -> int:
  def condition(mid):
    if nums[mid] == target:
      return "found"
    elif nums[mid] > target:
      return "left"
    else:
      return "right"
  
  if len(nums) > 0:
    rotation_index = count_rotation(nums)  
    if nums[rotation_index] == target:
      return rotation_index
    else:
      left_sub_array_target_pos = binary_search(0, rotation_index, condition, -1)
      right_sub_array_target_pos = binary_search(rotation_index + 1, len(nums) - 1, condition, -1)
      if left_sub_array_target_pos != -1:
        return left_sub_array_target_pos
      elif right_sub_array_target_pos != -1:
        return 1 + rotation_index + right_sub_array_target_pos
      else:
        return -1 
  else:
    return -1