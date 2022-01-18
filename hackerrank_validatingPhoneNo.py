N = int(input())
phoneNo = []
for _ in range(N):
    no = str(input())
    phoneNo.append(no)
for i in phoneNo:
    if i[0] in ('7','8','9') and len(i)==10 and i.isnumeric():
        print('Yes')
    else: print('No')