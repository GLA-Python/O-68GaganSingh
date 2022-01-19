n = list(map(int, input("Write space separated values").split()))
n1=[]
# print(n, len(n))
for i in range(len(n)-1):
    k=n[i+1]-n[i]
    n1.append(abs(k))
# print(n1)
for j in range(len(n1)-1):
    l=n1[j+1]-n1[j]
    if l<0:
        print("False")
        break
else:
    print("True")
