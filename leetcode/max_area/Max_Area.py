import math

def max_area(heights):
    maxArea = 0

    for i in range(len(heights)):
        for j in range(i+1,len(heights)):
            height = min(heights[i], heights[j])
            width = j - i
            area = height * width

            maxArea = max(area, maxArea)

    return maxArea

def max_area_optimal(heights):
    p1 = 0
    p2 = len(heights) - 1
    maxArea = 0

    while p1 < p2:
        height = min(heights[p1] , heights[p2])
        width = p2 - p1
        area = width * height
        maxArea = max(maxArea, area)
        if heights[p1] < heights[p2]:
            p1 = p1 + 1
        else:
            p2 = p2 - 1
    return maxArea



heights = [7,1,2,3,9]
# heights = [5]
print(max_area_optimal(heights))