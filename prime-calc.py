def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Generate and display prime numbers between 1 and 250
primes = [num for num in range(1, 251) if is_prime(num)]

# Display the prime numbers
print("Prime numbers between 1 and 250:")
print(primes)

# Store the prime numbers in a file
with open('results.txt', 'w') as file:
    file.write("Prime numbers between 1 and 250:\n")
    file.write(','.join(map(str, primes)))

# Read the contents of results.txt
with open('results.txt', 'r') as file:
    content = file.read()

# Extract prime numbers from the content
# Skip the first line which contains the header
prime_numbers = list(map(int, content.split('\n')[1].split(',')))

# Display the loaded prime numbers
print("Loaded prime numbers:")
print(prime_numbers)


