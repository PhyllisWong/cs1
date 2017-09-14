# Project Euler Challenge 1
def fizz_buzz_sums(num):
    sum = 0
    for i in range(num):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum

fizz_buzz_sums(1000)

# project Euler Challenge 2
def fibonoci_sum(num):
    f_sum = 0
    cur = 0
    f_next = 1
    temp = 0
    while cur < num:
        cur = (f_next + temp)
        temp = f_next
        f_next = cur
        if (cur % 2 == 0):
            f_sum += cur
    print(f_sum)
