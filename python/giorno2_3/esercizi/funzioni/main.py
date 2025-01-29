# Scrivere il codice dell'esercizi qui dentro

def mydivmod (x,y):
    if y == 0:
        raise Exception ("Impossibile dividere per zero")
    else:
        q = x//y
        r = x%y
        result = (q,r)
        return result

def pow_list(seq):
    return [x**2 for x in seq]

def count_words(s):
    conteggio = s.split(' ')
    return len(conteggio)

def reverse_string(s):
    return s[::-1]

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_palindrome(s):
    return s == s[::-1]

def sum_even_numbers(seq):
    return sum(x for x in seq if x % 2 == 0)

def find_max(seq):
    max_value = seq[0]
    for x in seq:
        if x > max_value:
            max_value = x
    return max_value

def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
