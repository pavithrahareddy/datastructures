def toh(n,s,a,d):
    if(n==1):
        print(s,"->",d)
        return
    toh(n-1,s,d,a)
    print(s,"->",d)
    toh(n-1,a,s,d)

toh(int(input()),'A','B','C')