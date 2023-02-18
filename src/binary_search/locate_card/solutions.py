
def locate_card_linear_search(cards : list[int], query : int) ->int:
  """
  Liner Search Algorithm: O(N)
    1. Create a variable `position` with value 0.
    2. Check whether the number at index position in card equals query.
    3. If it does, `position` is the answer and can returned from the function
    4. If not, increment the value of `position` by 1, and repeat steps 2 to 5 till we reach the last position.
    5. If the number was not fond, return -1
  """
  # Create a variable position with value 0
  position = 0
  # Set up a loop for repetition
  while position < len(cards):
    # Check if element at current position matches the query
    if cards[position] == query:
      # Answer found!
      return position
    # Increment
    position += 1
  # Reached  at the end of the array
  return -1

#####################################################################

def locate_card_binary_search(cards : list[int], query : int) -> int:
  """Binary Search Algorithm: O(log N) optimized solution"""
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
  
##########################################################

from binary_search.binary_search import BS

def locate_card(cards : list[int], query : int) -> int:
  """Pythonic implementation: O(log N)"""

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

  return BS(0, len(cards)-1, condition, -1)