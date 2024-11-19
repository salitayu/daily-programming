def findMinArrow(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    first_end = points[0][1]
    results = 1
    for x_start, x_end in points:
        if first_end < x_start:
            results += 1
            first_end = x_end
    return results