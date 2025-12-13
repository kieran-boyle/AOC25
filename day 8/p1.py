import os
import json

def eauclidean_distance(point1, point2):
    
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** 0.5

def find_groups(input):
    groups = []
    
    for distance in input:
        p1, p2 = distance[1]

        if not groups:
            groups.append([p1, p2])
            continue
        
        matching_idxs = [i for i, g in enumerate(groups) if p1 in g or p2 in g]

        if not matching_idxs:
            groups.append([p1, p2])
            
        else:
            merged = []
            
            for i in sorted(matching_idxs):
                
                for pt in groups[i]:
                    
                    if pt not in merged:
                        merged.append(pt)
                        
            if p1 not in merged:
                merged.append(p1)
                
            if p2 not in merged:
                merged.append(p2)

            for i in sorted(matching_idxs, reverse=True):
                del groups[i]

            groups.append(merged)
    
    return groups

with open(os.path.join(os.path.dirname(__file__), 'input.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    points = [(item[0], item[1], item[2]) for item in data]
    distances=[]
    
    for i in range(len(points)):
        
        for j in range(i + 1, len(points)):
            distances.append((eauclidean_distance(points[i], points[j]), (points[i], points[j])))
            
    distances.sort(key=lambda x: x[0])
    groups = find_groups(distances[:1000])
    largest_groups = sorted(groups, key=lambda x: len(x), reverse=True)[:3]
    total = 1
    
    for group in largest_groups:
        total *= len(group)
    
    print(total)