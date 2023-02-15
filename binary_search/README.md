# Binary Search 

## Motivating Problem: 
Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them face down in a sequence on a table. She challenges Bob to pick the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card. 

**Observations**: In this problem, we can represent the sequence of cards as a list of numbers. Turning over a specific card is equivalent to accessing the value at the corresponding possible list.

For example: Given the following 8 cards (sorted in decreasing order): [13, 11, 12, 7, 4, 3, 1, 0], we want to determine whether our queried number is our list. For instance, our queried number can be 7.

**In other words**: We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of of times we access elements from the list.

**Input**: 
1. Cards: A list of numbers sorted in decreasing order
2. Query: A number whose position in the array is to be determined.

**Output**: position: The position of the query in the list. 

**Function signature**:
```Python
def locate_card(cards : list[int], query : int) -> int
  return -1
```

**Test cases we want to handle**:
1. The number query occurs somewhere in the middle of the list cards.
2. query is the first element in the cards.
3. query is the last element in the card
4. The list cards containing just one element, which is query,
5. The list cards does not contain number query.
6. The list cards is empty.
7. The list of cads containing repeating numbers.
8. The number query occurs at more than one position in cards. 

**Solution 1 - Brute Force: Linear Search**

`locate_cards_linear_search(cards, query)`
1. Create a variable `position` with value 0.
2. Check whether the number at index position in card equals query.
3. If it does, `position` is the answer and can returned from the function
4. If not, increment the value of `position` by 1, and repeat steps 2 to 5 till we reach the last position.
5. If the number was not fond, return -1

**Solution 1 - Complexity**: O(N) In the worse case scenario i.e the query is not in the list of cards, we have to touch every single card.

**Solution 2 - Optimized: Binary Search**
1. Find the middle element of the list
2. If it matches queried number, return the middle position as the answer
3. If it's less than the queried number, then search the first half of the list.
4. If it's greater than the queried number, then search the second half of the list.
5. If no more elements remain, return -1

**Solution 2 - Complexity**: O(log N) - Note at each iteration we are removing half of the cards.

Simple proof:

Initial length: N

$$
\begin{align*}
    i=1&: \frac{N}{2} \\
    i=2&: \frac{N}{4} \\
    i=3&: \frac{N}{8} \\
    . \\
    .\\
    .\\
    i=k&:\frac{N}{2^{k}}
\end{align*}
$$

Let the kth iteration of the array have length 1 (smallest possible element), then

$$
\begin{align*}
    1=& \frac{N}{2^{k}}  \\
    2^{k} =& N \\
     k =& \log{N} \\
\end{align*}
$$

**Generic Binary Search Algorithm**

Here is the general strategy behind binary search, which is applicable to a variety of problems:

1. Come up with a condition to determine whether the answer lies before, after or at a given position.
2. Retrieve the midpoint and the middle element of the list.
3. If it is the answer, return the middle position as the answer.
4. If the answer lies before it, repeat the search with the first half of the list.
5. If the answer lies after it, repeat with the second half of the list
