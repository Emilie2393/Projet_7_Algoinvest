from itertools import combinations
import time

actions = [[20, 5], [30, 10], [50, 15], [70, 20], [60, 17], [80, 25],
           [22, 7], [26, 11], [48, 13], [34, 27], [42, 17],
           [110, 9], [38, 23], [14, 1], [18, 3], [8, 8], [4, 12],
           [10, 14], [24, 21], [114, 18]]

maximum_cost = 0
top_gain = 0
top_combinaison = []
profit_list = []

start = time.time()

for i in range(len(actions)):
    # combination of i * number of action in actions list 
    comb = combinations(actions, i)
    # for each comparation 
    for combinaison in list(comb):
        # for each action in each combination 
        for action in combinaison:
            # while maximum cost of each action is for now inferior at 500
            # and action cost is not superior of current maximum_cost
            if maximum_cost <= 500 and action[0] <= 500-maximum_cost:
                # cumulate action cost to previous actions cost
                maximum_cost += action[0]
                # add action profit to previous profit list
                profit_list.append(action[0] * action[1] / 100)
            else:
                break
        # compare actual profit list with previous best gain
        if sum(profit_list) > top_gain:
            top_gain = sum(profit_list)
            top_combinaison = combinaison
        # init variables for next combination 
        maximum_cost = 0
        profit_list = []

print(top_combinaison, top_gain)
end = time.time()
print(end - start)

