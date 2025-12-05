import os
import json

def find_joltage(bank):
    bank = [int(x) for x in bank]
    first_highest = 0
    first_index = 0
    second_highest = 0
    
    for i, battery in enumerate(bank):
        
        if i == len(bank) - 1:
            break
        
        if battery > first_highest:
            first_highest = battery
            first_index = i

    for i, battery in enumerate(bank):
            
            if i <= first_index:
                continue
            
            if battery > second_highest:
                second_highest = battery

    return int(f'{first_highest}{second_highest}')

    
with open(os.path.join(os.path.dirname(__file__), 'input.json'), 'r', encoding='utf-8') as f:
    battery_array = json.load(f)
    total_output_joltage = 0
    
    for bank in battery_array:
        total_output_joltage += find_joltage(bank)
    
    print(f'Total Output Joltage: {total_output_joltage}')