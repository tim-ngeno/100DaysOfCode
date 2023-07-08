"""Check for prime numbers"""


def prime_checker(number):
    """Calculate whether a number is prime or not"""
    if number <= 1:
        print("{} is not prime".format(number))
    else:
        for i in range(2, number):
            if (number % i) == 0:
                print("{} is not prime".format(number))
                break
        else:
            print("{} is prime".format(number))


while True:
    n = int(input("Type a number to check:  "))
    prime_checker(number=n)
#
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
#
#
# n = int(input("Type a number to check:  "))
# prime_checker(number=n)
