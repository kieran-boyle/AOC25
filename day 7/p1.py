import os
import json

def parse_input(data):
    new_data = []
    
    for row in data:
        new_data.append(list(row))
        
    return new_data
  
with open(os.path.join(os.path.dirname(__file__), 'input.json'), 'r', encoding='utf-8') as f:
    data = parse_input(json.load(f))
    tally = 0
    
    for i, row in enumerate(data):
        
        for j, symbol in enumerate(row):
            
            if data[i - 1][j] in ['|', 'S']:
                
                if symbol == '^':
                    tally += 1
                    data[i][j - 1] = '|'
                    data[i][j + 1] = '|'
                    
                else:
                    data[i][j] = '|'
                        
    print(tally)
            