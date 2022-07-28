N=7
ballcount=3
# user='Y'
user='N'
bricktype=' '
wallposition=[]
groundposition=[]
ballposition=[]
brickposition=['221','231','241']
ballout=0
middle=round(N/2)



# while(user=='Y'):
#     brickpositioninput=input('Enter the brick\'s position and the brick type :')
#     brickposition.append(brickpositioninput)
#     user=input('Do you want to continue(Y or N)?')
    
def bricks(x,y):
    global bricktype
    r=False
    for z in range(len(brickposition)):
        temp=brickposition[z]
        tempx=temp[0]
        tempy=temp[1]
        temptype=temp[2:len(temp)]
        if str(x)==tempx and str(y)==tempy:
            bricktype=temptype
            r=True
            break
    return r
def structure():
    global user
    if user=='N':    
        for Y in range(N):
            for X in range(N):
                if X==0 or Y==0 or X==N-1 or (X==N-1 and Y==N-1):
                    temp1=[]
                    temp1.append(X)
                    temp1.append(Y)
                    wallposition.append(temp1)
                    print('W', end=' ')
                elif Y==N-1 and X!=0 and X!=N-1 and (Y==N-1 and X!=middle-1):
                    temp2=[]
                    temp2.append(X)
                    temp2.append(Y)
                    groundposition.append(temp2)
                    print('G',end=' ')
                elif Y==N-1 and X==middle-1:
                    ballposition.append(X)
                    ballposition.append(Y)
                    print('o',end=' ')
                elif bricks(X,Y):
                    print(bricktype,end=' ')
                else:
                    print(' ',end=' ')
            print()
        print('Ball Count:',ballcount)

# while(ballout==1):
structure()
