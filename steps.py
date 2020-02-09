# start with fibonacci
# nr of solutions for steps 1 or 2
def staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a

#now accept any nr of steps in X like {1,2,5}
#for N is the desired step

def staircase2(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]

print(staircase2(5,{1,2,5}))