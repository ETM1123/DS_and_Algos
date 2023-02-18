"""Count rotation"""
from typing import Callable

def binary_search(lo : int, hi : int, condition: Callable[[int], str], not_found_output) -> int:
  while lo <= hi:
    mid = (lo + hi) // 2
    result = condition(mid)
    if result == "found":
      return mid
    elif result == "left":
      hi = mid - 1
    else:
      lo = mid + 1
  return not_found_output

def count_rotation(nums : list[int]) -> int:
  def condition(mid : int) -> str:
    if nums[mid - 1] > nums[mid]:
      return "found"
    elif nums[mid] < nums[-1]:
      return "left"
    else:
      return "right"
  return binary_search(0, len(nums) - 1, condition, 0)