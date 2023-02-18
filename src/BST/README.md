# Binary Search Tree

Binary Search Tree (BST) is special data structure that comes from larger class of data structures called Binary Trees


**Binary Tree**: An inverted tree truck with branches. Each node in
tree has at most 2 children. Some vocab - the top node is called the 
root node and the bottom code are called the children.

![Binary Tree pic](https://res.cloudinary.com/practicaldev/image/fetch/s--od-naD9n--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://miro.medium.com/max/975/1%2APWJiwTxRdQy8A_Y0hAv5Eg.png)

**Binary Search Tree**: A binary search tree or BST is a binary tree that satisfies the following conditions:
 
1. The left subtree of any node only contains nodes with key less tha the node's key
2. The right subtree of any node only contains nodes with key greater than the node's key

It follows from the above conditions that every subtree of a binary search tree must also be a binary search tree.

![BST pic](data:image/png;base64,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)


**Height of a Binary Tree**: Let's find the relationship b/w the height of tree and nthe number of nodes a tree has. Thus,

For a tree height of ${k}$, the number of node at $i$ level can be expressed:

$$
\begin{align*}
i_{0} =& 1 = 2^{0} \\
i_{1} =& 2 = 2^{1} \\
i_{2} =& 4 = 2^{2} \\
i_{3} = & 8 = 2^{3} \\
\vdots \\
i_{k-1} =& 2^{k-1}
\end{align*}
$$

where $i_0$ corresponds to level o i.e the rot node. 

If the total number of nodes in the tree is $N$, then if follows that:

$N$ = 1 + $2^1$ + $2^2$ + $2^3$ + ... + $2^{k-1}$

We can simplify the expression above by doing the following:

$N + 1$ = 1+1 + $2^1$ + $2^2$ + $2^3$ + ... + $2^{k-1}$


$N + 1$ = $2^1$ + $2^1$ + $2^2$ + $2^3$ + ... + $2^{k-1}$


$N + 1$ = $2^2$ + $2^2$ + $2^3$ + ... + $2^{k-1}$


$N + 1$ = $2^3$ + $2^3$ + ... + $2^{k-1}$

...

$N + 1$ = $2^{k-1}$ + $2^{k-1}$

$N + 1$ = $2^{k}$

$k = \log(N+1) \le \log(N) + 1$

Thus to store $N$ records we require a balanced binary search tree (BST) of height, $k$, no larger than $\log(N) + 1$. 

**Traversing a Binary Tree**: Unlike a list-like data structure, there are multiplay ways of traversing a binary tree.
1. In-order 
2. Pre-order
3. Post-order

The following questions are frequently asked in coding interviews:

1. Write a function to perform the in-order traversal of a binary tree
2. Write a function to perform the pre-order traversal of a binary tree
3. Write a function to perform the post-order traversal of a binary tree.

**In-order**:
- Traverse the left subtree recursively in-order
- Traverse the current node
- Traverse the right subtree recursively in-order

![In-order trav pic](https://lh3.googleusercontent.com/QRTgAbTK-54jPLU87RN4OAXWlBu1WR36LyaANNQ_Pg0N2gKmM0k_30h5S68Dwm_2qledVGQd5Byltj16KO3J5ufZs1ipixS4DKpHTRITXDiHajiLXEjf_sY7Id7e8G7r4mhBbANn)

**Pre-order**:
- Traverse the current node
- traverse the left subtree recursively pre-order
- traverse the right subtree recursively pre-order

![Pre-order trav pic](https://lh5.googleusercontent.com/b9g2tL87bG9rK2JIMBbZUIVTev9yOmfeJlx8Y_pmUiVDSjpmeof97B6d6ok4p6qrwq8TX2NaRqJKo1uXcqxNGzuHhq4H3uSaICyJcb4ERwsxyF-YVy0Sakb2EjEqlGn__FG_Ml4k)

**Post-order**: 
- Traverse the left subtree recursively
- Traverse the right subtree recursively
- Traverse the current node 

![Pre-order trav pic](https://lh6.googleusercontent.com/dyKoxSFKtdnpEVpNOV1_460ovzzLqcIe7rRplr6YrUheWqVJgtk9GztN-QHkvbxtJlDCo8_Y5NzLevE0dNxsitYjV0o3hUruNwcxYDteBGTzNg9knB0kfOMMmtY5B7Xrie2tnd86)
