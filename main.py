from fractions import Fraction

possibilities = list(range(0, 1000))

primes = list(map(int, input("Enter primes (separated by space): ").split()))

for p in primes:
    guess = possibilities[0]
    if len(possibilities) == 1:
        print("Answer:", guess)
        break
    print("Guess:", guess)
    dist = Fraction(input(f'Enter {p}-adic distance: '))
    if dist == 0:
        break
    possibilities = list(filter(lambda x: (x - guess) % (1 / dist) == 0 and (x - guess) * dist % p != 0, possibilities))