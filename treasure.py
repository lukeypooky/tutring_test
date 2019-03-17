number = int(raw_input())

temp = raw_input()
a = temp.split(' ')

for i in range(len(a)):
    a[i] = int(a[i])

temp = raw_input()

b = temp.split(' ')
for i in range(len(b)):
    b[i] = int(b[i])

for i in range(len(a)):

    for j in range(len(a) -1 ):

        if(a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]

for i in range(len(a)):

    for j in range(len(a) -1 ):

        if(b[j] < b[j+1]):
            b[j],b[j+1] = b[j+1],b[j]

total = 0
for i in range(len(a)):
    total = total + (a[i] * b[i])

print(total)