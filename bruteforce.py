from itertools import combinations
import time

class ForceBrute:
    def __init__(self, data, max_cost):
        self.data = data
        self.max_cost = max_cost
     
    def calculate(self):
        current_cost = 0
        top_gain = 0
        top_combinaison = []
        current_profit = []

        start = time.time()

        for i in range(len(self.data)):
            # combination of i * number of action in actions list 
            comb = combinations(self.data, i)
            # for each comparation 
            for combinaison in list(comb):
                # for each action in each combination 
                for action in combinaison:
                    # while maximum cost of each action is inferior at 500
                    # and action cost is not superior of current current_cost
                    if current_cost <= self.max_cost and action[0] <= self.max_cost-current_cost:
                        # cumulate action cost to previous actions cost
                        current_cost += action[0]
                        # add action profit to previous profit list
                        current_profit.append(action[0] * action[1] / 100)
                    else:
                        break
                # compare actual profit list with previous best gain
                if sum(current_profit) > top_gain:
                    top_gain = sum(current_profit)
                    top_combinaison = combinaison
                # init variables for next combination 
                current_cost = 0
                current_profit = []

        print("Brut force - La meilleure rentabilité est: ", round(top_gain, 2)," pour les actions suivantes: \n", top_combinaison)
        end = time.time()
        print(end - start)