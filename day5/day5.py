import re 

f = open('input.txt', 'r')
li = [i for i in f]

def get_crates(inp):
    crates = []
    for i in inp:
        if i == '\n': 
            break
        crates.append(i)
    return list(reversed(crates))

def remove_whitespace(letter):
    return letter != ' '

def parse_dict(li):
    d = {}
    crates = get_crates(li)
    towers = [i for i in list(zip(*crates))]
    for col in towers:
        try:
            if int(col[0]) in range(1,10):
                d[int(col[0])] = list(filter(remove_whitespace,[v for i, v in enumerate(col) if i != 0]))
        except:
            continue
    return d

def parse_instructions(li):
    instructions = []
    index = 0
    start_parsing = False
    while index < len(li):
        if start_parsing:
            instruction = li[index].strip()
            move, frm, to = re.findall(r'\d+', instruction)
            instructions.append({"move": int(move), "from": int(frm), "to": int(to)})
        if li[index] == '\n':
            start_parsing = True
        index += 1
    return instructions


def solution_one(input_list):
    crate_heaps = parse_dict(input_list)
    instructions = parse_instructions(input_list)
    for instruction in instructions:
        idx = instruction['move']
        for i in range(0, idx):
            x = crate_heaps[instruction['from']].pop()
            crate_heaps[instruction['to']].append(x)
    return(''.join([crate_heaps[k][-1:][0] for k, v in crate_heaps.items()]))

print(solution_one(li))


def solution_two(input_list):
    crate_heaps = parse_dict(input_list)
    instructions = parse_instructions(input_list)
    for instruction in instructions:
        idx = instruction['move']
        moving_crates = []
        for i in range(0, idx):
            x = crate_heaps[instruction['from']].pop()
            moving_crates.append(x)
        crate_heaps[instruction['to']].extend(list(reversed(moving_crates)))
    return(''.join([crate_heaps[k][-1:][0] for k, v in crate_heaps.items()]))

print(solution_two(li))

