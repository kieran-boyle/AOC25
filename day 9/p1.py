import os
import json

with open(os.path.join(os.path.dirname(__file__), 'input.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    areas = [] 
    
    for point1 in range(len(data)):
        
        for point2 in range(point1 + 1, len(data)):
            p1 = data[point1]
            p2 = data[point2]
            size = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)
            areas.append(size)
            
    print(max(areas))
