import time
import csv
import sys

actions = []
file = open("dataset2_Python+P7.csv")
reader = csv.reader(file)
next(reader)
for row in reader:
    if float(row[1]) > 0:
        row[1], row[2] = int(float(row[1]) * 100), round((float(row[1]) * float(row[2]) / 100),3)
        actions.append(row)

max_cost = 50000
before = sys.getallocatedblocks()
start = time.time()
# create a table with 501 columns (max_cost) and 21 rows (actions length)
table = [[0 for i in range(max_cost + 1)] for i in range(len(actions) + 1)]

for action in range(1, len(actions) + 1):
    for cost in range(1, max_cost + 1):
        # if action's cost is less than current cost range
        if actions[action-1][1] <= cost:
            # set best result between current action and previous action results for the same cost limitation 
            table[action][cost] = max(round(actions[action-1][2] + table[action-1][cost-actions[action-1][1]], 2), 
                                        table[action-1][cost])
        else:
            # set previous action profit
            table[action][cost] = table[action-1][cost]

indice = len(actions)
selection = []
total_cost = []
while max_cost >= 0 and indice >= 0:
    e = actions[indice-1]
    # if absolute result of max_cost - previous action cost is more than actions and table length
    # prevent an error which occurs when max_cost is lower than current action cost
    if abs(max_cost-e[1]) > len(actions) and abs(max_cost-e[1]) > len(table[0]):
        indice-=1
    else:
        # compare best result of current action with previous action results - current action cost + his profit,
        # if results fits, it meens that this action is responsible for the best result 
        # table[indice][max_cost] : current action will be saved
        if table[indice][max_cost] == round(table[indice-1][max_cost-e[1]] + e[2], 2):
            selection.append(e[0])
            max_cost -= e[1]
            total_cost.append(e[1])
        indice-=1

print("Knapsack - La meilleure rentabilité est:", table[-1][-1],"€ pour un cout de", sum(total_cost)/100, "€ pour les actions suivantes: \n", selection)
end = time.time()
print("Le temps d'execution est de", round(end - start, 3), "secondes")
diff = sys.getallocatedblocks() - before
print(diff, "blocs mémoires supplémentaires ajoutés")

