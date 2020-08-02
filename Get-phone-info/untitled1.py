
#li=lambda :list(map(int,input().split()))
"""inp2 = lambda : map(int,input().split())
a,b=inp2()"""
"""inp1= lambda : int(input())
g=inp1()
print(g)
#print(a,b)"""
"""mii = lambda: map(int, input().split())
n, p = mii()
print(n,p)"""
"""fo =lambda :range(int(input()))
k=fo()"""
"""pt=lambda x : print("".join(x))
f=pt(['1','2','3','4'])
inp2 = lambda : map(int,input().split())
a,b=inp2()"""
"""c=1
l=[1,2,3,5,7,11,13,17,19]
for _ in l:
    c*=_
print(c)"""
"""_, k = (int(x) for x in input().split())

import sys
print(sum((1 for n in map(int, sys.stdin) if not n % k)))"""
"""s=input()
c,l=0,""
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        f=s[i:j]
        if len(f)>c and f==f[::-1]:
            l=f
            c=len(f)
#print(c,l)
print('{} {}'.format(c,l))"""
"""
s="ab.c.'r"
s=s.replace('\'','')
print(s)"""
#a=input().lower().split()
"""d={'1':1,'2':2}
p=d.keys()
d=print(*p)"""
"""
from itertools import combinations
c=combinations(range(0,5),2)
for k,v in list(c):
    #f=(l[k]+l[v])//2
    #if d[f]:
    print(k,v)
print(list(c))"""
"""li=lambda :list(map(int,input().split()))
a=li()"""
"""import string
alp = list(string.ascii_lowercase)
print(alp)
f=list(string.ascii_letters)"""
# cook your dish here
"""t=int(input())
for _  in range(t):
    s=input().strip('0')
    print(s)
"""    
#This is The Coding Area
"""t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    while n>=1:
    	n//=2
    	c+=1
    print(c)"""
    
    
"""
from math import sqrt
from itertools import permutations
def is_prime(n):
    c = int(sqrt(n)//1)
    for i in range(2,c + 1):
        if n % i == 0:
            return False
            break
    else:
        return True

a,b=map(int,input().split())
l=[]
for i in range(a,b):
    if is_prime(i):
        l.append(str(i))
#print(l)
s=[]
comb = permutations(l, 2) 
for k,v in list(comb):
    s.append(int(str(k)+str(v)))
#print(s)
s=sorted(set(s))
#print(len(s))
l2=[]
for i in s:
    if is_prime(i):
        l2.append(i)
#print(l2)
#print(len(l2))
#print(min(l2),max(l2))
m=min(l2)
ma=max(l2)
def fib(n,m,ma): 
  
    # array declaration 
    f = [0]*(n+1) 
  
    # base case assignment 
    f[0]=m
    f[1] =ma
  
    # calculating the fibonacci and storing the values 
    for i in range(2 , n+1): 
        f[i] = f[i-1] + f[i-2] 
    for i in f:
        print(i)
    return f[n-1] 
print(fib(len(l2),m,ma))"""

