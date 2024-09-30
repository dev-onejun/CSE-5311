$$
\begin{array}{c}
\huge{\text{Homework #2}} \\
\hline
\text{Wonjun Park} \\
\text{UTA ID: 1002237177} \\
\href{mailto:wxp7177@mavs.uta.edu}{\text{wxp7177@mavs.uta.edu}}
\end{array}
$$

##### 1. Answer the following questions regarding Binary trees:

$\quad$ **1. What are the least and greatest number of leaf nodes in a binary tree with n nodes, show with examples? (7.5 p)** \
$\qquad$ The least number of leaf nodes in a binary tree with $n$ nodes is 1. For example, if a tree was constructed as completely unbalanced where each node has only one child, the binary tree would have only one leaf node. \
$\qquad$ The greatest number of leaf nodes in a binary tree with $n$ node is $\left\lfloor \frac{n + 1}{2} \right\rfloor$. For example, if a tree was a complete binary tree which filled from left to right, the binary tree would have $\left\lfloor \frac{n + 1}{2} \right\rfloor$ leaf nodes. \
$\quad$ **2. What is the relationship between the number of nodes in a full binary tree and the number of leaf nodes, show with an example? (7.5 p)** \
$\qquad$ A full binary tree is a binary tree which each node has either 0 or 2 children so that the number of nodes in the tree $n_t$ increases by 2 for each node. In other words, the number of nodes in a full binary tree is an arthmetic sequence with a common difference of 2 and the first term of 1 (the root node). The number of leaf nodes $n_l$ in a full binary tree increases by 1 for each node. In other words, it is an arthmetic sequence with a common difference of 1 and the first term of 1. \
$\qquad$ In summary,

$$
\begin{aligned}
& n_t = 2 \times N - 1 & N \in \mathbb{Z} \\
& n_l = N & N \in \mathbb{Z}
\end{aligned}
$$

$\qquad$ Therefore, the relationship between them is $\mathbf{n_t = 2 \times n_l - 1}$. The following are examples of a full binary tree with 7 nodes and 4 leaf nodes as well as with 5 nodes and 3 leaf nodes.

``` plaintext
Example 1          Example 2
    1                   1
   / \                 / \
  2   3               2   3
 / \ / \             / \
4  5 6  7           4   5
```


##### 2. Answer the following questions regarding Binary Search trees:

$\quad$ **1. Insert the following 15 randomly generated objects into a binary search tree in the order they are listed (show each step). (10 p)**
$$24, 13, 68, 62, 66, 22, 58, 80, 2, 59, 23, 54, 1, 15, 95$$

$\qquad$ The following is the binary search tree after inserting the 15 objects in the order they are listed.

``` plaintext
            24
          /    \
         /      \
        13      68
       /  \    /  \
      2   22  62  80
     /   / \  / \   \
    1  15 23 58 66  95
             / \
            54 59
```

$\quad$ **2. Give five integers that could be inserted into this tree that would increase the height of this tree (5 integers  that can (separately) increase the height of the tree by 1). please note that you are not actually inserting these values to the tree. explain your answer(5 p)** \
$\qquad$ To increase the height of the tree in 1), a number in the range between 24 and 54 is needed to be inserted. Therefore, \
$\qquad\qquad$ 25, 26, 27, 28, 29 \
$\qquad$ satisfy the condition. \
$\quad$ **3. Remove the root node( from part A)four times by copying up the smallest element of the right sub-tree, show each step and the final tree. (10 p)** \
$\qquad$ The following is the binary search tree after removing the root node four times by copying up the smallest element of the right sub-tree.

``` plaintext
            54                        58                          59                          62
          /    \                    /    \                      /    \                      /    \
         /      \                  /      \                    /      \                    /      \
        13      68                13      68                  13      68                  13      68
       /  \    /  \              /  \    /  \                /  \    /  \                /  \    /  \
      2   22  62  80            2   22  62  80              2   22  62  80              2   22  66   80
     /   / \  / \   \          /   / \  / \   \            /   / \   \    \            /   / \        \
    1  15 23 58 66  95        1  15 23 59 66  95          1  15  23  66   95          1  15  23       95
              \
              59
```

##### 3. Insert the following n objects, in the order given, into a binary min-heap and place your answer into an array (15 p)

$$5, 3, 9, 7, 2, 4, 6, 1, 8$$

$\qquad$ The following is the binary min-heap after inserting the 9 objects in the order they are listed,

``` plaintext
            1
          /    \
         /      \
        2        4
       /  \     / \
      3    5   9   6
     / \
    7   8
```

$\qquad$ and the list below is the array after inserting the 9 objects in the order they are listed.

$$[1, 2, 4, 3, 5, 9, 6, 7, 8]$$

##### 4. Answer the following questions regarding AVL trees:

$\quad$ **1. Insert the following sequence of elements into an AVL tree, starting with an empty tree (show each step) : 12, 24, 14, 27, 35, 17, 19, 22. (10 points)**

``` plaintext
1)        |2)        |3)                                |4)
12        |12        |12        12            14        |    14
          |  \       |  \         \          /  \       |   /  \
          |   24     |   24        14       12   24     |  12   24
          |          |  /            \                  |         \
          |          | 14            24                 |         27
```

``` plaintext
5)                                    |6)
    14                  14            |    14              14                24
   /  \                /  \           |   /  \            /  \              /  \
  12   24             12   27         |  12   27         12   24           14   27
         \                /  \        |      /  \            /  \         /  \    \
          27             24  35       |     24  35         17   27       12  17    35
            \                         |    /                      \
             35                       |   17                      35
```

``` plaintext
7)                     |8)
        24             |      24                  24
       /  \            |     /  \                /  \
      14   27          |   14    27             14   27
     /  \    \         |  /  \     \           /  \    \
    12  17    35       | 12  17     35        12  19    35
          \            |       \                 /  \
          19           |       19               17  22
                       |         \
                       |         22
```

$\quad$ **2. Delete 27 in the AVL tree that you got(show each step). (10 p)**

``` plaintext
    24             24            19
   /  \           /  \          /  \
  14   35        19   35       14   24
 /  \           /  \          /  \  / \
12  19         14  22        12  17 22 35
    / \       /  \
   17 22     12  17
```

$\quad$ **3. What maximum difference in heights between the leaves of a AVL tree is possible (in terms of Big O)? (5 p)** \
$\qquad$ In terms of Big O, the height of an AVL tree with $n$ nodes is $O(h) = O(\log n)$. Following the definition of AVL Tree, the shortest possible path from the root to a leaf is $O(h - 1) = O(\log n - 1)$ and the longest possible path from the root to a leaf is $O(h) = O(\log n)$. \
$\qquad$ Therefore, the maximum difference in heights between the leaves of an AVL tree is $O(\log n) - O(\log n - 1) = O(\log n)$.

##### 5. Answer the following questions regarding Red Black trees:

$\quad$ **1. What are the operations that could be performed in O(log n) time complexity by red-black tree? (5 p)** \
$\qquad$ The operations that could be performed in $O(\log n)$ time complexity by red-black tree are search, insert, and delete. \
$\quad$ **2. Insert the following sequence in to a red black tree (show each step): 5, 6, 1, 9, 2, 4, 3, 8, 7 (15 p)**

$$
\begin{array}{c|c|c}
\hline
\text{1)} & \text{2)} & \text{3)} \\
\hline
\begin{array}{ccccccccccc}
& &  &  &  & 5  &  &  &  &  &  \\
\end{array} &
\begin{array}{ccccccccccc}
& &  &  &  & 5 &  &  &  &  &  \\
& &  &  &  &   & \text{\\} & &  &  &  \\
& &  &  &  &  &  &  \color{red}{6}&  &  &  \\
\end{array} &
\begin{array}{ccccccccccc}
& &  &  &  & 5 &  &  &  &  &  \\
& &  &  & \text{/}  &   & \text{\\} & &  &  &  \\
&  &  & \color{red}{1} &   &  &  &  \color{red}{6} &  &  &  \\
\end{array} \\
\hline
\text{4)} & \text{5)} & \text{6)} \\
\hline
\begin{array}{ccccccccccc}
& &  &  &  & 5 &  &  &  &  &  \\
& &  &  & \text{/}  &   & \text{\\} & &  &  &  \\
& &  &  &  1 &  & 6 &  &  &  &  \\
& &  &  & & & & \text{\\} &  &  &  \\
& &  &  &  &  &  &  &  \color{red}{9} &  &  \\
\end{array} &
\begin{array}{ccccccccccc}
& &  &  &  & 5 &  &  &  &  &  \\
& &  &  & \text{/}  &   & \text{\\} & &  &  &  \\
&  &  & 1 &   &  &  &  6 &  &  &  \\
& &  & & \text{\\} & & & \text{\\} &  &  &  \\
& &  &  &  & \color{red}{2} &  &  &  \color{red}{9} &  &  \\
\end{array} &
\begin{array}{ccccccccccc}
& &  &  &  & 5 &  &  &  &  &  \\
& &  &  & \text{/}  &   & \text{\\} & &  &  &  \\
&  &  & 2 &   &  &  &  6 &  &  &  \\
& & \text{/} & & \text{\\} & & & \text{\\} &  &  &  \\
& \color{red}{1} &  &  &  & \color{red}{4} &  &  &  \color{red}{9} &  &  \\
\end{array} \\
\hline
\text{7)} & \text{8)} & \text{9)} \\
\hline
\begin{array}{ccccccccccc}
& &  &  &  & 5 &  &  &  &  &  \\
& &  &  & \text{/}  &   & \text{\\} & &  &  &  \\
&  &  & \color{red}{2} &   &  &  &  6 &  &  &  \\
& & \text{/} & & \text{\\} & & &  & \text{\\} &  &  \\
& 1 &  &  &  & 4 &  &  &   &  \color{red}{9} &  \\
& & &  & \text{/}& & & &  &  &  \\
& &  & \color{red}{3} &  &  &  &  &   &  &  \\
\end{array} &
\begin{array}{ccccccccccc}
& &  &  &  & 5 &  &  &  &  &  \\
& &  &  & \text{/}  &   & \text{\\} & &  &  &  \\
&  &  & \color{red}{2} &   &  &  &  8 &  &  &  \\
& & \text{/} & & \text{\\} & & \text{/}  &  & \text{\\} &  &  \\
& 1 &  &  &  & 4 & \color{red}{6} &  &  &  \color{red}{9} &  \\
& & &  & \text{/}& & & &  &  &  \\
& &  & \color{red}{3} &  &  &  &  &   &  &  \\
\end{array} &
\begin{array}{ccccccccccc}
& &  &  &  & 5 &  &  &  &  &  \\
& &  &  & \text{/}  &   & \text{\\} & &  &  &  \\
&  &  & \color{red}{2} &   &  &  &  \color{red}{8} &  &  &  \\
& & \text{/} & & \text{\\} & & \text{/}  &  & \text{\\} &  &  \\
& 1 &  &  &  & 4 & 6 &  &  &  9 &  \\
& & &  & \text{/} & & &\text{\\}  &  &  &  \\
& &  & \color{red}{3} &  &  &  & \color{red}{7}  &   &  &  \\
\end{array}
\end{array}
$$
