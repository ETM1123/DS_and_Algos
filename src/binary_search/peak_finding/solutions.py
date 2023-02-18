from binary_search.binary_search import BS

def find_peak(nums : list[int]) -> int:
  def condition(mid : int) -> str:
    if mid != 0 and mid !=  len(nums) - 1:
      if nums[mid] < nums[mid - 1]:
        return "left"
      elif nums[mid] < nums[mid + 1]:
        return "right"
      else:
        return "found"
    elif mid == 0:
      if nums[mid] > nums[mid + 1]:
        return "found"
      else:
        return "right"
    else: # mid == len(nums) -1
      if nums[mid] > nums[mid - 1]:
        return "found"
      else:
        return "left"
  
  lo, hi = 0, len(nums) - 1
  # One or empty element array
  if hi <= 0:
    return hi
  # Two element array
  elif hi + 1 == 2:
    if nums[lo] > nums[hi]:
      return lo
    else:
      return hi
  else:
    return BS(lo, hi, condition)