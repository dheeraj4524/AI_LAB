def TowersOfHanoi(n,from_rod,to_rod,a_rod):
    if n==1:
        print("Move disk 1 from rod ",from_rod," to rod",to_rod)
        printS(n,from_rod,to_rod,a_rod)
        return
    TowersOfHanoi(n-1,from_rod,a_rod,to_rod)
    print("Move disk ",n," from rod ",from_rod," to rod ",to_rod)
    printS(n,from_rod,to_rod,a_rod)
    TowersOfHanoi(n-1,a_rod,to_rod,from_rod)
def printS(n,from_rod,to_rod,a_rod):
    if(from_rod=='A'):
        if(to_rod=='B'):
            B.append(n)
            A.remove(n)
        elif(to_rod=='C'):
            C.append(n)
            A.remove(n)
    elif(from_rod=='B'):
        if(to_rod=='A'):
            A.append(n)
            B.remove(n)
        elif(to_rod=='C'):
            C.append(n)
            B.remove(n)
    elif(from_rod=='C'):
        if(to_rod=='A'):
            A.append(n)
            C.remove(n)
        elif(to_rod=='B'):
            B.append(n)
            C.remove(n)
    print("A: ",A,"B: ",B,"C: ",C)
print("Towers of Hanoi")
n=int(input("Enter no. of disks:"))
A=list(range(n,0,-1))
B=[]
C=[]
print("Initial state A: ",A,"B: ",B,"C: ",C)
TowersOfHanoi(n,'A','C','B')
print("Goal state A: ",A,"B: ",B,"C: ",C)