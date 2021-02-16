# in the previous program we found the prime factors of a number
# in this we are finding the highest prime factors of all?

def Prime_Factors(N):
    prime_factors = list()
    divisor = 2 # starting from the least prime number which divides itself
    while(divisor <= N):
        if N % divisor == 0:
            prime_factors.append(divisor)
            N = N / divisor
        else:
            divisor = divisor + 1
    print(prime_factors)
    return prime_factors

def Highest_Prime_Factor(N):
    list_of_prime_factors = Prime_Factors(N)
    highest_prime_factor = max(list_of_prime_factors)
    print(highest_prime_factor)

if __name__ == '__main__':
    user_input =input("Enter a number \n")
    user_input = int(user_input)
    Highest_Prime_Factor(user_input)
