import re
import email.utils as eu

n= int(input())
data = []
for _ in range(n):
    x,y = input().split()
    data.append(eu.formataddr((x,y.replace('<','').replace('>',''))))
sp = re.compile('[!#$%^&*()<>?/\|}{~:]')
em = re.compile('\\b^[a-zA-Z]+[A-Za-z0-9._%+-]+@[a-zA-Z]+\\.[A-Z|a-z]{1,3}\\b')
for i in data:
    if sp.search(eu.parseaddr(i)[1]) is None and em.match(eu.parseaddr(i)[1]) is not None:
        print(i)



