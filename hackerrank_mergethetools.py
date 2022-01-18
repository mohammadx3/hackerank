def merge_the_tools(string, k):
    z = list(string)
    f = []
    for i in range(0,len(z),k):
        y = []
        for j in z[i:i+k]:
            if j not in y:
                y.append(j)
        f.append(y)        
    for a in f:
        print(''.join(a))   
    # your code goes here
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)