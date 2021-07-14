n = int(input(""))
a=[]
b={}
for k in range(0,n):
    j=int(input(""))
    a.append(k)
print (a)

for i in range(1,len(a)):
    count = 0
    for j in a:
        if j%i==0:
            count = count+1
    b.update({i:count})
print(b)
