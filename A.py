N=int(input())
massiv=input().split()
for i in range(len(massiv)):
     if massiv.count(massiv[i])==2:
       print(massiv[i])
       break
