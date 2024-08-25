#

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

#### I. Introduction

#### II. Literature Review

**Big O Notation**

*Big O Notation* represents how long an algorithm takes time to run, enabling to predict the performance as the input gets arbitrarily large. The rules of *Big O Notation* are that **1)** drop the constant (ex. $O(1 + {n \over 2} + 100 \to O(n)$), **2)** drop less significant terms (ex. $O(n + n^2) \to O(n^2)$), and **3)** usually talks about the worst case. $Fig 1.$ is the comparison of the complexity among all types of *Big O Notation*.

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


#### References

$\tag*{}\label{1} \text{[1] Formal Definition of Big O Notation, Youtube Video, https://www.youtube.com/watch?v=T8_x0yhON-4, accessed in Aug. 25, 2024}$
$\tag*{}\label{2} \text{[2] Paul E. Black, "big-O notation", in Dictionary of Algorithms and Data Structures [online], Paul E. Black, ed. 6 September 2019. (accessed in Aug. 25, 2024) Available from: https://www.nist.gov/dads/HTML/bigOnotation.html}$
