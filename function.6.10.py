#(Find the isPrime number with function)
def is_prime (num):
    if num < 2 :
        return False
    for n in range(2 ,int(num**0.5)+1):
        if num % n == 0 :
            return False
    return True  # number is prime

def find_primes_num(numberOfPrimes) :
    primes = []
    for n in range(2 , numberOfPrimes) :
        if is_prime (n):
            primes.append(n)
    return primes

primes_less_than_1000 = find_primes_num(1000)
print(f"Prime numbers less than 10000: \n {primes_less_than_1000 }")
