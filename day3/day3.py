import math
import string

f = open('input.txt', 'r')
li = [i.strip() for i in f]

def parse_rucksack(r):
    length = len(r)
    half = math.floor(length / 2)
    left = r[:half]
    right = r[half:]
    if len(left) + len(right) == length:
        return [left , right]
    else:
        return TabError

def solution_one(input_list):
    acc = 0
    for rucksack in input_list:
        left, right = parse_rucksack(rucksack)
        l_Set = set(left)
        r_Set = set(right)
        intersect = r_Set.intersection(l_Set)
        
        priority = intersect.pop()
        num = string.ascii_letters.index(priority) + 1

        acc += num
    return acc

result = solution_one(li)
print(result)

def chunkify(l, n=3):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def solution_two(input_list):
    groups = list(chunkify(input_list))
    acc = 0
    for g in groups:
        intersect = set(g[0]) & set(g[1]) & set(g[2])
        priority = intersect.pop()
        num = string.ascii_letters.index(priority) + 1
        acc += num
    return acc

result = solution_two(li)
print(result)