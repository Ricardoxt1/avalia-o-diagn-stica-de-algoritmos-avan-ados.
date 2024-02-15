def numeroPerfeiro(numeroPerfeiro):
    divisores = 0
    for i in range(1, numeroPerfeiro):
        if numeroPerfeiro % i == 0:
            divisores += i
    if divisores == numeroPerfeiro:
        return numeroPerfeiro
    else:
        return 'Não é um número perfeito.'
    
print(numeroPerfeiro(6))
