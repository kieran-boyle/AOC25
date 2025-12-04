import os
import json

with open(os.path.join(os.path.dirname(__file__), 'input.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    count = 0
    
    for each_range in data.split(','):
        start, end = each_range.split('-')
        start = int(start)
        end = int(end)
        
        for i in range(start, end + 1):            
        
            if len(str(i)) % 2 == 0:
                mid = len(str(i)) // 2
                left = str(i)[:mid]
                right = str(i)[mid:]
                
                if left == right:
                    count += i
    
    print(count)