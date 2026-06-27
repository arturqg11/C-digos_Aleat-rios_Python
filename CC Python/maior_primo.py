def check_primo(numero):
    
    if numero < 2:
        return False

    divisor = 2

    while divisor < numero:
        
        if numero % divisor == 0:
            return False

        divisor += 1 

    return True

def maior_primo(a):

    while a >= 2:

        if check_primo(a):
            return a

        a -= 1
    
    return None

z = maior_primo(100)
print(z)