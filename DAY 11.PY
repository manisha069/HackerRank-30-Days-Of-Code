ls=[]
for i in range(6):
    x=list(map(int, input().split()))
    ls.append(x)

total=[]
for i in range(4):
    for j in range(4):
        sum=0
        sum=sum+ls[i][j]+ls[i][j+1]+ ls[i][j+2]
        sum=sum+ls[i+1][j+1]
        sum=sum+ls[i+2][j]+ls[i+2][j+1]+ls[i+2][j+2]
        total.append(sum)
print(max(total))
