
#Narayana Pandita's algorithm to find the next lexicographical permutation

def nextPermutation(a):
    a = list(a)
    k = len(a)-2
    while a[k] > a[k+1]:
        k -= 1
    #print(k)

    i = len(a)-2
    while a[k] > a[i]:
        i -= 1

    ak = a[k]
    a[k] = a[i]
    a[i] = ak
    #print(a)

    '''
    a1 = ''.join(a[:k])
    print(a1)
    a2 = a[k:]
    a2.reverse()
    a2 = ''.join(a2)

    return a1+a2
    '''
    b = a
    for i in range(len(a)):
        if 

print(nextPermutation('012'))
'''
g = '012'
for i in range(9):
    print(g)
    g = nextPermutation(g)
'''      
        
    
