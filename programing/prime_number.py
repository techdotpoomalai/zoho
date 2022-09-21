N=0
count=0
prime_number=[]
userinput=int(input("Enter your input :"))
if userinput<1000:
    N=userinput
else:
    N=1000

for test in range(2, N):
    for is_prime in range(1,test):
        if test % is_prime==0:
            count +=1
    if count==1:
        prime_number.append(test)
    count=0

print(prime_number)
