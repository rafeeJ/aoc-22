f = open('input.txt', 'r')
li = [i.strip() for i in f]

def parse_pair(pair):
    l_t, r_t = pair.split(',')
    # get largest range.
    s, l = l_t.split('-')
    left_array = [*range(int(s), int(l)+1, 1)]
    
    s, l = r_t.split('-')
    right_array = [*range(int(s), int(l)+1, 1)]  

    return [left_array, right_array]

def check_subarray(larger, smaller):
    large_idx = 0
    small_idx = 0

    while ( large_idx < len(larger) and small_idx < len(smaller)):
        if larger[large_idx] == smaller[small_idx]:
            large_idx += 1
            small_idx += 1
            if small_idx == len(smaller):
                return True
        else:
            large_idx = large_idx - small_idx + 1
            small_idx = 0
    return False

def check_subarray_pythonic(larger, smaller):
    try:
        idx = larger.index(smaller[0]) 
        new_large = larger[idx:]
        if len(new_large) >= len(smaller):
            return True
        else: return False
    except ValueError:
        return False

def solution_one(input_list):
    acc = 0
    for pair in input_list:
        left, right = parse_pair(pair)
        if len(left) > len(right):
            if check_subarray_pythonic(left, right): acc +=1
        if len(right) > len(left):
            if check_subarray_pythonic(right, left): acc +=1
        else:
            if right == left: acc +=1
    return acc

output = solution_one(li)
print(output)

def solution_two(input_list):
    acc = 0
    for pair in input_list:
        left, right = parse_pair(pair)
        if set(left) & set(right):
            acc +=1
    return acc

output = solution_two(li)
print(output)