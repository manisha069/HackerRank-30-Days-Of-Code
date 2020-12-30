# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
while t>0:
    t -=1
    ss=input()
    x=""
    y=""
    for i in range(len(ss)):
        if(i%2==0):
            x += ss[i]
        else:
            y += ss[i]
    print(x, y, end=" ")
    print()
