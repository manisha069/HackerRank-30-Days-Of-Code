# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
no=dict()
for i in range(n):
    x=input().split()
    no[x[0]]=x[1]
while True:
    try:
        name = input()
        if name in no:
            y=name+"="+no[name]
            print(y)
        else:
            print('Not found')
    except:
        break
