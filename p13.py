with open('p13.txt', 'r') as file:
    tall = file.readlines()
#tall = [int(tall) for tall in tall]

'''
a = 0
for i in tall
    a += int(i[-10:])
    #a = int(str(a)[-10:])
print(a)
'''

a = 0
for i in tall:
    a += int(i)
print(a)
