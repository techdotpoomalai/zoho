'''
Note:
    This is normal python file
    N only odd nuber ,you give use even its affected tha structure in inner wall 
    input string only upper case
    1- is bomb plant input
    2-is bobm doneted input
    moving key assuseval you given
    you enter wrong position of villans and bricks it's not affected the program it's just skip
    print text priority given below
        in this order
    0,0-alphabert starting place - 1st
    alphaberts position          - 2nd
    wall position                - 3rd
    villanposition               - 4th
    brick position               - 5th
    key  position                - 6th
    player position              - 7th
    bomb position                - 8th
    empty space                  - finally

'''


user=[]
key=[]
N=int(input('Map size:'))
user_input=input('Player position:')
# user=['FC']
user.append(user_input)
user_key=input('Key position:')
key.append(user_key)
# key=['FD']
villan_count=input('Villain count:')
bricks=input('Brick count:')

player_result=0
villan_position_count=0
briks_position_count=0
inner_wall=[]

villan_position=[]
bricks_position=[]

v_pos=[]
brick_pos=[]
bomb_rangees=[]
bomb_position=[]
player_out_or_not=0
player_position_x=0
player_position_y=0
player_move_or_not=0

alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def position(strings):
    position=[]
    axis_position=[]
    for s in strings:
        for x in range(len(alpha)):
            if s[1]==alpha[x]:
                axis_position.append(x+1)
                break
        for y in range(len(alpha)):
            if s[0]==alpha[y]:
                axis_position.append(y+1)
                break
        position.append(axis_position)
        axis_position=[]
    return position

def villan_pos(count):
    # villan_position=['BH', 'DF']
    dummy_v=[]
    for v in range(1, int(count)+1):
        v_pos.append("V"+str(v)+':')
        dummy_v=input(v_pos[v-1])
        villan_position.append(dummy_v)
    return position(villan_position)

def bricks_pos(count):
    # bricks_position=['CD', 'ED', 'FB', 'FF', 'GB', 'HD']
    dummy_b=[]
    for b in range(1, int(count)+1):
        brick_pos.append('B'+str(b)+':')
        dummy_b=input(brick_pos[b-1])
        bricks_position.append(dummy_b)
    return position(bricks_position)
    
v_pos=villan_pos(villan_count)
brick_pos=bricks_pos(bricks)
key_p=position(key)
player=position(user)

def vilan_place_fix(x,y,v_pos):
    global villan_position_count
    villan=v_pos[villan_position_count] 
    if villan[0]==x and villan[1]==y:
        villan_position_count+=1
        if len(v_pos)==villan_position_count:
            villan_position_count=0
        return True
    else:
        return False
          
def briks_place_fix(x,y,b_pos):
    global briks_position_count
    brikes=b_pos[briks_position_count]
    if brikes[0]==x and brikes[1]==y:
        briks_position_count+=1
        if len(brick_pos)==briks_position_count:
            briks_position_count=0
        return True
    else:
        return False
    
# def inner_wall(n):
#     wall=[]
#     temp=[]
#     for y in range(n):
#         for x in range(n):
#             if (x>2 and x<n-1) and (x%2==1 and y%2==1) and (y>2 and y<n-1):
#                 temp.append(x)
#                 temp.append(y)
#                 wall.append(temp)
#                 temp=[]
#     return wall
    
def player_position(x,y,p_p):
    global player_position_x
    global player_position_y  
    if x==player_position_x and y==player_position_y:
        return True
    else:
        return False
    
def bomb_position_set(X,Y,x_p):
    b_P_s=False
    for x in range(len(x_p)):
        if X==x_p[x][0] and Y==x_p[x][1]:
            b_P_s=True
        else:
            b_P_s=False
    return b_P_s

