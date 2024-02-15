# sequência de fibionacci

def serieFibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return serieFibonacci(n-1) + serieFibonacci(n-2)
    

print(serieFibonacci(4))
    
    