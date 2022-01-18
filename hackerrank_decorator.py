import builtins as bi
def append(val):
    global lst
    lst.append(val)
    pass
def insert(val, loc):
    global lst
    if loc < len(lst) and len(lst) != 0:
        tmp = lst[loc:]
        lst[loc] = val
        del lst[loc+1:]
        lst = lst +tmp
    elif (len(lst)==0 and loc==0) or loc==len(lst):
        lst.append(val) 
        
    pass

def reverse(val):
    global lst
    pass
def sort():
    global lst
    lst.sort()
    pass
def print():
    global lst
    bi.print(lst)
    pass
def pop():
    global lst
    del lst[len(lst)-1]
    pass
def reverse():
    global lst
    lst = lst[::-1]
    pass

if __name__ == '__main__':
    N = int(input())
    commands = ['insert','append','remove','sort','print','pop','reverse']
    inputs = []
    for i in range(N):
        inputs.append(input())    

lst = []
c = 0
while(c<N):
    command = inputs[c].split(' ')
    if len(command)>1:
        val = int(command[1])
    
    if len(command)>2:
        loc = int(command[1])
        val = int(command[2])    
        
    if command[0]=='append':
        append(val)
    
    if command[0]=='print':
        print()
    
    if command[0] == 'insert':
        insert(val,loc)
    
    if command[0] == 'sort':
        sort()

    if command[0] == 'remove':
        lst.remove(val)

    if command[0] == 'pop':
        pop()
    
    if command[0] == 'reverse':
        reverse()
    
    
    c += 1

