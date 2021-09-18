
from typing import Collection


test = [6, 4, 3, 5, 9, 15, 11, 8, 16, 13, 7, 2, 1, 10, 14, 12]

gaps = [701, 301, 132, 57, 23, 10, 4, 1]

def shell(test):
    for gap in gaps:
        for i in range(gap, len(test)):
            insert_value = test[i]
            j = i
            while j >= gap and test[j -gap] > insert_value:
                test[j] = test[j - gap]
                j -= gap
            if j != i:
                test[j] = insert_value
    return test

print(shell(test))

