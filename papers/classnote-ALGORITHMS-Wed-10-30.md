$$
\begin{array}{|c|c|}
\hline
\text{} & \text{} \\
\hline
\text{} & \text{} \\
\hline
\end{array}
$$

* Geometric Algorithms
    ex. Find the mid-point of a line: Given two coordinates of a line $(x_1, y_1)$ and $(x_2, y_2)$. we want to find the mid-point of them on the line connecting these two points.
        A. $( \frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2} )$
    ex. Check if a given point lies inside or outside a triangle: Given three coordinate of a triangle $(10, 30), (0,0), (20,0)$ and a point $p$, check if $p$ is inside or outside of triangle.
        A. Find the area of triangle $APB, BPC, CPA$ and compare it with the area of triangle $ABC$. If the sum of the area of the three triangles is equal to the area of triangle $ABC$, then the point $p$ is inside the triangle $ABC$. Otherwise, it is outside of the triangle $ABC$.
    ex. Count the maximum points on the same line: Given $n$ coordinate on a 2D plane. We need to find the maximum number of points which lie on the same line.
        A. 두 점을 가지고 slope 값을 찾아서 나머지 점들과 slope 값을 비교한다. 한 점으로부터 다른 점과의 비교이기 때문에 slope만 있어도 충분하다
    ex. Check if a line passes through origin: given two ccoordinate of a line (x1, y1) (x2, y2)
        A. Find the equation of the line and check if the line passes through the origin or not.
    ex. Check if a given point lies inside a rectangle: Given four coordinate of a rectangle $ABCD$ and a point $P$, check if $P$ lies inside the rectangle $ABCD$.
        A1. Use same approach as triangle.
        A2. Find the x value of P is between the x value of A and C (직사각형, 정사각형일때만 되겠다)

    ex. Check if given 4 points form a square: Given four coordinate of a square $(10, 20), (20,20), (10,10), (20, 10)$, check if the four points form a square or not.
        A. pick one point and calculate the distance of this point from the other three points. If two of these values are equal and the third value is $\sqrt{2}$ times the other two values, then the four points form a square.
        And then, pick the farthest point from the first point and calculate the same things as above. The result should be the same as the first calculation. (이 점이 반대편에 있을 수도 있기 때문에)

    ex. check if two circle touch or intersect each other: Given two circles A and B with the center coordinates $(x_1, y_1)$ and $(x_2, y_2)$ and radius $r_1$ and $r_2$ respectively.
        A. Find the distance between the two centers. if the distance is less than the sum of the radius, then the two circles intersect each other. If same, touch and if greater, no intersection.
    ex. Find the minimum radius such that at leas $k$ points lie inside the circle: Given an integer k, a circle center $(0, 0)$ and $n$ points on a 2D plane.
        A. Calculate distances of all points from the origin and sort them. The $k^{th}$ distance will be the minimum radius of the circle. (or median of medians in k-th smallest problem)
    ex. Find simple closed path for a given set of points: given n points, connect them without crossing
        A. Find the bottom most point by finding the minimum y value.
            Consider the remaining $n-1$ points and find their polar angle in counterclockwise direction order with regard to 1st point.
            Traverse the sorted array yields the simple closed path.
    ex. Closest pair of point in the plane: Given an array of n points and the problem is to find the closest pair in array
        A1. Brute force: compare all points and find the minimum distance (O(n^2))
        A2. Sort the array according to x-coordinate. With the middle point (array[n/2]), divide the array into two halves. Recursively find the minimum distance in both subarrays. ... (https://www.geeksforgeeks.org/closest-pair-of-points-onlogn-implementation/)
    ex. Optimum location of point to minimize total distance: Given a set of points and a line $ax + by + c = 0$, we need to find a point on this line such that the sum of distances from given set of points is minimized.
        A. 선 위의 점으로 방정식을 구하면, u-curve가 나온다 (2차함수). Ternary search를 이용하여 최소값을 찾는다.
            * Ternary Search
                - Start with the `low` and `high` initialized as some smallest and largest values respectively.
                - Loop that calculates two mids which `mid1` refers to the value of 1/3rd of the range and `mid2` refers to the value of 2/3rd of the range.
                - Calculate total distance of all points with respect to mid1 and mid2 and update low and high by comparing these distance cost
                - iteration continues until low and high become apprixmately equal

    ex. Polygon and convex hull: How to check if a given point lies inside or outside of a polygon: Given a polygon and a point p, check if p lies inside or outside the polygon.
        (위의 삼,사각형 approach는 적용하기 힘들다)
        A. Draw a horizontal line to the right of each point and extend it to infinity. Count the number of times the line intersects with polygon edges. A point is inside the polygon if either count of intersections is odd or point lies on an edge of the polygon. If none of the conditions is true, then the point is outside the polygon.
            polygon의 꼭짓점과 닿는 선은 밖에 있음에도 홀수번 닿으므로, we should return true if point lies on the line or same as one of vertices of given polygon. To handle this edge case, we check if $P$ is collinear with vertices of polygon. If it is collinear, then we check if P lies on current side of polygon. If yes True, no False.

    ex. Tangents, between two convex polygon: Given two convex polygons we need to find the lower and upper tangent.
        A. Find the leftmost point of the polygon A and rightmost point of the polygon B. leftmost점에서 B 의 점들을 옮겨가며, polygon을 통과하지 않는 점을 찾는다. 찾은 점에서 다시 A의 점들을 옮겨가며 polygon을 통과하지 않는 점을 찾는다. 이 두 점이 lower tangent이다. upper tangent도 같은 방법으로 찾는다.
        ``` plaintext
        def upper_tangent(A, B):
            L = a line joining the rightmost point of A and the leftmost point of B

            while L passes through any polygon:
                while L passes through polygon B:
                    L = L' (the point of B moves up)
                while L passes through polygon A:
                    L = L' (the point of A moves up)
            return L

        def lower_tangent(A, B):
            L = a line joining the rightmost point of A and the leftmost point of B

            while L passes through any polygon:
                while L passes through polygon B:
                    L = L' (the point of B moves down)
                while L passes through polygon A:
                    L = L' (the point of A moves down)

            return L
        ```

    ex. Find the number of diagonal in $n$ sided polygon: Given $n \geq 3$, find the number of diagnols in $n$ sided polygon.
        A. $n(n-3)/2$: n개에 대해 자기자신과 바로 옆의 점을 제외하고, 나머지 점들과 연결하면 대각선이 된다. 그리고 순서는 상관없으므로 2로 나눈다.

    * Convex hall - Jarvis' Algorithm
    ex. Given $n$ points, find the smallest convex polygon that contains all the points.
        A. Jarvis' Algorithm
            1. Find the leftmost point and start from there.
            2. Repeat the following bullets until the leftmost point is reached again.
                a) next point q is the point such that the triplet p,q,r is counterclockwise for any other point r.
                    r에 대해 q가 clockwise가 아니면, counterclockwise이다.
                b) next[p] = q
                c) p = q (to move to the next point)
    * Convex hall - Graham's Scan (추가 공부 필요 ㅎㅎ,, 대충 세 개점만 비교해서 clockwise면 버리고, 아니면 넘어가는 방식)
    ex. Given $n$ points, find the smallest convex polygon that contains all the points.
        A. Graham's Scan
            1. Find the bottom most point by comparing y values or all points. if there are two poitns with same y value, point with smaller x value. Let this point be $p_0$.
            2. Consider remaining $n-1$ points and sort them by polar angle in counterclockwise direction with regard to $p_0$. If more than one point has the same angle, put the nearest point first.
            3. After sorting, if two or more points have same angle, remove all except the farthest point from $p_0$.
            4. Process the remaining points one by one and keep removing points from the stack while the orientation of 3 points is not counterclockwise.

        The above algorithm can be divided into 2 parts:
            1) Sort points and find simple closed path
            2) accept or reject points to form convex hull

            Keep tracking the orientation of the last three points pre(p), cur(c), next(n), if orientation of these nodes is not counterclockwise, then discard the current node, otherwise keep the current node.

    ex. Interior and exterior angle of a regular polygon: Given $n$ of sides(n각형), task is to find interior and exterior angle of a regular polygon.
        A. exterior angle = 360/n, interior angle = 180 - exterior angle





### References

$\tag*{}\label{n} \text{[n] }$
