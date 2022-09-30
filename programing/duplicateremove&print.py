'''
    This code was every single character remove and print each same character removing but space character is excepted case....

'''

split_list=[]
remove_position=[]
remove_subposition=[]
remove_inter=[]
s='hellow world i am comming...'
s1=[]
is_print=False

# print(len(remove_position) != 0)

def cheack_repeat(x, xx):
    result=True
    for y in x:
        for yy in y:
            if yy==xx:
                result=False
    return result
    

for x in s:
    split_list.append(x)
for y in range(len(split_list)):
    for z in range(y+1, len(split_list)):
        if split_list[y]==split_list[z] and split_list[y] !=' ':
            if len(remove_position)==0:
                remove_subposition.append(z)
            else:
                if cheack_repeat(remove_position, z):
                    remove_subposition.append(z)
        
    if remove_subposition:
        remove_position.append(remove_subposition)
        remove_subposition=[]

for a in remove_position:
    for b in a:
        remove_inter.append(b)
        s1=split_list.copy()
    for c in remove_inter:
        s1[c]=''
    final_temp=''
    for final in s1:
        if final=='':
            is_print=True
            continue
        else:
            final_temp +=final
        s1=[]
    if is_print:
        print(final_temp)
        is_print=False

# print("****************************************************")

    
  
         
