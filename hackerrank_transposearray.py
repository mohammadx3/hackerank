import numpy as np

val = input().split(' ')
val1 = int(val[0])
val2 = int(val[1])
i = 0
array = []
while i < val1 :
    array.append(list(input().split(' ')))
    i += 1
array = [list(map(int,x)) for x in array]
tran_arr = np.transpose(np.array(array))
flatten_arr = tran_arr.flatten()

print(tran_arr)
print(flatten_arr)
