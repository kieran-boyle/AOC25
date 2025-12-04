import json

dial = range(100)
count = 0
position = 50

def parse_move(move):
    direction = move[0]
    steps = int(move[1:])
    return direction, steps

def move_dial(direction, steps):
    global position
    global count
    
    if steps <= 0:
        return
    
    if direction == 'L':
        position = (position - steps) % len(dial)
        
    elif direction == 'R':
        position = (position + steps) % len(dial)
    
    if position == 0:
        count += 1
    
with open('input.json') as f:
    data = json.load(f)
    
    for move in data:
        direction, steps = parse_move(move)
        move_dial(direction, steps) 

print(count)