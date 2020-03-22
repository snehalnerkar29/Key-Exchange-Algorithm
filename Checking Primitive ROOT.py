def checkPrimitiveRoot(N,R):
    alist=dict.fromkeys(range(N), False)
    #loop through values from 0 to N-2 
    for i in range(N-1):
        temp=pow(R,i,N)
        if alist[temp]==False:
            alist[temp]=not alist[temp]
        else:
#             print("NOT ROOT at ",i)
            return False
    return True
checkPrimitiveRoot(11,3)
False
checkPrimitiveRoot(11,2)
True
C. Generate all primitive Roots
def findRoot(N):
    collectRoots=[]
    #Try out all possible values between 1 to N-1
    for i in range(1,N,1):
        if checkPrimitiveRoot(N,i):
            print("{} is the Primitive Root module  {}".format(i,N))
            collectRoots.append(i)
            
#     print("NO ROOT Exists ")
    return collectRoots
findRoot(11)
2 is the Primitive Root module  11
6 is the Primitive Root module  11
7 is the Primitive Root module  11
8 is the Primitive Root module  11
D. Generate Discrete Logarithm Table

#works only when g is Primitive ROOT OF G
def generateDiscreteLogTable(N,g):
    collectRoots=findRoot(N)
    if g not in collectRoots:
        print(" {} not Root of {}".format(g,N))
        return 
    table=dict.fromkeys(range(1,N),0)
    for i in range(N-1):
        temp=pow(g,i,N)
        table[temp]=i
       
    print("TABLE FOR DISCRETE LOGARITHM OF {} under module {}".format(g,N))
    print("N\tLog(g)[N]")
    for k,v in table.items():
        print("{}\t{}".format(k,v))
        
generateDiscreteLogTable(11,2)
2 is the Primitive Root module  11
6 is the Primitive Root module  11
7 is the Primitive Root module  11
8 is the Primitive Root module  11
TABLE FOR DISCRETE LOGARITHM OF 2 under module 11
N	Log(g)[N]
1	0
2	1
3	8
4	2
5	4
6	9
7	7
8	3
9	6
10	5
