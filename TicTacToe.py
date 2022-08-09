# import random
import random

def rnd(l):
    list1 = []
    
    for m in range(3):
        for n in range(3):
            if l[m][n]==' _ ':
                list1.append([m,n])
                

    r = random.choice(list1)
    a,b=r[0],r[1]
    
    return a+1,b+1

def puto(i,j,l):
    for m in range(3):
        for n in range(3):
            if m==i and n==j:
                l[m][n]=' O '
                
def putx(i,j,l):
    for m in range(3):
        for n in range(3):
            if m==i and n==j:
                l[m][n]=' X '
                
def pgame(l):
    for m in range(3):
        for n in range(3):
            print(l[m][n], end=' ')
        print()

#row+1 and col+1 because 0 == False

def duo_check_hor(l,k):
    #horizontal check
    for m in range(3):
        count=0
        
        for n in l[m]:    
            if(n==k):
                count+=1 
                
        if(count==2):
            row=m
            break
        else:
            count=0

    if (count==2):
        col=0
        f=0
        for m in l[row]:
            
            if(m==' _ '):
                f=1
                break
            col+=1
            
        if f==1:        
            return row+1,col+1
    else: 
        return False
    
def duo_check_ver(l,k):    
    #vertical check
    for m in range(3):
        c=0
        for n in range(3):
            if l[n][m] == k:
                c+=1
        if c == 2:
            col=m            
            break
        else:
            c=0
    row=0
    if c == 2:
        f=0
        for m in range(3):
            
            if(l[m][col]==' _ '):
                f=1
                row=m
                break
            
        if f==1:        
            return row+1,col+1
    else:
        return False

def duo_check_dig(l,k):    
    #diagonal check
    for m in range(3):
        c=0
        if l[m][m] == k:
            c+=1
        if c == 2:          
            break
        
            

    if c == 2:
        for m in range(3):
            f=0
            
            if(l[m][col]==' _ '):
                f=1
                row=m
                col=m
                break
        if f==1:        
            return row+1,col+1

    #diagonal check 2

    for m in range(3):
        c=0
        n=2-m
        if l[m][n] == k:
            c+=1
        if c == 2:          
            break
        
    
    if c == 2:
        f=0
        for m in range(3):
            
            n=2-m
            if(l[m][n]==' _ '):
                f=1
                row=m
                col=n
                break
        if f==1:        
            return row+1,col+1
    else:
        return False
    
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
    for m in range(3):
        c=0
        if l[m][m] == k:
            c+=1
        if c == 3:
            return True          
            break

    #diagonal check 2
    for m in range(3):
        c=0
        n=2-m
        if l[m][n] == k:
            c+=1
        if c == 3:  
            return True        
            
        else:
            return False

def hr():
    print()
    for x in range(10):
        print('*',end=' ')
    print()
    print()

def duo_o(g):

    if(duo_check_hor(g,' O ')):
        a,b=duo_check_hor(g,' O ')
        return a,b

    elif(duo_check_ver(g,' O ')):
        a,b=duo_check_ver(g,' O ')
        return a,b

    elif(duo_check_dig(g,' O ')):
        a,b=duo_check_dig(g,' O ')
        return a,b

    else: 
        return False

def duo_x(g):

    if(duo_check_hor(g,' X ')):
        a,b=duo_check_hor(g,' X ')
        return a,b

    elif(duo_check_ver(g,' X ')):
        a,b=duo_check_ver(g,' X ')
        return a,b

    elif(duo_check_dig(g,' X ')):
        a,b=duo_check_dig(g,' X ')
        return a,b

    else: 
        return False

def victory(g):
    if(trio_check(game,' O ')):
        hr()
        print('You Won')
        return False
    elif(trio_check(game,' X ')):
        hr()
        print('You Lost')
        return False
    else:
        return True

def ifempty(m,n,l):
    if l[m][n]==' _ ':
        return True
    else:
        return False



game= [[' _ ',' _ ',' _ '],
       [' _ ',' _ ',' _ '],
       [' _ ',' _ ',' _ ']]
pgame(game)
    
t=9
while(victory(game) and t):
    
    hr()
    #user input
    i=int(input('enter row[1,2,3] = '))
    j=int(input('enter col[1,2,3] = '))
    if(ifempty(i-1,j-1,game)):
        puto(i-1,j-1,game)
    else:
        print('invalid position!!')
        i=int(input('enter row[0,1,2] = '))
        j=int(input('enter col[0,1,2] = '))
        if(ifempty(i-1,j-1,game)):
            puto(i-1,j-1,game)
        else:
            print('Tu mat hi khel bye!!!!')
            break

    pgame(game)
    t-=1
    if(t==0):
        hr()
        print("It's a Draw")
        break
    
    #our input
    

    if(duo_x(game)):
        a,b=duo_x(game)
        if(ifempty(a-1,b-1,game)):
            putx(a-1,b-1,game)
        else:
            a,b=rnd(game)
            putx(a-1,b-1,game)
            
    elif(duo_o(game)):
        a,b=duo_o(game)
        print(a,b)
        if(ifempty(a-1,b-1,game)):
            putx(a-1,b-1,game)
        else:
            a,b=rnd(game)
            putx(a-1,b-1,game)

    else:
        a,b=rnd(game)
        putx(a-1,b-1,game)

    hr()
    pgame(game)
    t-=1
