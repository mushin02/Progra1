
def is_prime(num):
    if num <=1:
        return False
    for n in range(2, num):
        if num % n ==0:
            return False
    return True


def main():
    numbers_string = input('add your numbers: ')
    your_numbers= [int(n.strip()) for n in numbers_string.split(",")]
    primes = [num for num in your_numbers if is_prime(num)]
    print(f'Prime numbers: {primes}')

main()    