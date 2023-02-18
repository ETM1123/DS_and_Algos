# Binary Search 

**Generic Binary Search Algorithm**

Here is the general strategy behind binary search, which is applicable to a variety of problems:

1. Come up with a condition to determine whether the answer lies before, after or at a given position.
2. Retrieve the midpoint and the middle element of the list.
3. If it is the answer, return the middle position as the answer.
4. If the answer lies before it, repeat the search with the first half of the list.
5. If the answer lies after it, repeat with the second half of the list

**Complexity**: O(log N) - Note at each iteration we are removing half of the cards.

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