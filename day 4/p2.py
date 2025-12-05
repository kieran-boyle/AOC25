import os
import json

def check_neigbours(row, col, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    count = 0
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            
            if grid[r][c] == '@':
                count += 1
                
    return count

with open(os.path.join(os.path.dirname(__file__), 'input.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    total = 0
    last_total = -1
    
    while total != last_total:
        last_total = total
        new_data = [list(row) for row in data]

        for i, row in enumerate(data):
            
            for j, position in enumerate(row):
                
                if position == '@' and check_neigbours(i, j, data) < 4:
                    total += 1
                    new_data[i][j] = '.'
                    
        data = new_data
                   
    print(total)