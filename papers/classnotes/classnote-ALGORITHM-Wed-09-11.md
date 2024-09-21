$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

**Linear time selection problem**

step 1) if n is small n<6 -> sort it and return. k_th smallest
step 2) group the n elements into n/5

When $S = 35,15,54,61,83,39,14,7,3,5,42,96,11,12,17}$, group the elements in 5 becomes $S_1 = 35,15,54,61,83$ and $S_2 = 39,14,7,3,5$ and $S_3 = 42,96,11,12,17$.

step 3) sort each group and find the median of each group. $M_1 = 54, M_2 = 7, M_3 = 17$.

step 4) among medians of each group, find the median of medians. $M = 17$. and rearange the sequence of the small groups as $S_1 = 3,5,7,14,39$, $S_2 = 11,12,17,42,96$ and $S_3 = 15, 35, 54, 61, 83$

Cardinality |L| = $\frac{3n}{5} \times \frac{1}{2} = \frac{3n}{10}$, |R| = $n - \frac{3n}{10} = \frac{7n}{10}$.

if k = rank of m -> return m (# k_th smallest element)
elif k < rank of m -> return k_th smallest on set L (# recursive call)
elif k > rank of m -> return k-rank of m_th smallest on set R (# recursive call)

$$
T(n) = n + T(\frac{n}{5}) + T(\frac{7n}{10}) \\
\\
n + T(\frac{n}{5}) + T(\frac{7n}{10}) \le C \times n \\
n + C \times \frac{n}{5} + C \times \frac{7n}{10} \le C \times n \\
1 + \frac{C}{5} + \frac{7C}{10} \le C \\
\to C = 10
$$

The runtime is not lienar time (증명가능) since the constnat C ....

**Tree Data Structure**

Tree is a data structure that consists of nodes in a parent/child relationship. The top node is called the root of the tree. The node that has no children is called a leaf node. The path is called as a sequence of nodes from root to the specific node. Visiting means checking the value of the node. Traverse means passing through in a specific order. Keys are the values stored in the nodes.

The height of the tree is the length of the longest path from the root to a leaf node. The depth of a node is the length of the path from the root to the node. The level of a node is the depth of the node + 1. The height of the tree is the maximum depth of the tree.

Tree can 1) store data naturally forms a hierarchy, 2) provide moderate access/search (quicker than linked list and slower than array), 3) provide moderate insertion/deletion (quicker than array and slower than unordered linked list), 4) do not have upper limit on # of nodes (like linked lists and unlike arrays)

**Binary Tree**

Find maximum (or minimum) value: O(n) since it needs to traverse all the nodes. no order inside tree.

**Binary Search Tree**

Binary search tree is a binary tree that satisfies the following properties:

1. n of children of each node is at most 2.
2. The left subtree of a node contains only nodes with keys less than the node's key.
3. The right subtree of a node contains only nodes with keys greater than the node's key.
4. The left and right subtree must also be a binary search tree.
5. No duplicate nodes.

For any node n, p,q,n is 정해져있음. 그림 넣으면 좋을듯.

Operations: Insert, Search, pre-order traversal, in-order traversal, post-order traversal
Find: O(h), Insert: O(h), Delete: O(h) where h is the height of the tree.

Search Algorithm:

$$
\text{Find (value, root):} \\
\quad \text{if root is empty} \\
\quad \quad \text{return False} \\
\quad \text{if root.value == value} \\
\quad \quad \text{return True} \\
\quad \text{if value < root.value} \\
\quad \quad \text{return Find(value, root.left)} \\
\quad \text{if value > root.value} \\
\quad \quad \text{return Find(value, root.right)} \\
$$

Check if the tree is a binary search tree:

$$
\text{CheckBST(root, min, max):} \\
\quad \text{checkBST(root.left, left.min, left.max) is false} \\
\quad \quad \text{return False} \\
\quad \text{checkBST(root.right, right.min, right.max) is false} \\
\quad \quad \text{return False} \\
\quad \text{if root.value < left.max or root.value > right.min} \\
\quad \quad \text{return True} \\
\quad \text{else} \\
\quad \quad \text{return False} \\
$$

Insert a key in a binary search tree:

$$
\text{Insert(root, node):} \\
\quad \text{if root is empty} \\
\quad \quad \text{return node} \\
\quad \text{if node.value = root.value} \\
\quad \quad \text{do nothing} \\
\quad \text{elif node.value < root.value} \\
\quad \quad \text{root.left = Insert(root.left, node)} \\
\quad \text{elif node.value > root.value} \\
\quad \quad \text{root.right = Insert(root.right, node)} \\
$$

Find the node with the maximum/minimum value:

The maximum value is the rightmost node in the tree. The minimum value is the leftmost node in the tree.

**Heap**

Heap is a complete binary tree that satisfies the heap property. The heap property is that the key of each node is greater than or equal to the key of its parent. The root of the tree is the maximum element in a max-heap and the minimum element in a min-heap.

