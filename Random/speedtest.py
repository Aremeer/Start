import random
import timeit

def sum_arr(arr):
    return sum(x for x in arr if x >= 0)


def sum_arr_for(arr):
    s = 0
    for n in arr:
        if n >= 0:
            s += n
    return s


arr = random.sample(range(-10000, 10000), 10000)

res_gen = timeit.timeit(lambda: sum_arr(arr), number=1000)
res = timeit.timeit(lambda: sum_arr_for(arr), number=1000)

print(f'res generator is {res_gen}')
print(f'res for loop is {res}')