def move(key, N, i_w, b_p):
    
    
    def up(i_w, b_p):
        global player_position_y
        global player_position_x
        temp_y=player_position_y-1
        cheak_inner_wall=True
        cheak_brick_position=True
        for cheak in range(len(i_w)):
            if i_w[cheak][0]==player_position_x and i_w[cheak][1]==temp_y:
                cheak_inner_wall=False
        for cheak in range(len(b_p)):
            if b_p[cheak][0]==player_position_x and b_p[cheak][1]==temp_y:
                cheak_brick_position=False
                
        if player_position_y>2 and cheak_inner_wall and cheak_brick_position:
            player_position_y-=1

    def down(N, i_w, b_p):
        global player_position_y
        global player_position_x
        cheak_inner_wall=True
        cheak_brick_position=True
        temp_y=player_position_y+1
        for cheak in range(len(i_w)):
            if i_w[cheak][0]==player_position_x and i_w[cheak][1]==temp_y:
                cheak_inner_wall=False
        for cheak in range(len(b_p)):
            if b_p[cheak][0]==player_position_x and b_p[cheak][1]==temp_y:
                cheak_brick_position=False
        
        if player_position_y+1 !=N and cheak_inner_wall and cheak_brick_position:
            player_position_y=player_position_y+1

    def right(N,i_w, b_p):
        global player_position_y
        global player_position_x
        temp_x=player_position_x+1
        
        cheak_inner_wall=True
        cheak_brick_position=True
        for cheak in range(len(i_w)):
            if i_w[cheak][0]==temp_x and i_w[cheak][1]==player_position_y:
                cheak_inner_wall=False
        for cheak in range(len(b_p)):
            if b_p[cheak][0]== temp_x and b_p[cheak][1]==player_position_y:
                cheak_brick_position=False
        if player_position_x+1 !=N and cheak_inner_wall and cheak_brick_position:
            player_position_x=player_position_x+1
        
    def left( i_w, b_p):
        global player_position_x
        global player_position_y
        temp_x=player_position_x-1
        cheak_inner_wall=True
        cheak_brick_position=True
        for cheak in range(len(i_w)):
            if i_w[cheak][0]==temp_x and i_w[cheak][1]==player_position_y:
                cheak_inner_wall=False
        for cheak in range(len(b_p)):
            if b_p[cheak][0]== temp_x and b_p[cheak][1]==player_position_y:
                cheak_brick_position=False
        if player_position_x>2 and cheak_inner_wall and cheak_brick_position:
            player_position_x=player_position_x-1

    def upleft(i_w, b_p):
        global player_position_x
        global player_position_y
        temp_x=player_position_x-1
        temp_y=player_position_y-1
        cheak_inner_wall=True
        cheak_brick_position=True
        for cheak in range(len(i_w)):
            if i_w[cheak][0]==temp_x and i_w[cheak][1]==temp_y:
                cheak_inner_wall=False
        for cheak in range(len(b_p)):
            if b_p[cheak][0]==temp_x and b_p[cheak][1]==temp_y:
                cheak_brick_position=False
        if player_position_x>2 and player_position_y>2 and cheak_inner_wall and cheak_brick_position:
            player_position_x=player_position_x-1
            player_position_y=player_position_y-1

    def downleft(N, i_w, b_p):
        global player_position_x
        global player_position_y
        temp_x=player_position_x-1
        temp_y=player_position_y+1
        cheak_inner_wall=True
        cheak_brick_position=True
        for cheak in range(len(i_w)):
            if i_w[cheak][0]==temp_x and i_w[cheak][1]==temp_y:
                cheak_inner_wall=False
        for cheak in range(len(b_p)):
            if b_p[cheak][0]==temp_x and b_p[cheak][1]==temp_y:
                cheak_brick_position=False
        if player_position_x>2 and player_position_y<N-1 and cheak_inner_wall and cheak_brick_position:
            player_position_x=player_position_x-1
            player_position_y=player_position_y+1

    def upright(N, i_w, b_p):
        global player_position_x
        global player_position_y
        temp_x=player_position_x+1
        temp_y=player_position_y-1
        cheak_inner_wall=True
        cheak_brick_position=True
        for cheak in range(len(i_w)):
            if i_w[cheak][0]==temp_x and i_w[cheak][1]==temp_y:
                cheak_inner_wall=False
        for cheak in range(len(b_p)):
            if b_p[cheak][0]==temp_x and b_p[cheak][1]==temp_y:
                cheak_brick_position=False
        if player_position_x<N-1 and player_position_y>2  and cheak_inner_wall and cheak_brick_position:
            player_position_x=player_position_x+1
            player_position_y=player_position_y-1

    def downright(N,i_w, b_p):
        global player_position_x
        global player_position_y
        temp_x=player_position_x+1
        temp_y=player_position_y+1
        cheak_inner_wall=True
        cheak_brick_position=True
        for cheak in range(len(i_w)):
            if i_w[cheak][0]==temp_x and i_w[cheak][1]==temp_y:
                cheak_inner_wall=False
        for cheak in range(len(b_p)):
            if b_p[cheak][0]==temp_x and b_p[cheak][1]==temp_y:
                cheak_brick_position=False
        if player_position_x<N-1 and player_position_y <N-1 and cheak_inner_wall and cheak_brick_position:
            player_position_x=player_position_x+1
            player_position_y=player_position_y+1 

    def plant_bomb():
        global bomb_position
        global bomb_rangees
        temp_position=[]
        bomb_range_up=[]
        bomb_range_down=[]
        bomb_range_left=[]
        bomb_range_right=[]
        
        bomb_range_up.append(player_position_x)
        bomb_range_up.append(player_position_y-1)
        bomb_range_down.append(player_position_x)
        bomb_range_down.append(player_position_y+1)
        bomb_range_left.append(player_position_x-1)
        bomb_range_left.append(player_position_y)
        bomb_range_right.append(player_position_x+1)
        bomb_range_right.append(player_position_y)
        bomb_rangees.append(bomb_range_up)
        bomb_rangees.append(bomb_range_down)
        bomb_rangees.append(bomb_range_left)
        bomb_rangees.append(bomb_range_right)
        
        temp_position.append(player_position_x)
        temp_position.append(player_position_y)
        bomb_position.append(temp_position)
     
    def donate_bomb():
        global brick_pos
        global v_pos
        global bomb_position
        global player_out_or_not
        brick_index=[]
        viilan_index=[]
        global bomb_rangees
        for q in range(len(bomb_rangees)):
            if bomb_rangees[q][0]==player_position_x and  bomb_rangees[q][1]==player_position_y:
                player_out_or_not=1
        if player_out_or_not!=1:
            for bomb in range(len(bomb_rangees)):
                for b in range(len(brick_pos)):
                    if bomb_rangees[bomb]==brick_pos[b]:
                        brick_index.append(brick_pos[b])
                for v in range(len(v_pos)):
                    if bomb_rangees[bomb]==v_pos[v]:
                        viilan_index.append(v)
            for index1 in brick_index:
                brick_pos.remove(index1)
            for index2 in viilan_index:
                v_pos.remove(v_pos[index2])
            bomb_position.pop(0)
            
        
    if key=='W':
        up(i_w, b_p)
        
    if key=='S':
        down(N,i_w, b_p)
    if key=='A':
        left(i_w, b_p)
    if key=='D':
        right(N,i_w, b_p)
    if key=='Q':
        upleft(i_w, b_p)
    if key=='Z':
        downleft(N,i_w, b_p) 
    if key=='E':
        upright(N,i_w, b_p)
    if key=='C':
        downright(N,i_w, b_p)
    if key =='1':
        plant_bomb()
    if key=='2':
        donate_bomb()
        
