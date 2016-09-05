from is_prime import is_prime

i = 1
p = 1
while i <= 10001:
    if is_prime(p):
        
        i += 1
    p += 1

print(p-1)


    
