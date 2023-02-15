"""Brute force solution to locate_card: O(N)"""

def locate_card_linear_search(cards : list[int], query : int) ->int:
  """
  Liner Search Algorithm:
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