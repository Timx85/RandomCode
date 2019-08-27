x = "Lopen"

def reverse(x):
    output = ""
    for c in x:
        output = c + output
    
    return output

print(reverse(x))

def reverse2(x):
    output_len = len(x)
    output = [None] * output_len
    output_index = output_len - 1
    for c in x:
        output[output_index] = c
        output_index -=1
    
    return ''.join(output)

print(reverse2(x))