from dataclasses import dataclass


@dataclass
class Point:
    """
    Point class for convenient work with coordinates
    """
    x: int
    y: int

    # The magic method of subtraction
    def __sub__(self, point2):
        return Point(self.x - point2.x, self.y - point2.y)

    # Calculation of the norm of the vector corresponding to the point
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** .5

    # A magic method for debugging code
    def __repr__(self):
        return f'Point: x={self.x}, y={self.y}'


n = int(input())  # Entering the number of points

points = list()  # Array of points on the plane
connects = [True] + [False] * (n + 1)  # An array of point states is attached or not
ans = [1]  # Answer
ans_amount = 0  # Number of points involved
current_point_index = 0  # index of the current point

# Filling the list with data
for _ in range(n + 2):
    points.append(Point(*map(int, input().split())))

while ans_amount < n + 1:
    max_distance = 0
    p1 = points[current_point_index]  # Current point

    for i, p2 in enumerate(points):
        if connects[i] or i == current_point_index:
            continue

        distance = (p2 - p1).norm()  # Calculating the distance between points

        # Finding the maximum distance
        if distance > max_distance:
            max_distance = distance
            current_point_index = i

    ans.append(current_point_index + 1)
    connects[current_point_index] = True
    ans_amount += 1

print("YES")
print(*ans)
