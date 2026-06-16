def is_prime(n: int):
    
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


def all_primes(n: int):
    primes = []
    
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
            
    return primes