# 1D Peak Finding 

## Problem (Leetcode )
Given an array, `nums`, of integers, find a **peak** in array `nums`. 

**Definition** Given an Array $X$ with $x_1$, $x_2$, $\cdots$, $x_n$ elements, element $x_i$ is a peak if and only iff $x_i > x_{i-1}$ and $x_i > x_{i+1}$. In other words, $x_i$ is greater than both of its adjacent neighbors. 

**Additional properties on array** $X$
1. Unique adjacent neighbors: $x_i \ne x_{i+1}$ for $x_i \in X$.
2. Length bounds: $1 \le X.length \le n$
3. Value bounds: $x_1 > -\infty $ and $x_n > -\infty$ for all $x \in X$. 

The third property of $X$ claims that for any boundary element of $X$ (first or last element of $X$) is a peak if the proceeding or prior element is less than the boundary element. In other words,

For all $x_i \in X$,
1. $x_1$ is a peak if $x_1 > x_2$ and 
2. $x_n$ is a peak if $ x_n > x_{n-1}$

This also implies that a one element array, has a peak at its only element. 

Properties (1) and (3) implies that array $X$ will always have a peak.

**Input**
1. Array of integers, `nums`

**Output**
1. The location of the peak in `nums`, integer

**Function signiture**:
```Python
def find_peak(nums : list[int])->int:
  return -1
```

**Test cases we want to handle**
1. one element array
2. two element array, with first element as peak
3. two element array, with second element as peak
4. n element array, with first element as peak
5. n element array, with last element as peak
6. n element array, with last n/2 element as peak
7. n element array, with peak in the first half of the array
8. n element array, with peak in the second half of the array

**Solution**

```find_peak(nums)```
1. Compute the middle index of `nums`, `mid`
2. Check if `nums[mid]` < `nums[mid - 1]` if so focus search on left half of the array
2. Check if `nums[mid]` < `nums[mid + 1]` if so focus search on right half of the array
3. Otherwise, return `mid`


**Complexity** O(log N)