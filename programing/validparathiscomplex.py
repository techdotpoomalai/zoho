p='(((((((((())))))))))((()))((()))((()))'
a=[]
b=''
# print(p[5:5+3])
def complex(l,n, p):
    temp=''
    temp_=''
    lenth=len(l)
    for g in l:
        temp +=g
        if g=='(':
            temp_+=')'
    if temp!=temp_:
        global b
        b +=temp+temp_
        for v in range(lenth):
            a.pop()
        return True
    else:
        return False

for q in range(len(p)):
    if p[q]=='(':
        a.append(p[q])
    else:
        if not a:
            pass
        elif complex(a,q,p):
            continue
        else:
            if p[q]==')' and a[len(a)-1]=='(':
                b+=a[len(a)-1]+p[q]
                a.pop()
print(b)