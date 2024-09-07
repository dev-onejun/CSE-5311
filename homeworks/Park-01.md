$$
\begin{array}{c}
\huge{\text{Homework #1}} \\
\hline
\text{Wonjun Park} \\
\text{UTA ID: 1002237177} \\
\href{mailto:wxp7177@mavs.uta.edu}{\text{wxp7177@mavs.uta.edu}}
\end{array}
$$

##### 1. You have an array containing integers from 1 to 10 (not in order) but one number is missing (there is 9 numbers in the array ).

a) write a pseudo code to find the missing number (15 points).

$\qquad missing\_number(array)$: \
$\qquad\qquad n = 10$ \
$\qquad\qquad total = n \times (n + 1) / 2$ \
$\qquad$ \
$\qquad\qquad sum = 0$ \
$\qquad\qquad \text{for } i \text{ in array:}$ \
$\qquad\qquad \qquad sum += i$ \
$\qquad\qquad$ \
$\qquad\qquad missing\_number = total - sum$ \
$\qquad\qquad \text{return } missing\_number$

b) what is the worst case run time complexity of your suggested solution (5 points)

$\qquad$ My suggestion has a time complexity of $O(n)$, where $n$ is the number of elements in the `array`. The algorithm requires a single $\qquad$loop to calculate the sum of the elements in the `array`.


##### 2. You are given an array of integers:

a) write a pseudo code to find all pairs of numbers whose sum is equal to a particular number (15 points).

$\qquad find\_pairs(array, target)$: \
$\qquad\qquad array.sort()$ \
$\qquad$ \
$\qquad\qquad left = 0$ \
$\qquad\qquad right = len(array) - 1$ \
$\qquad\qquad pairs = []$ \
$\qquad$ \
$\qquad\qquad \text{while } left < right:$ \
$\qquad\qquad \qquad sum = array[left] + array[right]$ \
$\qquad\qquad \qquad \text{if } sum == target:$ \
$\qquad\qquad \qquad \qquad pairs.append((array[left], array[right]))$ \
$\qquad\qquad \qquad \qquad left += 1$ \
$\qquad\qquad \qquad \qquad right -= 1$ \
$\qquad\qquad \qquad \text{elif } sum < target:$ \
$\qquad\qquad \qquad \qquad left += 1$ \
$\qquad\qquad \qquad \text{else:}$ \
$\qquad\qquad \qquad \qquad right -= 1$ \
$\qquad$ \
$\qquad\qquad \text{return } pairs$

b) what is the worst case run time complexity of your suggested solution (5 points)

$\qquad$ Assume that the sorting algorithm utilized in the `array.sort()` function utilized $O(n \log n)$ time complexity algorithms such as $\qquad$merge sort. The suggested solution has a time complexity of $O(n \log n + n) = O(n \log n)$, where $n$ is the number of elements in $\qquad$the `array`.


##### 3. You are given an array of integers:

a) write a pseudo code to remove duplicates from your array (15 points).

$\qquad remove\_duplicates(array)$: \
$\qquad\qquad n = len(array)$ \
$\qquad\qquad present = [False] * n$ \
$\qquad\qquad unique = []$ \
$\qquad$ \
$\qquad\qquad \text{for } num \text{ in } array:$ \
$\qquad\qquad \qquad \text{if not } present[num]:$ \
$\qquad\qquad \qquad \qquad present[num] = True$ \
$\qquad\qquad \qquad \qquad unique.append(num)$ \
$\qquad$ \
$\qquad\qquad \text{return } unique$

b) what is the worst case run time complexity of your suggested solution (5 points)

$\qquad$ The algorithm has a time complexity of $O(n)$, where $n$ is the number of elements in the `array`. The algorithm requires a single $\qquad$loop to iterate through the elements in the `array` and check whether the element has already presented in the `unique` list with $\qquad$the `present` hash table.

##### 4. you are given 2 sorted arrays:

a) write a pseudo code to find the median of the two sorted arrays (combined in to 1 array) (15 points).

$\qquad find\_median(array1, array2)$: \
$\qquad\qquad array = array1 + array2$ \
$\qquad\qquad array.sort()$ \
$\qquad$ \
$\qquad\qquad n = len(array)$ \
$\qquad\qquad \text{if } n \% 2 == 0:$ \
$\qquad\qquad \qquad median = (array[n // 2 - 1] + array[n // 2]) / 2$ \
$\qquad\qquad \text{else:}$ \
$\qquad\qquad \qquad median = array[n // 2]$ \
$\qquad$ \
$\qquad\qquad \text{return } median$

b) what is the worst case run time complexity of your suggested solution (5 points)

$\qquad$ Assume that the sorting algorithm utilized in the `array.sort()` function utilized $O(n \log n)$ time complexity algorithms such as $\qquad$merge sort. The suggested solution has a time complexity of $O(n \log n)$, where $n$ is the number of elements in the `array` due to $\qquad$the sorting process.

##### 5.  Answer the following questions:

a) When does the worst case of Quick sort happen and what is the worst case run time complexity in terms of big O? (5 points)

$\qquad$ The worst case of Quick sort occurs when the pivot element is the smallest or largest element in the array. The worst case run $\qquad$time complexity of Quick sort is $O(n^2)$, where $n$ is the number of elements in the array.

b) When does the best case of bubble sort happen and what is the best case run time complexity in terms of big O? (5 points)

$\qquad$ The best case of Bubble sort occurs when the array has already been sorted. The best case run time complexity of Bubble sort $\qquad$is $O(n)$, where $n$ is the number of elements in the array.

c) What is the runtime complexity of Insertion sort in all 3 cases? Explain the situation which results in best, average and worst case complexity. (10 points)

$\qquad$ **1)** The best case run time complexity of Insertion sort is $O(n)$, where $n$ is the number of elements in the array. The best case $\qquad\;$occurs when the array is already sorted. **2)** The average case run time complexity of Insertion sort is $O(n^2)$, where $n$ is the $\qquad\quad$&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;number of elements in the array. The average case occurs when the array is randomly shuffled. **3)** The worst case run time $\qquad\quad\;$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;complexity of Insertion sort is $O(n^2)$ as well, where $n$ is the number of elements in the array. The worst case occurs when the $\qquad\;$array is sorted in reverse order.
