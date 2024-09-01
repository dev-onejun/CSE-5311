# Approximation of Computational Cost: A Review of Algorithm Design and Analysis

$$
\mathbf{\text{Wonjun Park}} \\
\text{Computer Science} \\
\text{University of Texas at Arlington} \\
\text{Arlington, TX, United States}
$$

##### *Abstract*

$$
\mathbf{\text{Acronym and Abbreviation}} \\
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

### I. Introduction

### II. Literature Review

#### A. Basic Definition in Algorithms

##### Big O Notation

*Big O Notation* represents how long an algorithm takes time to run, enabling to predict the performance as the input gets arbitrarily large. The rules of *Big O Notation* are that **1)** drop the constant (ex. $O(1 + {n \over 2} + 100 \to O(n)$), **2)** drop less significant terms (ex. $O(n + n^2) \to O(n^2)$), and **3)** usually talks about the worst case. $\text{Fig 1}$ is the comparison of the complexity among all types of *Big O Notation*.

$$
\underrightarrow{\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Complexity\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ } \\
\begin{array}{cccccccc}
O(1) & O(\log{N}) & O(N) & O(N \log{N}) & O(N^2) & O(N^3) & O(2^N) & O(N!) \\
Constant & Logarithmic & Linear & N \times \log{N} & Quadratic & Cubic & Exponential & Factorial
\end{array}
$$
$\text{Fig 1. The Complexity of Big O Notation}$

This relationship between the original function $T(n)$ and the function in *Big O Notation* $F(n)$ is referred as $C \times F(n)$ is asymptotically bigger than $T(n)$ [[1](#mjx-eqn-1), [2](#mjx-eqn-2)]. The relationship derives to the formal definition of *Big O Notation*. The formal definition of *Big O Notation* is that there are variables constant $C$ and $n$ where $n \ge n_0$, which are met the formula $T(n) \le C \times F(n)$ for the notation of $T(n) = O(F(n))$. Take $T(n) = 3n^2 + 4$ for example. The *Big O Notation* of $T(n)$ is $O(n^2)$ so that $F(n)$ becomes $n^2$. Are there any variables of $C$ and $n$ which satisfy the formula $T(n) \le C \times F(n)$? The smallest $C$ which may meet the requirement is 4. With the derived formula $3n^2 + 4 \le 4 \times n^2$, the smallest $n$ which meet the formula is 2. After 2, the formula is always true.

For wrapping up, these steps are explained as three steps: **1)** Find $F(n)$ as transforming the given function $T(n)$ with *Big O Notation*. **2)** Find the smallest $C$ which may meets the propotional expression $T(n) \le C \times F(n)$. **3)** Find the smallest $n$ which satisfies the requirement.

In summary, when the formula is given in the form of $T(n) = O(L(n))$, the comparision, $T(n) \leq c \cdot L(n)$, is always true if both a constant $c$ and a value $n$, which is larger than $n_0$, are exist.

The following python code shows *Time Complexity* of each function with *Big O Notation*.

``` Python
def print_first_item(items): # O(1): Order of one. Constant.
    print(item[0])

def print_all_items(items): # O(n): Order of n. Linear time.
    for item in items:
        print(item)

def print_all_possible_pairs(items): # O(n^2): Order of n square. Quadratic time.
    for item_a in items:
        for item_b in items:
            print(item_a, item_b)

def is_contain(haystack, needle): # Best: O(1), Worst: O(n) | -> O(n)
    for item in haystack:
        if needle == item:
            return True
    return False
```

*Space Complexity* also uses *Big O Notation* to express the complexity. Two functions below present their space complexity as one does not allocate any memory and the other stores $n$ variables in `hi_list`.

``` Python
def say_hi_n_times(n): # Space Complexity: O(1)
    for time in range(n):
        print('hi')

def list_of_hi_n_times(n): # Space Complexity: O(n)
    hi_list = []
    for time in range(n):
        hi_list.append(time)
```

In summary, *Time complexity* refers to time cost of algorithms and *Space Complexity* talks about memory cost.

##### Big-$\theta$ (Theta) Notation

Big-$\theta$ notation describes the upper and lower bounds of the complexity of an algorithm. In other words, the notation describes the tight bound of the complexity. Likewise **Big-O Notation**, the notation **1)** drop the constant, **2)** drop the low order term, and **3)** is defined as asymptotically. To be specific for **3)**, after the specific value $n_0$, the running time of the algorithm is always between two functions $c_1 \cdot L(n)$ and $c_2 \cdot L(n)$.

##### Big-$\Omega$ (Omega) Notation

Big-$\Omega$ notation describes the lower bound of the complexity of an algorithm, without providing an upper bound. In other words, the notation refers to the best case of the complexity. Likewise **Big-O Notation**, the notation **1)** drop the constant, **2)** drop the low order term, and **3)** is defined as asymptotically.

#### B. Array - Data Structure

Typically, *Array* refers to fixed in size data structure that stores elements of the same data type. While the strengths of arrays are that **1)** they are fast to access their elements, **2)** they are fast to append elements to the end of the array, the weakness are that **1)** they are fixed in size and **2)** they have cost to insert or delete elements. $\text{Table 1}$ shows the time complexity in the worst case of each operation.

