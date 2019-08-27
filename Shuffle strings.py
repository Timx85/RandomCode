import random
import json

def shuffle(input_str):
    input_arr = list(input_str)
    str_len = len(input_arr)

    for i in range(0,str_len):
        random_index = int(random.random() * (str_len - 1))+1
        temp = input_arr[i]
        input_arr[i] = input_arr[random_index]
        input_arr[random_index]= temp
    
    return "".join(input_arr)

print(shuffle("abcde"))

def do_length_match():
    input_str = "averylongstr"

    result = shuffle(input_str)

    if len(result) != len(input_str):
        print("Failed to shuffle: Output does not match input except %s and returned %s" % (len(input_str)),len(result))

do_length_match()

def does_contain_all_letters():
    """
    {   'a':   {  '0':1
            '12':2
            },
        'b': 0
    }
    """

    input_str = "abcde"
    result = {}

    for i in range(0,100):
        shuffled = shuffle(input_str)
        for j,letter in enumerate(shuffled):
            if letter not in result:
                result[letter] = {}
            
            if j not in result[letter]:
                result[letter][j] = 0
            
            result[letter][j] += 1
        
        print(json.dumps(result, indent=4))