def cheak_player_out_or_not(v_pos):
    # global player_position_x
    # global player_position_y
    global player_out_or_not
    for cheak in range(len(v_pos)):
        if v_pos[cheak][0]==player_position_x and v_pos[cheak][1]==player_position_y:
            player_out_or_not=1
        
def cheak_key_player_same(key_p):
    global player_position_x
    global player_position_y
    global player_result
    if player_position_x==key_p[0][0] and player_position_y==key_p[0][1]:
        player_result=1




while(player_result != 1 and player_out_or_not != 1):
     
    if player_move_or_not==0:
        player_position_x=player[0][0]
        player_position_y=player[0][1]
        player_move_or_not=1
    
    # innerwall=inner_wall(N)

    for y in range(N+1):
        for x in range(N+1):
            if (x==0 and y==0):
                print(" ",end=' ')
                N=N
            
            elif x==0 and y>0:
                print(alpha[y-1],end=' ')
            elif y==0:    
                print(alpha[x-1], end=' ')
            elif (y==1 or x==1) or (x==N or y==N) or (x%2!=0 and y%2!=0) :
                if (x>2 and x<N-1) and (x%2==1 and y%2==1) and (y>2 and y<N-1):
                    temp_wall=[]
                    temp_wall.append(x)
                    temp_wall.append(y)
                    inner_wall.append(temp_wall)
                print('*',end=' ')
            elif (vilan_place_fix(x, y, v_pos)):
                print('V',end=' ')
            elif (briks_place_fix(x,y,brick_pos)):
                print('B',end=' ')
            elif x==key_p[0][0] and y==key_p[0][1]:
                print('K',end=' ')
            elif player_position(x,y, player):
                print('P',end=' ')
            elif bomb_position_set(x,y,bomb_position):
                print('X',end=' ')
            else:
                print(' ',end=' ')
        print()
    move_key=input('Enter move key:')
    # move_key='2'
    move(move_key, N, inner_wall, brick_pos)
    cheak_player_out_or_not(v_pos)
    cheak_key_player_same(key_p)
if player_out_or_not==1:
    print('PLAYER OUT')
if player_result==1:
    print('PLAYER WIN')