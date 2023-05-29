def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    numero = number
    a = 1
    while True:
        a = a + 1
        if numero == 1:
            return False
        elif numero <= 0:
            return False
        elif numero % a == 0 and a != numero:
            return False
        elif a == numero:
            return True

def list_prime_factors(number: int) -> list[int]:
    """Retorna uma lista com os fatores primos de cada número da lista fornecida."""
    prime_factors = []
    for i in range(2, number + 1):
        if is_prime(i):
            while number % i == 0:
                prime_factors.append(i)
                number //= i

    return prime_factors
