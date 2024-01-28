import math

def pascal(n):
    def binomial_coefficient(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    result = ""
    for i in range(n):
        for j in range(i + 1):
            result += str(binomial_coefficient(i, j))
            if j < i:
                result += " "
        result += "\n"
    
    return result

# Example usage:
n = 3
print(pascal(n))
