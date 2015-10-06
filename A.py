f=open('input.txt')
N=int(f.readline())
massiv=f.readline().split()
for i in range(len(massiv)):
     if massiv.count(massiv[i])==2:
      x=massiv[i] 
      break
f=open('output.txt')
print(x, file=f)
f.close()
