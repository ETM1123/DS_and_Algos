# Search in a Rotated Array

## Problem (Leetcode 38)
Given a rotated array, `nums`, and an integer `target`, find and return the index of `target`, if it is in `nums`, otherwise return -1. 

Assume array `nums` contain only unique elements.

**Definition**: An array $X$ is rotated $n$ times iff for all $x \in X$ is shifted $n$ times to the right and array $X$ is originally sorted in increasing order. 

For example the rotated array [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the [0, 2, 3, 4, 5, 6, 9] 3 time. 

**Observations**:  Let array $X$ be rotated $j$ times Then
1. $X$ is strictly increasing i.e $x_{i-1} < x_{i}$  for all $x\in X$ where $i \ne j$. However when $i = j$ then $x_{i-1} > x_i$.
2. The sub-arrays $X[:j]$, and $X[j+1:]$ are sorted. 

For example (the array above) [5, 6, 9, 0, 2, 3, 4] which was rotated 3 times, it's sub-arrays  [5, 6, 9], [0], [2, 3, 4] are sorted. Note the sub-arrays were obtained by knowing the the number of times the array was rotated.

In other words, given an array, `nums`, that is **rotated** unknown number of times, and a integer, `target`, we want to find the position `target` is in `nums`, if the `target` is not present in the array then return -1.

**Input**
1. Rotated array
2. Integer target

**Output** Position of target else -1


**Function signature**:
```python
def search(nums: list[int], target : int) -> int:
  return -1
```
**Test cases we want to handle**:
1. rotated list, with target in the first half
2. rotated list, with target in the second half
3. rotated list, with target not in the second list
4. empty list
5. one element list with target in list
6. one element list with target not in list
7. two element list sorted with target in list
8. two element list sorted with target not in list
9. sorted list with target in list
10. sorted list target not in list
11. A list rotated n-1 times, with target in list
12. A list rotated n-1 times, with target not in list



**Solution**

``search(nums, target)``
1. Find the number of times `nums` was rotated, call it `rotation_index`.
2. Check if the the number at `rotation_index` is the target i.e nums[rotation_index] = target
3. If it is, found target, return `rotation_index`
4. Else, create Left and right sub-arrays by splitting nums at rotation_index. Don't include the number at  `rotation_index`.
5. Use Binary search on the left and right sub-array to find `target`.
6. If the `target` is in the left sub-array then return `i` where `i` is the result of the Binary Search.
7. If the `target` in the right sub-array return 1 + `rotation_index` + `j`, where `j` is the result of the  Binary Search.
8. If the `target` is not in the sub-arrays then return -1

Note we can also use Binary Search to find the `rotation_index` i.e number times `nums` was rotated.

``count_rotation(nums)``
1. Find the middle element of the list
2. If the number to the left (middle position- 1) of the middle number is greater than the middle number then we  found the `rotation_index` and return the middle position
3. If the middle number is less than the last number in `nums` (note in pyhton we can access the last element with index -1) then search the first half of the list.
4. Else search the 2nd half of the list.
5. Repeat steps 1 - 4 until sub-arrays are empty
6. Return 0, i.e the array is already sorted or rotated 0 times

**Solution Complexity** O(log N)

The complexity of ``search(nums, target)`` is equivalent to the complexity of ``count_rotation(nums)`` + the complexity of Binary Search. Note complexity of  ``count_rotation(nums)`` is equivalent to the complexity of Binary Search. We know the complexity of Binary Search is O(log N). Thus, based on our reasoning, The complexity of ``search(nums, target)`` = O(log N) + O(log N) = O(log N).