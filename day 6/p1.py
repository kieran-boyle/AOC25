import os
import json

def parse_input(data):
    new_data = []
    sum_arrays = []
    operands = []
    
    for i, row in enumerate(data):
    
        if i != len(data) - 1:
            nums = list(map(int, row.split()))
            new_data.append(nums)
            
        else:
            operands = row.split()

    length = len(new_data)

    for i, digit in enumerate(new_data[0]):
        this_sum = []
        this_sum.append(operands[i])
        this_sum.append(digit)
         
        for l in range(1, length):
            this_sum.append(new_data[l][i])
            
        sum_arrays.append(this_sum)
        
    return sum_arrays

def compute_sum(arr):
    total = 0
    operand = arr[0]
    
    for i, item in enumerate(arr):
        
        if i == 0:
            continue
        
        if operand == '+':
            total += item
        
        elif operand == '*':
            
            if total == 0:
                total = 1
                
            total *= item

    return total

with open(os.path.join(os.path.dirname(__file__), 'input.json'), 'r', encoding='utf-8') as f:
    data = json.load(f)
    parsed_data = parse_input(data)
    result = 0
    
    for sum in parsed_data:
        result += compute_sum(sum)
        
    print(result)