$$
\text{Table 1. Time Complexity of Array Data Structure} \\
\begin{array}{|c|c|c|c|c|c|c|}
\hline
& \text{lookup} & \text{append} & \text{insert} & \text{delete} & \text{extend} & \text{slice} \\
\hline
\text{Worst Case} & O(1) & O(1) & O(n) & O(n) & O(n) & O(n) \\
\hline
\end{array}
$$

*Insert* is a operation that inserts an element at a specific index in the array so that everything starting at that index is shifted to the right. Therefore, the worst case of the operation becomes $O(n)$ in the beginning of the array. *Delete* needs to shift all elements to the left after the element is deleted. In other words, the worst case of the operation is $O(n)$ when the targeted element is the beginning of the array. *Extend* is a operation that appends all elements of another array to the end of the targeted array. The time complexity of the operation is $O(n)$ since the operation requires to copy all elements of the other array to the targeted array. Specifically, $n$, in the *Extend* operation, is the number of elements in the other array. *Slice* is a operation that returns a subarray of the targeted array. The algorithm of the opreation is **1)** to create a new array, **2)** to copy targeted elements to the new array. The time complexity of the operation is $O(n)$ because the operation entails to copy all elements of the subarray. To be specific, $n$, in the *Slice* operation, is the number of elements in the subarray.

*In-Place Algorithms* refer to algorithms that do not require extra space to store the result of the algorithm. In other words, they do not copy the input array during its operation so that the access to the original array is not guranteed after the end of the algorithms. The algorithms are efficient in terms of space complexity. However, sometimes the algorithms are inefficient in terms of time complexity.

#### C. Dynamic Array

*Dynamic Array* is a data structure that is similar to *Array* but it is not fixed in size. Three strengths, **1)** fast to access elements, **2)** flexible in size, and **3)** friendly to be cached, and two weaknesses, **1)** slow at the worst case of append operation and **2)** more cost to insert and delete elements. $\text{Table 2}$ shows the time complexity in both the average case and the worst case of each operation.

$$
\text{Table 2. Time Complexity of Dynamic Array Data Structure} \\
\begin{array}{|c|c|c|c|c|c|c|}
\hline
& \text{lookup} & \text{append} & \text{insert} & \text{delete} \\
\hline
\text{Average Case} & O(1) & O(1) & O(n) & O(n) \\
\hline
\text{Worst Case} & O(1) & O(n) & O(n) & O(n) \\
\hline
\end{array}
$$

#### D. Searching Algorithms

What *Searching Algorithms* conduct is to find a target $x$, and return its index if the target were in arrays or databases, or return False if not. **Linear Search** is the simplest algorithm to search the target, suitable for short lists. **Binary Search** needs to be conducted on a sorted list, and it is faster than the linear search. The algorithm is the popular algorithm for large databases with records sorted by numerical values. Pseudo code of the algorithms is shown below.

``` Python
def binary_serach(list, min, max, key):
    while min <= max:
        mid = (min + max) // 2

        if list[mid] > key:
            max = mid - 1
        elif list[mid] < key:
            min = mid + 1
        else:
            return mid

    return False
```

With the step of Binary Search, the time complexity of the algorithm $O(\log{n})$ is derived. The algorithm is efficient in terms of time complexity, but it requires the list to be sorted. The algorithm is not suitable for the unsorted list.


### References

$\tag*{}\label{1} \text{[1] Formal Definition of Big O Notation, Youtube Video, https://www.youtube.com/watch?v=T8_x0yhON-4, accessed in Aug. 25, 2024}$
$\tag*{}\label{2} \text{[2] Paul E. Black, "big-O notation", in Dictionary of Algorithms and Data Structures [online], Paul E. Black, ed. 6 September 2019. (accessed in Aug. 25, 2024) Available from: https://www.nist.gov/dads/HTML/bigOnotation.html}$

### Appendix

##### Logarithms

$\cdot \text{ Simplification : } \log_{b}{b^x} = x$ \
$\cdot \text{ Multiplication : } \log_{b}{(x \cdot y)} = \log_{b}{x} + \log_{b}{y}$ \
$\cdot \text{ Division : } \log_{b}{\left(\frac{x}{y}\right)} = \log_{b}{x} - \log_{b}{y}$ \
$\cdot \text{ Power : } \log_{b}{x^y} = y \cdot \log_{b}{x}$ \
$\cdot \text{ Change of Base : } \log_{b}{x} = \frac{\log_{c}{x}}{\log_{c}{b}}$

#### Practices

1. Find the largest value, when a list of numbers is given
    1. Define a variable `largest` and compare the variable to all elements in the list ($O(n)$)
    2. Sort the given list and return the first or last element ($O(n \log{n})$)
2. Find the second largest value, when a list of numbers is given
    1. Use variables `largest` and `second_largest` and compare the variables to all elements in the list ($O(n)$)
3. 32 teams are in the list. In order to find a particular team, how many times do you need to compare the teams in the worst case?
    6?
