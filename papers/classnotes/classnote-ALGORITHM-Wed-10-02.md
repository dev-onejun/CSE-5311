$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

#### Example

1. Give an example of a graph with 5 vertices in which DFS traversal is the same as BFS.

``` plaintext
A
 \
  B
   \
    C
     \
      D
       \
        E
```

DFS and BFS print same result

2. Design a tree with 5 nodes such that if you run DFS, size of stack will be the largest possible

``` plaintext
A
 \
  B
   \
    C
     \
      D
       \
        E
```

The largest possible size of stack is 5.

3. Design a tree with 5 nodes such that if you run BFS, size of queue will be the largest possible

``` plaintext
           A
        / | | \
       B  C D  E
```

The largest possible size of queue is 4.

4. Which statements are correct?

``` plaintext
a) Worst case of quick sort using median is same as heap sort -> O (nlogn and nlogn)
b) Worst case of quick sort is same as merge sort -> X (O(n^2) vs O(nlogn))
c) Heap sort has same worst case as merge sort -> O (nlogn and nlogn)
```

---
cf. 소팅 비교

||best|average|worst case|
|:--:|:--:|:--:|:--:|
|Quick Sort|nlogn|nlogn|n^2|
|Quick Sort using median|nlogn|nlogn|nlogn|
|Merge Sort|nlogn|nlogn|nlogn|
|Heap Sort|nlogn|nlogn|nlogn|
|Bubble Sort|n|n^2|n^2|
|Insertion Sort|n|n^2|n^2|
|Selection Sort|n^2|n^2|n^2|

---

5. Suppose that you implement a Heap with the largest element on the top (Max Heap). Which statement is true?

(When the array represent starts from index 1) -> A[1]: root, when A[k] -> parent: A[k/2], left child: A[2k], right child: A[2k+1]

``` plaintext
a) Parent of A[9] is A[16] -> X
b) left chld of A[8] is A[17] -> X
c) right child of A[8] is A[17] -> O
d) Grand parent of A[9] is A[2] -> O
e) Grand parent of A[8] is A[4] -> X
```

6. Suppose you are told an undirected graph has n vertices and n edges. Which statement is true?

``` plaintext
a) The graph may not have a cycle
b) The graph definitely has a cycle -> O
c) The graph has exactly one connected component
```

7. Given two sorted sets $S$ and $T$ which are the size of $n$. Sorting their union in the most efficient way take?

- $O(n)$
각각에서 하나씩 비교해서 pop 하면서 넣으면 O(2n) = O(n)

8. Quick Sort's running time depends on the selection of ...

``` plaintext
a) size of array
b) sequence of values
c) pivot element -> O
```

9. Visiting the root node after visiting left and right subtrees is called?

- post-order traversal

10. The minimum number of edges required to create a cyclic graph of n vertices?

- n

11. The minimum number of spanning tree in a connected graph?

- 1

12. In the max heap, we deleted the root node. What is the next step?

- Move the last node to the root and heapify ? 최대값인지 어케 앎?

13. All spaning tress of a graph G...

``` plaintext
a) have same number of edges and same number of vertices -> O (All have n-1 edges and n vertices)
b) have same number of edges and different number of vertices
c) have different number of edges and same number of vertices
```

14. Rebalancing AVL trees cost?

``` plaintext
a) O(1)
b) O(logn) -> O
c) O(n)
```

15. Suppose that we have an array of size $n$ containing numbers. The array is sorted.

    a. Find the maximum value in the array. What is the cost?

    - $O(1)$

    b. Find the average value of the array

    - $O(n)$: Sum all elements (and divide by $n$)

    c. Find the median value of the array

    - $O(1)$: A[n/2]

16. For each function below, give an a symptotic upper bound using big-O. You should choose your answer from the following list.

- O(n), O(n^2), O(2^n), O(log n), O(log^2 n), O(log^3 n), O(n^3), O(n^4), O(n^5), O(n logn), O(n^2 log n), O(n^6), O(n^7), O(n^8), and O(log log n).

    a. $100 n^3 - 7 n^3 + 14 n^2$
        - $O(n^3)$
    b. $100 n^3 - 100 n^3 + 7 n^2$
        - $O(n^2)$
    c. $log(7n^2)$
        - $O(log n)$
    d. $5 \log(\log n) + 4 \log^2 n$
        - $O(log^2 n)$
    e. $n + 100 + 2^n$
        - $O(2^n)$
    f. $n^3 (1 + 6n + n^2)$
        - $O(n^5)$
    g. $\log n (n + n^2)$
        - $O(n^2 log n)$
    h. $(n (2n + 5 + n^3))^2$
        - $O(n^8)$
    i. $\log(\log n) + 5 \log n$
        - $O(log n)$
    j. $\log_2 2^n$
        - $O(n)$

17. Full tree: every node except leaves has two children. (Is is less strict than complete tree)
Perfect tree: all internal nodes have 2 children and all leaves are same level (complete and full tree)

What is the minimum and maximum number of nodes in a full tree of height 6 ? (hint: a tree containing only root has height of 0)
**Q. If the height of the root is not written as 0, is it considered as 1?**

``` plaintext
Minimum
    O - 0
   / \
  O   O - 1
  /    \
  O     O - 2
  /      \
  O       O - 3
  /        \
  O         O - 4
  /          \
  O           O - 5
  /            \
  O             O - 6
```
The maximum: $2^{h+1} - 1 = 2^7 - 1 = 127$ (등비수열 합)

18. What is the minimum and maximum number of non-leaf nodes in a complete tree of height 5? (Non-leaf node 갯수만 세는 거!)
?

19. What is the minimum and maximum number of nodes in a balanced AVL tree of height 5?

``` plaintext
Minimum: 양 옆으로 2개의 브랜치로 height 5 만들고, avl tree 조건에 맞게 최소로 채워넣기 -> 20
Maximum: 2^6 - 1 = 63 (perfect tree)
```

20. Draw the AVL tree that results from inserting these keys 2,5,6,8,9,7 in this order into an initially empty AVL tree.

** AVL Tree rotation할 때 balance factor 안맞을경우, leaf에서부터 rotation해가며, root까지 rotation 해야하는 경우가 있다**














### References

$\tag*{}\label{n} \text{[n] }$
