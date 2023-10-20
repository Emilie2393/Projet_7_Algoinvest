max_cost = 500
actions = [[20, 5], [30, 10], [50, 15], [70, 20], [60, 17], [80, 25],
           [22, 7], [26, 11], [48, 13], [34, 27], [42, 17],
           [110, 9], [38, 23], [14, 1], [18, 3], [8, 8], [4, 12],
           [10, 14], [24, 21], [114, 18]]

# create a table with 501 columns (max_cost) and 21 rows (actions length)
table = [[0 for i in range(max_cost + 1)] for i in range(len(actions) + 1)]

for action in range(1, len(actions) + 1):
    for cost in range(1, max_cost + 1):
        if actions[action-1][0] <= cost:
            table[action][cost] = max(round((actions[action-1][0] * actions[action-1][1]/100) + table[action-1][cost-actions[action-1][0]], 2), table[action-1][cost])
            # cumul des gains si la capacité ne depassent pas 500
        else:
            table[action][cost] = table[action-1][cost]
            # non cumul
print(table)


indice = len(actions)
selection = []

while max_cost >= 0 and indice >= 0:
    e = actions[indice-1]
    print(e)
    print(table[indice][max_cost])
    print(table[indice-1][max_cost-e[0]] + (e[0]*e[1]/100))
    if table[indice][max_cost] == round(table[indice-1][max_cost-e[0]] + (e[0]*e[1]/100), 2):
        selection.append(e)
        max_cost -= e[0]
    indice-=1

print(table[-1][-1], selection)
    

