import math

import numpy as np
import random

if __name__ == '__main__':
    # Point noir : choix entre deux colonnes => distance avec le deuxième choix ?

    matrix = np.random.randint(100, size=(5, 5))
    print(matrix)

    candidates = dict()
    answer = list()

    for j in range(len(matrix[0])):
        candidates[j] = list()

        for i in range(len(matrix)):
            if matrix[i][j] == 0:
                candidates[j].append(i)


    def sorter(item):
        return len(item[1])


    remaining = [i for i in range(len(candidates))]
    for i in range(len(candidates)):
        if len(candidates[i]) == 0:
            min = np.min(matrix[:, i])

            for j in range(len(candidates)):
                if matrix[j][i] == min:
                    candidates[i].append((j))

    for i in range(len(candidates)):
        item = sorted(candidates.items(), key=sorter)[0]
        print(candidates)

        column = item[0]
        line = item[1][0]
        answer.append((line, column))

        # Remove the column
        candidates.pop(column, None)

        # Remove the line
        remaining.remove(line)
        for c in candidates.items():
            try:
                 c[1].remove(line)
            except ValueError:
                pass

            if len(c[1]) == 0:
                minimum = math.inf
                to_add = list()
                for l in remaining:
                    if matrix[l][column] < minimum:
                        to_add = list()
                        to_add.append(l)
                    elif matrix[l][column] == minimum:
                        to_add.append(l)
                candidates[c[0]] = to_add

    answer.sort()

    print("Réponse : ", answer)
    cost = 0
    for coo in answer:
        cost += matrix[coo[0]][coo[1]]
    print("Coût = ", cost)
