import math


# points
points = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]


def euclidianDistance(x, y):
    
    x1, y1 = x
    x2, y2 = y
    
    result = math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))
    return result


distances = []

for i in range (len(points)):
    for j in range(i + 1, len(points)):
        distance = euclidianDistance(points[i],points[j])
        distances.append(distance)
        
        
#min distance

minDistance = min(distances)

print("Minimum distance:", minDistance)
