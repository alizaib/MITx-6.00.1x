def prime_generator():
    primes = []
    next_prime = 2

    while True:
        yield next_prime        
        primes.append(next_prime)
        n = next_prime

        while True:
            next_prime += 1
            is_prime = True

            for p in primes:
                if next_prime % p == 0:
                    is_prime = False
                    break

            if is_prime:                
                break


generator = prime_generator();
for i in range(15):
    print(generator.__next__())
        
