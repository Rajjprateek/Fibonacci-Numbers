n=eval(input('enter number'))
f=0
s=1
t=0
print(f,end=' ,')
print(s,end=' ,')
for x in range (1,n):
    t=f+s
    print(t,end=' ,')
    f=s
    s=t
