
# inputting array:
a = []
n = 1

for i in range(0,n):
    print('Input',i+1,'number:')
    a.append(int(input()))
# finish inputting array

# counting every number:
'''
b = []
for i in range(0,n):
    b.append(1)
    for j in range(i+1,n):
        print('j=',j)
        if a[j]==a[i] :
            b[i] += 1

# looking for MAX
maxGLOBAL = b[0]
numGLOBAL = a[0]
for i in range(1,n):
    if b[i]>maxGLOBAL:
        maxGLOBAL = b[i]
        numGLOBAL = a[i]
print('Max numb=',numGLOBAL,' it occurs ',maxGLOBAL,' times')
'''

max = a[0]

for i in range(1,n):
    if a[i]>max:
        max=a[i]

print(a)
print('САМОЕ БОЛЬШОЕ ЧИСЛО=', max)