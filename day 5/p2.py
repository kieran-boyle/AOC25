import os
import json

def build_ranges(ranges):
    new_data = []
    
    for each_range in ranges:
        each_range = each_range.split('-')
        new_data.append([int(each_range[0]), int(each_range[1])])

    return new_data

with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    ranges = data[0]
    ranges = build_ranges(ranges)
    acc = []
    
    for each_range in ranges:
        
        for i in range(each_range[0], each_range[1] + 1):
            
            if i not in acc:
                acc.append(i)

    print(acc)
    #numbers get too big, will need to think of a different solution.