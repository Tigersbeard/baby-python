
#a = [1,8,3,10,5]

'''
for x in range (0, 5):
    print(a[x]*a[x])

for x in range (0, 5):
    print(a[x]**2)

for x in range (0, 5):
    b = [a[x]**2, ]

b = [a[x]**2 for x in range (0, 5)]
'''

#b = [i**2 for i in a]
#print(b)

c = []

for i in "ofd":
    for j in "nua":
        for k in "eny":
            c.append(i + j + k)
            
print(c)