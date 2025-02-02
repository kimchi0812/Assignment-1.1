import numbers


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

print(fizz_buzz(3))    
print(fizz_buzz(5))   
print(fizz_buzz(15))   

def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)

print (sum_of_squares([1, 2, 3]))
print (sum_of_squares([2,4,6]))

def count_vowels(string):
    vowels = "aeiouAEIOU" 
    return sum(1 for char in string if char in vowels)

print(count_vowels("hello"))
print(count_vowels("aeiou)"))

from collections import Counter

def count_repeats(string):
    char_counts = Counter(string)
    return sum(1 for char, count in char_counts.items() if count > 1)

print(count_repeats("hello"))
print(count_repeats("aeiou"))

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)