with open('p11_grid.txt', 'r') as file:
    lines = file.readlines()

n = []
for line in lines:
    a = line.split(' ')
    b = []
    for i in a:
        b.append(int(i))
        
    n.append(b)
     

N = 0
for i in range(20):
    for j in range(20):
        horizontal, vertical, diag1, diag2 = 0, 0, 0, 0
        if j < 17:
            horizontal = n[i][j]*n[i][j+1]*n[i][j+2]*n[i][j+3]
        if horizontal > N:
            N = horizontal

        if i < 17:
            vertical = n[i][j]*n[i+1][j]*n[i+2][j]*n[i+3][j]
        if vertical > N:
            N = vertical

        if i < 17 and j < 17:
            diag1 = n[i][j]*n[i+1][j+1]*n[i+2][j+2]*n[i+3][j+3]
        if diag1 > N:
            N = diag1

        if i > 3 and j < 17:
            diag2 = n[i-1][j]*n[i-2][j+1]*n[i-3][j+2]*n[i-4][j+3]
        if diag2 > N:
            N = diag2

print(N)
                
 













        


