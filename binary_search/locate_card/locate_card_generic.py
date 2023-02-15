"""Pythonic way of implementing BS"""

from typing import Callable

def binary_search(lo : int, hi : int, condition : Callable[[int], str]) -> int:
  while lo <= hi:
    mid = (lo + hi) // 2
    result = condition(mid)
    if result == "found":
      return mid
    elif result == "left":
      hi = mid - 1
    else:
      lo = mid + 1
  return - 1

def locate_card(cards : list[int], query : int) -> int:
  
  def condition(mid : int) -> str:
    if cards[mid] == query:
      if mid > 0 and cards[mid - 1] ==query:
        return "left"
      else:
        return "found"
    elif cards[mid] < query:
      return "left"
    else:
      return "right"
  
  return binary_search(0, len(cards)-1, condition)