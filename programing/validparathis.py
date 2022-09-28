'''
    this code only second order multiplication only working...
''''

p='()(())(())()(())'
a=[]
b=''

for q in range(len(p)):
    if p[q]=='(':
        a.append(p[q])
    else:
        if not a:
            pass
        elif p[q]==')' and a[len(a)-1]=='(' and a[len(a)-2]=='(' and p[q+1]==')':
            b+=a[len(a)-2]+a[len(a)-1]+p[q]+p[q+1]
            a=[]
        else:
            if p[q]==')' and a[len(a)-1]=='(':
                b+=a[len(a)-1]+p[q]
                a.pop()
print(b)