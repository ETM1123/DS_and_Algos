"""General algorithm for Binary Search"""
from typing import Callable

def BS(lo : int, hi : int, condition : Callable[[int], str], not_found_output : int = None) -> int:
  """
  1. Come up with a condition to determine whether the answer lies before, after or at a given position.
  2. Retrieve the midpoint and the middle element of the list.
  3. If it is the answer, return the middle position as the answer.
  4. If the answer lies before it, repeat the search with the first half of the list.
  5. If the answer lies after it, repeat with the second half of the list
  """
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

test_num = 100000000