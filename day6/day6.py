f = open('input.txt', 'r')
li = [i.strip() for i in f]
puzzle_input = li[0]

def check_valid(chars, target):
    arr = list(chars)
    if len(set(arr)) == target:
        return True
    return False

def solution_one(inp):
    idx = 0
    processed = ''
    while idx < len(inp):
        processed += inp[idx]
        idx += 1
        if idx < 4: continue
        if check_valid(processed[-4:], 4):
            return idx

print(solution_one(puzzle_input))

def solution_two(inp):
    idx = 0
    processed = ''
    while idx < len(inp):
        processed += inp[idx]
        idx += 1
        if idx < 14: continue
        if check_valid(processed[-14:], 14):
            return idx

print(solution_two(puzzle_input))

# Below is created after submitting

def general_solution(inp, target):
    idx = 0
    processed = ''
    while idx < len(inp):
        processed += inp[idx]
        idx += 1
        if idx < target: continue
        if check_valid(processed[-target:], target):
            return idx

print(general_solution(puzzle_input, 4))
print(general_solution(puzzle_input, 14))
