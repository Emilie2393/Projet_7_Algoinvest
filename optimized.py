import time

class Knapsack():
    def __init__(self, data, max_cost):
        self.data = data
        self.max_cost = max_cost
    
    def calculate(self):
        start = time.time()
        # create a table with 501 columns (max_cost) and 21 rows (actions length)
        table = [[0 for i in range(self.max_cost + 1)] for i in range(len(self.data) + 1)]

        for action in range(1, len(self.data) + 1):
            for cost in range(1, self.max_cost + 1):
                # if action's cost is less than current cost range
                if self.data[action-1][0] <= cost:
                    # set best result between current action and previous action results for the same cost limitation 
                    table[action][cost] = max(round((self.data[action-1][0] * self.data[action-1][1]/100) + 
                                                     table[action-1][cost-self.data[action-1][0]], 2), table[action-1][cost])
                else:
                    # set previous action profit
                    table[action][cost] = table[action-1][cost]

        indice = len(self.data)
        selection = []

        while self.max_cost >= 0 and indice >= 0:
            e = self.data[indice-1]
            # if absolute result of self.max_cost - previous action cost is more than self.data and table length
            # prevent an error which occurs when self.max_cost is lower than current action cost
            if abs(self.max_cost-e[0]) > len(self.data) and abs(self.max_cost-e[0]) > len(table[0]):
                indice-=1
            else:
                # compare best result of current action with previous action results - current action cost + his profit,
                # if results fits, it meens that this action is responsible for the best result 
                # table[indice][self.max_cost] : current action will be saved
                if table[indice][self.max_cost] == round(table[indice-1][self.max_cost-e[0]] + (e[0]*e[1]/100), 2):
                    selection.append(e)
                    self.max_cost -= e[0]
                indice-=1

        print("Knapsack - La meilleure rentabilité est:", table[-1][-1]," pour les actions suivantes: \n", selection)

        end = time.time()
        print(end - start)
    

