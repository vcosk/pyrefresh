# fixed argumet functions
def get_sum(num1: int = 1, num2: int = 2):
    print(f'Adding numbers {num1} and {num2}')
    return num1 + num2

# argument order same the function
print(get_sum(-1,2))

# named arguments for the function
print(get_sum(num2=3,num1=-1))

# using default values for function argument
print(get_sum())


# variable argument function
def get_sums(*args):
    print('summing numbers:', args)
    sum = 0
    for value in args:
        sum += value
    return sum

print(get_sums(1,2,4,5,6,7,8,9))

# return multiple values
def next_2(num):
    return num + 1, num + 2

n = 5
print(f'Next two numbers of {n}:', next_2(n))

# unpacking multiple return values
n = 6
n1, n2 = next_2(n)
print(f'Next tow number of {n} are {n1} and {n2}')

# Higher order functions
def multBy(num):
    return lambda x: x*num

multBy5 = multBy(5)
print('3 * 5 =', multBy5(3))

print('4 * 7 =', multBy(7)(4))

def multList(list, func):
    result = []
    for x in list:
        result.append(func(x))
    return result

data = list(range(0,10))
print(f'List {data} scaled by 5:', multList(data, multBy5))