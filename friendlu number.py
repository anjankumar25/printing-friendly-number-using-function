def frd(a,b):
    v=0 
    c=0
    
    for i in range(1,a):
        if a % i==0:
             v=v+i
    
    for j in range(1,b):
        if b%j==0:
            c=c+j
    

    if v*b == c*a:
        print(f"{a} and{b}is friendly number")
    else:
        print("not a friendly numbers")
frd(a=6,b=28)