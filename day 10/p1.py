import os
import json

def parse_input(data):
    results = []
    
    for line in data:
        this_data = []
        split_line = f'{line}'.split(' ')
        diagran = list(map(lambda x: 0 if x == '.' else 1, split_line[0]))
        this_data.append(diagran)
        buttons = split_line[1:-2]
        
        for i, button in enumerate(buttons):
            button = button.replace('(', '').replace(')', '').split(',')
            buttons[i] = list(map(int, button))
            
        this_data.append(buttons)
        requirements = list(map(int, split_line[-1][:-2].replace('{', '').replace('}', '').replace('"','').split(',')))
        this_data.append(requirements)
        results.append(this_data)
    
    return results
        
with open(os.path.join(os.path.dirname(__file__), 'test.json'), 'r', encoding='utf-8') as f:
    data = parse_input(json.load(f))
    
    for line in data:
        diagram, buttons, requirements = line
        print(diagram)