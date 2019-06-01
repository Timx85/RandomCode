"""
Write a program that asks the user how many Fibonnaci 
numbers to generate and then generates them. Take this 
opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers 
in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers 
where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""
def generate_finonnaci_numbers(nrOfNrs):
    fibonnaciSequence = []
    for number in range(0,nrOfNrs):
        if number == 0 or number ==1:
            fibonnaciSequence.append(number)
        else:
            fibonnaciSequence.append(fibonnaciSequence[number-1] + fibonnaciSequence[number-2])
    return fibonnaciSequence

nrOfNrs = int(input("How many Fibonnaci numbers do you want to generate? "))
print(generate_finonnaci_numbers(nrOfNrs))


