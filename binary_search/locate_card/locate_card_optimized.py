"""Optimized solution to locate_card: O(log N)"""

def locate_card_binary_search(cards : list[int], query : int) -> int:
  """Binary Search:"""
  lo, hi = 0, len(cards)
  while lo <= hi:
    mid = (lo + hi) // 2
    result = test_location(cards, query, mid)
    if result == "found":
      return mid
    elif result == "left":
      hi = mid - 1
    else:
      lo = mid + 1
  return -1 
    
def test_location(cards : list[int], query: int , mid : int) -> str:
  mid_number = cards[mid]
  if mid_number == query:
    if mid - 1 >= 0 and cards[mid -1] == query:
      return "left"
    else:
      return "found"
  elif mid_number < query:
    return "left"
  else:
    return "right"
