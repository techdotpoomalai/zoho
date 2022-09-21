L='34343444444t6767'
count=1
max_count=0
count_char=''
max_char=''
i=0
n=0
while(i<len(L)):
    i +=1
    start=L[n]
    if i==len(L):
        break
    move=L[i]
    if start==move:
        count +=1
        count_char=start
        n=i
        if max_count<count:
            max_count=count
            # count=count+1
            max_char=count_char*count
    else:
        start=move
        n=i
        if max_count<count:
            max_count=count
            # count=count+1
            max_char=count_char*count
        count=1

       
print(max_char)