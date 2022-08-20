
import random

#rnd function gives us random positions out of the empty positions(in human form).
def rnd(l):
    list1 = []
    
    for m in range(3):
        for n in range(3):
            if l[m][n]==' _ ':
                list1.append([m,n])
                

    r = random.choice(list1)
    a,b=r[0],r[1]
    
    return a+1,b+1

#Puts O in the position given (arguments in comp form)
def puto(i,j,l):
    l[i][j]=' O '

#Puts space in the position given (arguments in comp form)
def pute(i,j,l):
    l[i][j]=' _ '
#Puts X in the position given (arguments in comp form)            
def putx(i,j,l):
    l[i][j]=' X '
                
# Prints the game board
def pgame(l):
    for m in range(3):
        for n in range(3):
            print(l[m][n], end=' ')
        print()

#row+1 and col+1 because 0 == False
def trio_check(l,k):
    #hori
    for m in range(3):
        count=0
        
        for n in l[m]:    
            if(n==k):
                count+=1 
                
        if(count==3):
            return True
            

    #vertical check
    for m in range(3):
        c=0
        for n in range(3):
            if l[n][m] == k:
                c+=1
        if c == 3:
            return True           
            

    #diagonal check 1
    c=0
    for m in range(3):
        if l[m][m] == k:
            c+=1
        if c == 3:
            return True

    #diagonal check 2
    c=0
    for m in range(3):
        
        n=2-m
        if l[m][n] == k:
            c+=1
        if c == 3:  
            return True            
    
    return False

#prints a horizontal line to seprate the boards
def hr():
    print()
    for x in range(10):
        print('*',end=' ')
    print()
    print()

#Check if the given index is empty
def ifempty(m,n,l):
    if l[m][n]==' _ ':
        return True
    else:
        return False

def UserInput(game):
    i=int(input('enter row[1,2,3] = '))
    j=int(input('enter col[1,2,3] = '))
    if(ifempty(i-1,j-1,game)):
        puto(i-1,j-1,game)
        return 0
    else:
        print('invalid position!!')
        i=int(input('enter row[0,1,2] = '))
        j=int(input('enter col[0,1,2] = '))
        if(ifempty(i-1,j-1,game)):
            puto(i-1,j-1,game)
            return 0
        else:
            print('Tu mat hi khel bye!!!!')
            return 1
 
def emsp(l):
    list1 = []#list of all the empty positions
    
    for m in range(3):
        for n in range(3):
            if l[m][n]==' _ ':
                list1.append([m,n])

    return list1


def score(g):
    if(trio_check(game,' O ')):
        return -1
    elif(trio_check(game,' X ')):
        return 1
    else:
        return 0




def minmax(game,depth,maxiplay): # -1 0 1
    if score(game)!=0:
        return score(game)

    if maxiplay:
        maxEval = -5
        
        child = emsp(game)
        for ch in child:
            putx(ch[0],ch[1],game)
            e = minmax(game,depth-1,True)
            maxEval = max(maxEval,e)
            pute(ch[0],ch[1],game)
        return maxEval

    else:
        minEval = 5
        child = emsp(game)
        for ch in child:
            puto(ch[0],ch[1],game)
            e = minmax(game,depth-1,False)
            minEval = min(minEval,e)
            pute(ch[0],ch[1],game)
        return minEval




def bestMove(game):
    list1 = emsp(game) #list of all the empty positions
    bestScore = -5

    for posi in list1:
        game[posi[0]][posi[1]]=' X '
        evalu = minmax(game,3,False)
        game[posi[0]][posi[1]]=' _ '
        if evalu > bestScore:
            bestScore = evalu
            r = posi

    return r[0],r[1]



                
#game ahead

game= [[' _ ',' _ ',' _ '],
       [' _ ',' _ ',' _ '],
       [' _ ',' _ ',' _ ']]
pgame(game)
    
t=9
while(True):
    if score(game) == 1:
        hr()
        print ('You lost')
        break
    if score(game) == -1:
        hr()
        print ('You Won')
        break
    if(t==0):
        hr()
        print("It's a Draw here")
        break
    hr()

    #user input
    if UserInput(game):
        print('hao bhaiya bye!!')
        break

    pgame(game)
    t=-1

    if score(game) == 1:
        hr()
        print ('You lost')
        break
    if score(game) == -1:
        hr()
        print ('You Won')
        break
    if(t==0):
        hr()
        print("It's a Draw here")
        break
    hr()


    #our input
    a,b=bestMove(game)
    #a,b=rnd(game)
    #a-=1
    #b-=1
    putx(a,b,game)

    hr()
    pgame(game)
    t=-1


