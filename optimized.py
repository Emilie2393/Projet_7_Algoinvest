import csv
from bruteforce import calculate
import time

start = time.time()
actions = []
with open('dataset1_Python+P7.csv', newline='') as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        row[1] = float(row[1])
        row[2] = float(row[2])
        if row[1] <= 0:
            print(row[1])
            continue
        else:
            actions.append(row)

for action in actions:
    action.append(round(float(action[2]) / float(action[1]), 3))

calculate(actions)
end = time.time()

print(end-start)