from itertools import combinations
import time
import sys

actions = [[1, 20, 5], [2, 30, 10], [3, 50, 15], [4, 70, 20], [5, 60, 17], [6, 80, 25],
        [7, 22, 7], [8, 26, 11], [9, 48, 13], [10, 34, 27], [11, 42, 17],
        [12, 110, 9], [13, 38, 23], [14, 14, 1], [15, 18, 3], [16, 8, 8], [17, 4, 12],
        [18, 10, 14], [19, 24, 21], [20, 114, 18]]
max_cost = 500
for action in actions:
    action[2] = action[1] * action[2] / 100

current_cost = 0
top_gain = 0
top_combinaison = []
current_profit = []
top_cost = 0
before = sys.getallocatedblocks()
start = time.time()

for i in range(len(actions)):
    # combination of i * number of action in actions list 
    comb = combinations(actions, i)
    # for each comparation 
    for combinaison in list(comb):
        # for each action in each combination 
        for action in combinaison:
            # if action cost is not superior of max_cost with
            # cumulate action's cost in current_cost
            if action[1] <= max_cost-current_cost:
                # cumulate action cost to previous actions cost
                current_cost += action[1]
                # add action profit to previous profit list
                current_profit.append(action[2])
            else:
                break
        # compare actual profit list with previous best gain
        if sum(current_profit) > top_gain:
            top_gain = sum(current_profit)
            top_combinaison = combinaison
            top_cost = current_cost
        # init variables for next combination 
        current_cost = 0
        current_profit = []

print("Brut force - La meilleure rentabilité est:", round(top_gain, 2),"€ pour un cout de", top_cost, "€ pour les actions suivantes: \n", top_combinaison)
end = time.time()
print("Le temps d'execution est de", round(end - start, 3), "secondes")
diff = sys.getallocatedblocks() - before
print(diff, "blocs mémoires supplémentaires ajoutés")