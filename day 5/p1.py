import os
import json

def build_ranges(ranges):
    new_data = []
    
    for each_range in ranges:
        each_range = each_range.split('-')
        new_data.append([int(each_range[0]), int(each_range[1])])

    return new_data

def check_range(target, each_range):
    
    if each_range[0] <= target <= each_range[1]:
        
        return True
    
    return False
    
with open(os.path.join(os.path.dirname(__file__), 'input.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    ranges, targets = data[0], data[1]
    ranges = build_ranges(ranges)
    total = 0
    
    for target in targets:
        
        for each_range in ranges:
            
            if check_range(int(target), each_range):
                total += 1
                break
            
    print(total)