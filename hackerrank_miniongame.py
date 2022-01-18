import numpy as np
f = open('input_minion.txt','r+')
a = f.read()
x = str(a)
v = 'a e i o u A E I O U'.split(' ')
kevin,stuart = 0,0
for i,n in enumerate(x):
    if n in v:
        kevin += len(x)-i
    else:
        stuart += len(x)-i

if (stuart)<(kevin):
        print(f'Kevin {(kevin)}')
elif (stuart)>(kevin):
        print(f'Stuart {(stuart)}')
else: print('Draw')
f.close()


