f = open('input.txt', 'r')
li = [i for i in f]



points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

def determine_output(opp, me):
    guide = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}
    #do we draw?
    if guide[opp] == guide[me]: return 3
    #do we win?
    if guide[me] == "paper" and guide[opp] == "rock": return 6
    if guide[me] == "rock" and guide[opp] == "scissors": return 6
    if guide[me] == "scissors" and guide[opp] == "paper": return 6

    return 0


def sol_one(input_list):
    acc = 0
    for rnd in input_list:
        opp, me = rnd.strip().split(' ')
        result = determine_output(opp, me)
        acc += points[me] + result
        # rnd = "A Y"
    return acc

output = sol_one(li)
print(output)

def determine_shape(opp, result):
    guide = {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scis
    "X": "l",
    "Y": "d",
    "Z": "w"
    }
    # what do we do when its a draw?
    if guide[result] == "d": return guide[opp]
    if guide[result] == "w":
        if opp == "A": return guide["B"]
        if opp == "B": return guide["C"]
        if opp == "C": return guide["A"]
    if guide[result] == "l":
        if opp == "A": return guide["C"]
        if opp == "B": return guide["A"]
        if opp == "C": return guide["B"]

def sol_two(input_list):
    result_key = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    acc = 0
    for rnd in input_list:
        opp, res = rnd.strip().split(' ')
        result = determine_shape(opp, res)
        acc += result_key[res] + result
    return acc

output = sol_two(li)
print(output)