1. highest/lowest priority element is always stored at the root.
2. is not a sorted structure (partially sorted)
3. no specific relationship between the nodes of the tree.
4. is a complete binary tree which means all levels are completely filled except possibly for the last level and the last level has all keys as left as possible. (the possible height of the tree is log(n))

Heaps are useful when we want to remove the object with the highest/lowest priority.

![Heap as array representation](http://www.cse.hut.fi/en/research/SVG/TRAKLA2/tutorials/heap_tutorial/KekoTRAKLA-89_1.gif)

array at index k = 4. left child = 2k, right child = 2k+1, parent = k/2

How to construct a min heap with the following input: 35, 33, 42, 10, 14, 19, 27, 44, 26, 31

- Insert a value sequentially and heapify the tree. heapify is a process that swap a inserted value to the root if the value is the minimum. The swap is repeated from the leaf to the root.

For max heap, vice versa.

Max heap construction algorithm:
1. Create a node at the end of the heap.
2. Assign a value to the node.
3. Compare the value with the parent node.
4. If the value of the node is greater than the parent node, swap them.
5. Repeat until the node is greater than the parent node or the node is the root.

Max heap deletion algorithm: (So heap is only interested in the root(maximum/minimum value) pop?)
1. remove the root node.
2. move the last node of the last level to the root.
3. compare the values of the children with the root value
4. if the root value is smaller than the children, swap the root with the larger child.
5. repeat until the root value is larger than the children or the node is the leaf.

Heap sort:
1. Build a max heap from the input data.
2. The root of the heap is the maximum element. Pop the root and replace the root with the last element of the heap.
3. Heapify the root of the tree.
4. Repeat until the heap is empty.
-> maximum 을 하나씩 꺼내서 정렬하는 방법. O(nlogn)

$$
\text{HeapSort(A : array)} \\
\quad \text{BuildMaxHeap(A)} \\
\quad \text{for i = A.length downto 1} \\
\quad \quad \text{swap(A[1], A[i])} \\
\quad \quad \text{n = n - 1} \\
\quad \quad \text{heapify(A, 1)} \\

\text{BuildMaxHeap(A : array)} \\
\quad \text{n = n of elements in A} \\
\quad \text{for i = n/2 downto 1} \\
\quad \quad \text{heapify(A, i)} \\

\text{heapify(A : array, i : integer)} \\
\quad \text{left = 2i} \\
\quad \text{right = 2i + 1} \\
\quad \text{if left <= n and A[left] > A[i]} \\
\quad \quad \text{max = left} \\
\quad \text{else} \\
\quad \quad \text{max = i} \\
\quad \text{if right <= n and A[right] > A[max]} \\
\quad \quad \text{max = right} \\
\quad \text{if max != i} \\
\quad \quad \text{swap(A[i], A[max])} \\
\quad \quad \text{heapify(A, max)} \\
$$

**Disjoint Set**

A disjoint set consists of a number of items, each ()? stores an id, parent pointer. The pointers of elements are arranged to form one or more trees where each tree represents a set.
(If an elements' parent pointer, points to no other element, the element is representative item of the set)?
(a set may contain one or more elements)?

MakeSet(x): creates a new set with a parent pointer pointing to itself. -> O(1)
Find(x): follow the chain of parent pointers from x through the tree until to an element whose parent is itself. (the element is the representative of the set)? -> O(n)
Union(x, y): Find(x), Find(y), use `Find` to determine the roots of the trees x and y belong to. If the roots are distinct, trees are combined by attaching the root of one to the root of the other. -> O(n)

$\text{MakeSet(x)}$ \
$\quad \text{if x is not already present:}$ \
$\quad \quad \text{add x to the disjoint set tree}$ \
$\quad \quad \text{x.parent = x}$ \
$\quad \quad \text{x.rank = 0}$

$\text{Find(x)}$ \
$\quad \text{if x.parent != x}$ \
$\quad \quad \text{x.parent = Find(x.parent)}$ \
$\quad \text{return x.parent}$

![Disjoint set](https://algocoding.wordpress.com/wp-content/uploads/2014/09/uf2_union3.png)

How to optimize Disjoint set
1. union by rank: attach the tree with the smaller rank to the root of the tree with the larger rank.
    - both same rank: attach one to the other and increase the rank by 1.
    - different rank: attach the smaller rank tree to the larger rank tree.
2. path compression: make the found root as the parent of x so that we don't have to traverse the tree again. ?

$\text{Union(x, y)}$ \
$\quad \text{rootX = Find(x)}$ \
$\quad \text{rootY = Find(y)}$ \
$\quad \text{if rootX == rootY}$ \
$\quad \quad \text{return}$ \
$\quad \text{if rootX.rank < rootY.rank}$ \
$\quad \quad \text{rootX.parent = rootY}$ \
$\quad \text{else if rootX.rank > rootY.rank}$ \
$\quad \quad \text{rootY.parent = rootX}$ \
$\quad \text{else}$ \
$\quad \quad \text{rootX.parent = rootY}$ \
$\quad \quad \text{rootY.rank = rootY.rank + 1}$

### References

$\tag*{}\label{n} \text{[n] }$
