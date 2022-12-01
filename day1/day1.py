f = open('input.txt', 'r')

l = [i for i in f]

highest_cals = 0
acc = 0 
elves = []

for idx in range(len(l)):
    if l[idx] == '\n':
        elves.append(acc)
        highest_cals = max(highest_cals, acc)
        acc = 0
        continue
    acc = acc + int(l[idx])

print(highest_cals)

sorted_elves = sorted(elves)
sum_of_top_three = sum(sorted_elves[-3:])
print(sum_of_top_three)
