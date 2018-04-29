import numpy as np

def extract():
    f = open('Competition_train_cnt.txt', 'r')
    li = []
    count = 0
    X = []
    for line in f:
        if count == 64:
            li.append(X)
            X = []
            count = 0

        vals = line[:-1].strip(" ").split(" ")
        row = []
        for v in vals:
            if v == " " or v == '':
                continue
            else:
                row.append(float(v))
        X.append(row)
        count += 1
    li.append(X)

    print(np.array(li).shape)
    return li