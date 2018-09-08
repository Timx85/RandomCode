def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and filters out numbers that
       are both positive and even (divisible by 2), try to use a
       list comprehension"""
    even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
    return even_numbers

numbers = [0,2,5,6,7,8,10,100]
print(filter_positive_even_numbers(numbers))