$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

**Tree Traversals**

Breadth First Traversal
Depth First Traversal

*Level Order Traversal*

Method 1: uses 2 functions -> $O(n^2)$

``` python
def print_level_order(tree):
    for d in range(1, height(tree) + 1):
        print_given_level(tree, d)

def print_given_level(tree, level):
    if tree is Null:
        return
    if level == 1: # if target node
        print(tree.data)
    elif level > 1:
        print_given_level(tree.left, level - 1)
        print_given_level(tree.right, level - 1)
```

Method 2: uses a queue

``` python
def print_level_order(tree):
    create an empy queue
    temp_node = root
    while temp_node is not null:
        print temp_node.data
        enqueue temp_node.left
        enqueue temp_node.right
        dequeue a node from queue and assigin it to temp_node
```

Depth First Traversal

Tree 있다고 할 때
  A
 B  C
D E F G

1) In_order Traversal: D, B, E, A, F, C, G

```
until all nodes are visited:
    step 1) recursively visit left subtree
    step 2) visit root
    step 3) recursively visit right subtree
```

2) Pre_order Traversal: A, B, D, E, C, F, G

```
until all nodes are visited:
    step 1) visit root
    step 2) recursively visit left subtree
    step 3) recursively visit right subtree
```

3) Post_order Traversal: D, E, B, F, G, C, A

```
until all nodes are visited:
    step 1) recursively visit left subtree
    step 2) recursively visit right subtree
    step 3) visit root
```

Example

```
        25
       / \
    15          50
   /   \      /    \
  10   22    35    70
 / \   / \   / \   / \
4  12 18 24 31 44 66 90
```
In_order: 4, 10, 12, 15, 18, 22, 24, 25, 31, 35, 44, 50, 66, 70, 90
Pre_order: 25, 15, 10, 4, 12, 22, 18, 24, 50, 35, 31, 44, 70, 66, 90
Post_order: 4, 12, 10, 18, 24, 22, 15, 31, 44, 35, 66, 90, 70, 50, 25

When inserting a node into a Binary Search Tree, find median of the array is important

```
def repeat_median(S) ??
    M = median(S)
    Partition S into L(Smaller), M, R(Larger)
    root = M
    root.left = repeat_median(L)
    root.right = repeat_median(R)
    return root
```

DELETE -> $O(h)$
Case 1 node -> has no children
15
10 20
    25
Delete 25 -> just delete it

Case 2 node has one child (replace with child)
15
10 20
    25
Delete 20 -> replace with 25, connecting 25 to 15

Case 3. node has 2 children
15
/ \
10 20
   / \
   18 30
   / \  \
  16 19  30
          \
          50

Delete 20 -> replace with 19, connecting 19 to 15 (maximum of left or minimum of right ? 둘 중 하나는 어떻게 결정? 그냥 마음대로인 거 같긴 한데)

```
Delete (X):
    if X is a leaf:
        delete X
    if X has one child(left):
        find Max of left subtree -> M
        bring M to X's position
        delete M
    if X has one child(right):
        find Min of right subtree -> M
        bring M to X's position
        delete M
    if X has two children:
        find Max of left subtree -> M
        bring M to X's position
        delete M
```

In summary, it is important that BST is balanced. To 보장, AVL Tree is proposed.

AVL Tree is a self-balancing Binary Search Tree where the difference between heights of left and right subtrees cannot be more than 1 for all nodes. 모든 각 서브트리의 루트 노드에서 왼쪽, 오른쪽 서브트리의 높이 차이가 1 이하여야 함

1 is called as balance factor

To store the structure of AVL Trees, AVL rotations are used. There are 4 types of rotations
1) Left rotiation
2) Right rotation
3) Left-Right rotation
4) Right-Left rotation

If a tree become unbalanced because a node was inserted into right subtree of the right subtree. Then, we need to do left rotation. (A\B\C -> A/B\C)
If a tree become unbalanced because a node was inserted into left subtree of the left subtree. Then, we need to do right rotation. (C/B/A -> C/B\A)
If a tree become unbalanced because a node was inserted into right subtree of the left subtree. Then, we need to do left-right rotation. (A/B\C -> A\B\C) 일자로 펴주고, right rotation
If a tree become unbalanced because a node was inserted into left subtree of the right subtree. Then, we need to do right-left rotation. (C/B/A -> C/B\A) 일자로 펴주고, left rotation
예시 문제 꼭 보기. 70이 왜 60 오른쪽으로?

What is the maximum height of a balanced AVL Tree with 7 nodes (Assume height of a tree containing only root is O ?)? -> 3

Cost of search in AVL tree is O(log n) but in BST is O(n)

**Red Black Tree** : 유튜브 찾아봐야 할듯,,,

Red Black Trees are a BST with one extra attribute: color (red or black) for each node.

1. Every node is either red or black
2. Root is always black
3. if a node is red, its childrens(both) are black
4. every simple path from root node to leaves contains the same number of black nodes

Operations: Insert, lookup, remove, print

Insert operation:
    If we inserting into a nonempty tree,
        1) Use BST insert algorithm to add K to the tree
        2) Color the node containing K red
        3) Restore red-black tree properties

    if K -> color it black if k-> root ? empty일 때 얘기하는 건가

    When we insert K, double red problem may occur.
        case 1) K's parent is black -> no problem
        case 2) K's parent is red -> 3rd properties of red-black tree is violated
            Let P for K's parent, G for K's grandparent.
                case 2.a) P's sibling is black or Null
                    ...
                case 2.b) Parent's sibiling is red
                    no rotation is required. just recoloring
                        colored P and S as black
                        colored G as black if G is root, otherwise red

Practice

1. Create a red black tree by inserting  values in the following order into an empty red black tree: 8, 18, 5, 15, 17, 25, 40, 80
기본적으로 Red color로 넣고, properties에 어긋나는 게 있으면 recolroring 하는거 같은데

height에 log n의 upper bound가 있음
Insert Time complexity: finding O(log n) + coloring O(1) + restoring O(log n) => O(log n)

delete, lookup은 안할거라는데?

2. A claim, "in Red and Black trees, height of longest possible path <= 2x length of shortest path" is true? -> correct.                                    "

**Splay Trees**

- Another types of BST.
- Bring recently accessed node to the root node.
- Every operation plays at the root node.
- Every operation involves a common operation "splaying" which brings the target node to the root
- rotation
    zig rotation: every item moves one position to the right
    zag rotation: evvery item moves one position to the left
    zig zig rotation: every item moves two position to the right
    zag zag rotation: every item moves two position to the left
    zia zag rotation: every node moves one position to the right followed by one position to the left
    zag zig rotation: every node moves one position to the left followed by one position to the right

- Insertion into splay tree
    step 1) check if tree is empty
    step 2) if empty, insert the node (becoming root) to tree
    step 3) if not empty, find 맞는 position with BST insertion algorithm
    step 4) splay the node into the root


이름과 효과만 일단 알고 있으면, 구현은 가져다 써도 되자너 ,,


### References

$\tag*{}\label{n} \text{[n] }$
