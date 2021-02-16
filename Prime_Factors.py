# here we are to find the Prime factors of the given number which is received from the user and Listed in a List
# of Prime Factors:

def Prime_Factors(N):
    prime_factors = list()
    divisor = 2 # smallest prime number to start
    while(divisor <= N):
        if N % divisor == 0: # checking the remainder of the division to be zero
            prime_factors.append(divisor) # adding to the list of the prime factors
            N = N / divisor
        else:
            divisor = divisor + 1 # incrmenting the prime factors if the prime factors do not give a non 0 remainder
    print(prime_factors)
    return prime_factors

if __name__ == '__main__':
    N = input("Enter the Number \n")# getting input from the user
    N = int(N) # possible that the interpreter saves it as a string type so converting it to INT type
    Prime_Factors(N)



