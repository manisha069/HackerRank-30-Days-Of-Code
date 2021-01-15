# Enter your code here. Read input from STDIN. Print output to STDOUT


d1, m1, y1=map(int, input().split())
d2, m2, y2= map(int, input().split()) 
fine=0
if y1>y2:
    fine=10000
else:
    if m1>m2:
        fine=500*(m1-m2)
    else:
        if d1>d2:
            fine=15*(d1-d2)
if d1<=d2 and m1<=m2 and y1<=y2:
    fine=0
if y1<y2:
    fine=0
print(fine)
