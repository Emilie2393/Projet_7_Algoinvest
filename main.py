from bruteforce import ForceBrute
from optimized import Knapsack

actions = [[20, 5], [30, 10], [50, 15], [70, 20], [60, 17], [80, 25],
           [22, 7], [26, 11], [48, 13], [34, 27], [42, 17],
           [110, 9], [38, 23], [14, 1], [18, 3], [8, 8], [4, 12],
           [10, 14], [24, 21], [114, 18]]

#brut_force = ForceBrute(actions, 500)
#brut_force.calculate()
knapsack = Knapsack(actions, 500)
knapsack.calculate()