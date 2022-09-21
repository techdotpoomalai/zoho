array=[1,2,4,6,8,10]
d=[]
c=0
temp=[]
for x in array:
    for y in range(1, x+1):
        if x%y==0:
            c+=1
    d.append(c)
    c=0
    
r_d=d[::-1]
r_array=array[::-1]
for a in range(1,max(d)+1):
    for z in range(len(r_d)):
        if a==r_d[z]:
            print(str(r_array[z])+" divisier is "+str(r_d[z]))
