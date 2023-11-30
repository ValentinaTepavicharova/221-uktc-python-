n = int(input())
longest_intersections = None

for _ in range(n):
        range1, range2 = input('Enter ranges:').split('-')
        range1 = [int(x) for x in range1.split(', ')]
        range2 = [int(x) for x in range2.split(', ')]

        start = max(range1[0], range2[0])
        end = min(range1[1], range2[1])

        if longest_intersections is None:
                longest_intersections = [start, end]
                continue
        if longest_intersections[1] - longest_intersections[0] + 1 < end - start + 1:
                longest_intersections = [start, end]

print(f"Longest intersections is {list((range(longest_intersections[0], longest_intersections[1] + 1)))} with length ")
