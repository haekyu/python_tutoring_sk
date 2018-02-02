from time import time


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def dynamic_fib(n, reservoir):
    if n < 2:
        reservoir[n] = 1
        return 1, reservoir
    else:
        # if fib(n - 2) is already calculated
        if reservoir[n - 2] > 0:
            fib_n_2 = reservoir[n - 2]
        # if not
        else:
            fib_n_2, reservoir = dynamic_fib(n - 2, reservoir)

        # if fib(n - 1) is alreadly calculated
        if reservoir[n - 1] > 0:
            fib_n_1 = reservoir[n - 1]
        # if not
        else:
            fib_n_1, reservoir = dynamic_fib(n - 1, reservoir)

        reservoir[n] = fib_n_1 + fib_n_2

        return reservoir[n], reservoir


start = time()
print(fib(40))
end = time()
print('naive fib: %.2lf sec' % (end - start))

start = time()
reservoir = [-1] * 100
fib_40, reservoir = dynamic_fib(40, reservoir)
print(fib_40)
end = time()
print('naive fib: %.2lf sec' % (end - start))

